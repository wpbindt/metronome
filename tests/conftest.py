from typing import Generator

from pytest import fixture

from etronome.beat_counter import BeatCounter
from etronome.model import Model
from tests.doubles import FakeSound


@fixture
def sound() -> FakeSound:
    return FakeSound()


@fixture
def model(sound: FakeSound) -> Generator[Model, None, None]:
    model = Model(bpm=240, beat=sound)
    yield model
    model.quit()

@fixture
def beat_model(model: Model) -> BeatCounter:
    return BeatCounter(model)