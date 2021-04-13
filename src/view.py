import tkinter as tk

from .controller import ControlsController
from .model import Model


class Display(tk.Frame):
    def __init__(self, master: tk.Frame, model: Model) -> None:
        super().__init__(master=master, height=2)

        self.bpm = tk.Label(master=self, text=str(model.bpm))
        self.bpm.pack(side=tk.LEFT)

        unit = tk.Label(master=self, text='bpm')
        unit.pack(side=tk.RIGHT)

        model.register(self)

    def update(self, model: Model) -> None:
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


class View(tk.Frame):
    def __init__(self, master: tk.Tk, model: Model) -> None:
        super().__init__(master=master)
        display = Display(master=self, model=model)
        controller = ControlsController(model=model)
        controls = Controls(
            master=self,
            controller=controller,
        )
        display.pack(side=tk.LEFT)
        controls.pack(side=tk.RIGHT)
        self.pack()
