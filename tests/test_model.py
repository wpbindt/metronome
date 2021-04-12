from time import sleep

from src.model import Model
from tests.doubles import FakeSound


def test_model():
    fake_sound = FakeSound()
    model = Model(bpm=240, beat=fake_sound)

    model.start()
    sleep(0.51)
    model.stop()
    assert fake_sound.calls == 3

    sleep(0.51)
    assert fake_sound.calls == 3

    fake_sound.reset()
    model.bpm = 480
    model.start()
    sleep(0.51)
    model.stop()
    assert fake_sound.calls == 5
