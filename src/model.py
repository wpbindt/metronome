import threading
from time import sleep
from typing import Callable, Protocol


class ModelObserver(Protocol):
    def update(self) -> None:
        ...


class Model:
    def __init__(self, bpm: int, beat: Callable[[], None]) -> None:
        self._bpm: int = bpm
        self._beat = beat
        self._observers: list[ModelObserver] = []
        self._initialize_thread()

    def __enter__(self, *args, **kwargs) -> None:
        self.start()

    def __exit__(self, *args, **kwargs) -> None:
        self.stop()

    @property
    def bpm(self) -> int:
        return self._bpm

    @bpm.setter
    def bpm(self, value: int) -> None:
        self._bpm = value
        for observer in self._observers:
            observer.update()

    @property
    def _seconds_per_beat(self) -> int:
        return 60 / self.bpm

    def _initialize_thread(self) -> None:
        self._stop_event = threading.Event()
        self._beat_thread = threading.Thread(target=self._beat_loop)

    def start(self) -> None:
        self._initialize_thread()
        self._beat_thread.start()

    def stop(self) -> None:
        self._stop_event.set()

    def _beat_loop(self) -> None:
        while not self._stop_event.is_set():
            self._beat()
            sleep(self._seconds_per_beat)

    def register(self, observer: ModelObserver) -> None:
        self._observers.append(observer)
        observer.update()
