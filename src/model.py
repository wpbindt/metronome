from threading import Thread
from time import sleep
from typing import Callable, Protocol


class ModelObserver(Protocol):
    def update(self) -> None:
        ...


class Model:
    def __init__(self, bpm: int, beat: Callable[[], None]) -> None:
        self._bpm: int = bpm
        self._beat = beat
        self.observers: list[ModelObserver] = []
        beat_thread = Thread(target=self._beat_loop)
        beat_thread.start()

    @property
    def bpm(self) -> int:
        return self._bpm

    @bpm.setter
    def bpm(self, value: int) -> None:
        self._bpm = value
        for observer in self.observers:
            observer.update()

    @property
    def seconds_per_beat(self) -> int:
        return 60 / self.bpm

    def _beat_loop(self) -> None:
        while True:
            self._beat()
            sleep(self.seconds_per_beat)

    def register(self, observer: ModelObserver) -> None:
        self.observers.append(observer)
        observer.update()
