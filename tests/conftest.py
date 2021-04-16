from typing import Generator

import pytest

from etronome.model import Model
from tests.doubles import FakeSound


@pytest.fixture
def sound() -> FakeSound:
    return FakeSound()


@pytest.fixture
def model(sound: FakeSound) -> Generator[Model, None, None]:
    model = Model(bpm=240, beat=sound)
    yield model
    model.quit()
