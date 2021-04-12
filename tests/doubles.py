from dataclasses import dataclass
from typing import Optional

from src.observer import Event, EventObserver


class FakeView:
    def __init__(self) -> None:
        self.observers: list[EventObserver] = []
        self.bmp: Optional[int] = None

    def register(self, observer: EventObserver) -> None:
        self.observers.append(observer)

    def press_up(self) -> None:
        for observer in self.observers:
            observer.send_event(Event.UP)

    def press_down(self) -> None:
        for observer in self.observers:
            observer.send_event(Event.DOWN)

    def set_bpm(self, value: int) -> None:
        self.bpm = value


@dataclass
class FakeSound:
    calls: int = 0

    def __call__(self) -> None:
        self.calls += 1

    def reset(self) -> None:
        self.calls = 0
