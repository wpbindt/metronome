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

    def __enter__(self) -> None:
        self.start()

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ) -> None:
        self.quit()

    def register_for_bpm(self, observer: Observer[int]) -> None:
        self._bpm_observers.append(observer)

    def register_for_is_playing(self, observer: Observer[bool]) -> None:
        self._is_playing_observers.append(observer)

    @property
    def _seconds_per_beat(self) -> float:
        return 60 / self.bpm

    def _initialize_thread(self) -> None:
        self._can_play = threading.Event()
        self._quit_event = threading.Event()
        beat_thread = threading.Thread(target=self._beat_loop)
        beat_thread.start()

    def start(self) -> None:
        self._can_play.set()
        self.is_playing = True

    def stop(self) -> None:
        self._can_play.clear()
        self.is_playing = False

    def quit(self) -> None:
        self._quit_event.set()

    def _beat_loop(self) -> None:
        while not self._quit_event.is_set():
            self._can_play.wait()
            self._beat()
            sleep(self._seconds_per_beat)
