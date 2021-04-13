from dataclasses import dataclass


@dataclass
class FakeSound:
    calls: int = 0

    def __call__(self) -> None:
        self.calls += 1

    def reset(self) -> None:
        self.calls = 0
