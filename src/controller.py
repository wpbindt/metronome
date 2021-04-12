from .model import Model
from .observer import Event
from .view import View


class Controller:
    def __init__(self, view: View, model: Model) -> None:
        self.view = view
        view.register(self)
        self.model = model
        model.register(self)

    def send_event(self, event: Event) -> None:
        if event == Event.UP:
            self._increase_bpm()
        elif event == Event.DOWN:
            self._decrease_bpm()

    def update(self):
        self.view.set_bpm(self.model.bpm)

    def _increase_bpm(self) -> None:
        self.model.bpm += 1

    def _decrease_bpm(self) -> None:
        self.model.bpm -= 1
