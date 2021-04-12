from threading import Thread
from time import sleep
from typing import Callable


class Model:
    def __init__(self, beat: Callable[[], None]) -> None:
        self.bpm: int = 120
        self._beat = beat
        beat_thread = Thread(target=self._beat_loop)
        beat_thread.start()

    @property
    def seconds_per_beat(self) -> int:
        return 60 / self.bpm

    def _beat_loop(self) -> None:
        while True:
            self._beat()
            sleep(self.seconds_per_beat)
