from dataclasses import dataclass
from typing import TypeVar

from src.observable import Observer


@dataclass
class FakeSound:
    calls: int = 0

    def __call__(self) -> None:
        self.calls += 1

    def reset(self) -> None:
        self.calls = 0


T = TypeVar('T')


@dataclass
class FakeObserver(Observer[T]):
    updates: int = 0

    def update_(self, value: T) -> None:
        self.updates += 1
