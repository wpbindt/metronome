from dataclasses import dataclass

from src.model import Model


@dataclass
class FakeSound:
    calls: int = 0

    def __call__(self) -> None:
        self.calls += 1

    def reset(self) -> None:
        self.calls = 0


@dataclass
class FakeModelObserver:
    updates: int = 0

    def update(self, model: Model) -> None:
        self.updates += 1
