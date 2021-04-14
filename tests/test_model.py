from time import sleep

from src.model import Model
from tests.doubles import FakeModelObserver, FakeSound


def test_model(model: Model, sound: FakeSound) -> None:
    fake_observer = FakeModelObserver()

    model.start()
    sleep(0.51)
    model.stop()
    assert sound.calls == 3

    sleep(0.51)
    assert sound.calls == 3

    sound.reset()
    model.register(fake_observer)
    model.bpm = 480
    assert fake_observer.updates == 1

    model.start()
    sleep(0.51)
    model.stop()
    assert sound.calls == 5


def test_is_playing(model: Model, sound: FakeSound) -> None:
    fake_observer = FakeModelObserver()
    model.register(fake_observer)

    model.start()
    assert model.is_playing
    assert fake_observer.updates == 1

    model.stop()
    assert not model.is_playing
    assert fake_observer.updates == 2


def test_rapid_start_stop(model: Model, sound: FakeSound) -> None:
    """
    Previously, this would start up a new metronome thread without ever
    stopping the last, leading to two metronomes sounding at the same
    time.
    """
    model.start()
    sleep(0.1)
    model.stop()
    model.start()
    sleep(0.41)
    model.stop()
    assert sound.calls == 3
