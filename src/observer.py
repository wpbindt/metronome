from enum import Enum
from typing import Protocol


class Event(Enum):
    UP = 0
    DOWN = 1


class EventObserver(Protocol):
    def send_event(self, event: Event) -> None:
        ...
