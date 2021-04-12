from src.controller import Controller
from src.model import Model
from tests.doubles import FakeSound, FakeView


def test_controller():
    fake_sound = FakeSound()
    model = Model(
        beat=fake_sound,
        bpm=120
    )
    view = FakeView()
    controller = Controller(model=model, view=view)

    view.press_down()
    assert view.bpm == 119
    assert model.bpm == 119

    view.press_up()
    assert view.bpm == 120
    assert model.bpm == 120
