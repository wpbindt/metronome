from .model import Model


class BeatCounter:
    TIMEOUT = 1

    def __init__(self, model: Model) -> None:
        self.model = model

    def tap(self) -> None:
        ...
