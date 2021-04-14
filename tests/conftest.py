import pytest

from src.model import Model
from tests.doubles import FakeSound


@pytest.fixture
def sound() -> FakeSound:
    return FakeSound()


@pytest.fixture
def model(sound: FakeSound) -> Model:
    return Model(bpm=240, beat=sound)
