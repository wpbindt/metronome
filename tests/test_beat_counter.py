from time import sleep

from pytest import approx

from etronome.beat_counter import BeatCounter
from etronome.model import Model


def test_beat_counter_timeout(beat_counter: BeatCounter, model: Model) -> None:
    beat_counter.tap()
    sleep(BeatCounter.TIMEOUT + 0.1)
    beat_counter.tap()
    assert model.bpm == approx(240)


def test_beat_counter(beat_counter: BeatCounter, model: Model) -> None:
    beat_counter.tap()
    sleep(0.5)
    beat_counter.tap()
    assert model.bpm == approx(120)

    sleep(BeatCounter.TIMEOUT + 0.1)

    beat_counter.tap()
    sleep(1/3)
    beat_counter.tap()
    sleep(1/3)
    beat_counter.tap()
    assert model.bpm == approx(180)


def test_beat_counter_average(beat_counter: BeatCounter, model: Model) -> None:
    beat_counter.tap()
    sleep(1/3 - 0.1)
    beat_counter.tap()
    sleep(1/3 + 0.1)
    beat_counter.tap()
    assert model.bpm == approx(180)
