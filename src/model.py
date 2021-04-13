from __future__ import annotations
import threading
from time import sleep
from types import TracebackType
from typing import Callable, Optional, Protocol, Type


class ModelObserver(Protocol):
    def update_(self, model: Model) -> None:
        ...


class Model:
    def __init__(self, bpm: int, beat: Callable[[], None]) -> None:
        self._bpm: int = bpm
        self._beat = beat
        self._observers: list[ModelObserver] = []
        self._initialize_thread()
        self._is_playing = False

    def __enter__(self) -> Model:
        self.start()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ) -> None:
        self._observers = []
        self.stop()

    @property
    def bpm(self) -> int:
        return self._bpm

    @bpm.setter
    def bpm(self, value: int) -> None:
        self._bpm = value
        for observer in self._observers:
            observer.update_(self)

    @property
    def is_playing(self) -> bool:
        return self._is_playing

    @is_playing.setter
    def is_playing(self, value: bool) -> None:
        self._is_playing = value
        for observer in self._observers:
            observer.update_(self)

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

    def register(self, observer: ModelObserver) -> None:
        self._observers.append(observer)
