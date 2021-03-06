from __future__ import annotations
from functools import partial
import threading
from time import sleep
from types import TracebackType
from typing import Callable, Optional, Type

from .observable import Observable, Observer
from .utils import bound_float


class Model:
    MIN_BPM = 1
    MAX_BPM = 1015
    bpm = Observable[float](
        observers='_bpm_observers',
        transformer=partial(bound_float, MIN_BPM, MAX_BPM)
    )
    is_playing = Observable[bool]('_is_playing_observers')

    def __init__(self, bpm: float, beat: Callable[[], None]) -> None:
        self._bpm_observers: list[Observer[float]] = []
        self.bpm = bpm
        self._beat = beat
        self._initialize_thread()
        self._is_playing_observers: list[Observer[bool]] = []
        self.is_playing = False

    def __enter__(self) -> Model:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ) -> None:
        self.quit()

    def register_for_bpm(self, observer: Observer[float]) -> None:
        self._bpm_observers.append(observer)

    def register_for_is_playing(self, observer: Observer[bool]) -> None:
        self._is_playing_observers.append(observer)

    @property
    def _seconds_per_beat(self) -> float:
        return 60 / self.bpm

    def _initialize_thread(self) -> None:
        self._can_play = threading.Event()
        self._quit_event = threading.Event()
        beat_thread = threading.Thread(target=self._beat_loop, daemon=True)
        beat_thread.start()

    def start(self) -> None:
        self._can_play.set()
        self.is_playing = True

    def stop(self) -> None:
        self._can_play.clear()
        self.is_playing = False

    def quit(self) -> None:
        self._quit_event.set()
        self._can_play.set()  # cannot quit when paused

    def _beat_loop(self) -> None:
        while True:
            self._can_play.wait()
            if self._quit_event.is_set():
                break
            self._beat()
            sleep(self._seconds_per_beat)
