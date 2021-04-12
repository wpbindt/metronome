from typing import Protocol

from .observer import EventObserver


class View(Protocol):
    observers: list[EventObserver]

    def set_bpm(self, value: int) -> None:
        ...

    def register(self, observer: EventObserver) -> None:
        ...
