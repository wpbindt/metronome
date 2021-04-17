from etronome.controller import ControlsController, PlayPauseController
from etronome.model import Model


def test_controls_controller(model: Model) -> None:
    controller = ControlsController(model=model)

    model.start()

    controller.up_action()
    assert model.bpm == 241

    controller.down_action()
    assert model.bpm == 240


def test_play_pause_controller(model: Model) -> None:
    controller = PlayPauseController(model)

    model.start()
    assert model.is_playing

    controller.button_action()
    assert not model.is_playing

    controller.button_action()
    assert model.is_playing
