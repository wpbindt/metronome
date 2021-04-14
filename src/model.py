from __future__ import annotations
import threading
from time import sleep
from types import TracebackType
from typing import Callable, Optional, Type

from .observable import Observable, Observer


class Model:
    _bpm_observers, bpm = Observable[int].create()
    _is_playing_observers, is_playing = Observable[bool].create()

    def __init__(self, bpm: int, beat: Callable[[], None]) -> None:
        self.bpm = bpm
        self._beat = beat
        self._initialize_thread()
        self.is_playing = False

    def __enter__(self) -> Model:
        self.start()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ) -> None:
        self._bpm_observers[:] = []
        self._is_playing_observers[:] = []
        self.stop()

    def register_for_bpm(self, observer: Observer[int]) -> None:
        self._bpm_observers.append(observer)

    def register_for_is_playing(self, observer: Observer[bool]) -> None:
        self._is_playing_observers.append(observer)

    @property
    def _seconds_per_beat(self) -> float:
        return 60 / self.bpm

    def _initialize_thread(self) -> None:
        self._stop_event = threading.Event()
        self._beat_thread = threading.Thread(
            target=self._beat_loop,
            args=(self._stop_event,)
        )

    def start(self) -> None:
        if self.is_playing:
            return
        self.is_playing = True
        self._initialize_thread()
        self._beat_thread.start()

    def stop(self) -> None:
        self.is_playing = False
        self._stop_event.set()

    def _beat_loop(self, stop_event: threading.Event) -> None:
        while not stop_event.is_set():
            self._beat()
            sleep(self._seconds_per_beat)
