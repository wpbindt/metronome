from dataclasses import dataclass
from typing import Generic, TypeVar


@dataclass
class FakeSound:
    calls: int = 0

    def __call__(self) -> None:
        self.calls += 1

    def reset(self) -> None:
        self.calls = 0


T = TypeVar('T')


class FakeObserver(Generic[T]):
    def __init__(self) -> None:
        self.update_values: list[T] = []

    @property
    def updates(self) -> int:
        return len(self.update_values)

    def update_(self, value: T) -> None:
        self.update_values.append(value)

    def reset(self) -> None:
        self.update_values = []
