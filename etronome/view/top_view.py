import tkinter as tk

from .controls import Controls
from .display import Display
from .play_pause import PlayPause
from ..model import Model


class TopView(tk.Frame):
    def __init__(self, master: tk.Tk, model: Model) -> None:
        super().__init__(master=master)

        left_frame = tk.Frame(master=self)
        display = Display(master=left_frame, model=model)
        display.pack(side=tk.TOP)

        play_pause = PlayPause(master=left_frame, model=model)
        play_pause.pack(side=tk.BOTTOM)

        left_frame.pack(side=tk.LEFT)

        controls = Controls(master=self, model=model)
        controls.pack(side=tk.RIGHT)

        self.pack()
