from .model import Model


class ControlsController:
    def __init__(self, model: Model) -> None:
        self.model = model

    def up_action(self) -> None:
        self.model.bpm += 1

    def down_action(self) -> None:
        self.model.bpm -= 1
