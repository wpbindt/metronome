from time import sleep

from src.model import Model
from tests.doubles import FakeModelObserver, FakeSound


def test_model():
    fake_sound = FakeSound()
    model = Model(bpm=240, beat=fake_sound)
    fake_observer = FakeModelObserver()

    model.start()
    sleep(0.51)
    model.stop()
    assert fake_sound.calls == 3

    sleep(0.51)
    assert fake_sound.calls == 3

    fake_sound.reset()
    model.register(fake_observer)
    model.bpm = 480
    assert fake_observer.updates == 1

    model.start()
    sleep(0.51)
    model.stop()
    assert fake_sound.calls == 5


def test_is_playing():
    fake_sound = FakeSound()
    model = Model(bpm=240, beat=fake_sound)
    fake_observer = FakeModelObserver()
    model.register(fake_observer)

    model.start()
    assert model.is_playing
    assert fake_observer.updates == 1

    model.stop()
    assert not model.is_playing
    assert fake_observer.updates == 2


def test_rapid_start_stop():
    fake_sound = FakeSound()
    model = Model(bpm=240, beat=fake_sound)

    model.start()
    sleep(0.1)
    model.stop()
    model.start()
    sleep(0.41)
    model.stop()
    assert fake_sound.calls == 3
