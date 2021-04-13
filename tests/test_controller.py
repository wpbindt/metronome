from src.controller import ControlsController, PlayPauseController
from src.model import Model
from tests.doubles import FakeSound


def test_controls_controller():
    fake_sound = FakeSound()
    model = Model(
        beat=fake_sound,
        bpm=120
    )
    controller = ControlsController(model=model)

    with model:
        controller.up_action()
        assert model.bpm == 121

        controller.down_action()
        assert model.bpm == 120


def test_play_pause_controller():
    fake_sound = FakeSound()
    model = Model(beat=fake_sound, bpm=120)
    controller = PlayPauseController(model)

    with model:
        assert model.is_playing
        controller.button_action()
        assert not model.is_playing
        controller.button_action()
        assert model.is_playing
