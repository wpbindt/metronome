from src.controller import ControlsController
from src.model import Model
from tests.doubles import FakeSound


def test_controller():
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
