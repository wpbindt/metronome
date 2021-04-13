import tkinter as tk

from .controller import ControlsController, PlayPauseController
from .model import Model


class Display(tk.Frame):
    def __init__(self, master: tk.Frame, model: Model) -> None:
        super().__init__(master=master, height=2)

        self.bpm = tk.Label(master=self, text=str(model.bpm))
        self.bpm.pack(side=tk.LEFT)

        unit = tk.Label(master=self, text='bpm')
        unit.pack(side=tk.RIGHT)

        model.register(self)

    def update_(self, model: Model) -> None:
        self.bpm['text'] = str(model.bpm)


class Controls(tk.Frame):
    def __init__(
        self,
        master: tk.Frame,
        controller: ControlsController,
    ) -> None:
        super().__init__(master=master)

        up_button = tk.Button(master=self, text='+', width=2)
        up_button.bind('<Button 1>', lambda event: controller.up_action())
        up_button.pack()

        down_button = tk.Button(master=self, text='-', width=2)
        down_button.bind('<Button 1>', lambda event: controller.down_action())
        down_button.pack()


class PlayPauseView(tk.Frame):
    def __init__(
        self,
        master: tk.Frame,
        model: Model,
        controller: PlayPauseController,
    ) -> None:
        super().__init__(master=master)

        self.button = tk.Button(master=self, text='play')
        self.button.bind(
            '<Button 1>',
            lambda event: controller.button_action()
        )
        self.button.pack()

        model.register(self)
        self.update_(model)

    def update_(self, model: Model) -> None:
        self.button['text'] = 'pause' if model.is_playing else 'play'


class View(tk.Frame):
    def __init__(self, master: tk.Tk, model: Model) -> None:
        super().__init__(master=master)

        top_frame = tk.Frame(master=self)
        display = Display(master=top_frame, model=model)
        display.pack(side=tk.LEFT)

        controls_controller = ControlsController(model=model)
        controls = Controls(
            master=top_frame,
            controller=controls_controller,
        )
        controls.pack(side=tk.RIGHT)

        top_frame.pack()

        play_pause_controller = PlayPauseController(model)
        play_pause = PlayPauseView(
            master=self,
            model=model,
            controller=play_pause_controller
        )
        play_pause.pack(side=tk.BOTTOM)

        self.pack()
