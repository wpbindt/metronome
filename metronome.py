#!/usr/bin/env python
from argparse import ArgumentParser
import tkinter as tk

from src.controller import Controller
from src.model import Model
from src.sound import play_sound
from src.tk_view import TkView


parser = ArgumentParser()
parser.add_argument('bpm', type=int, default=120)
args = parser.parse_args()

model = Model(bpm=args.bpm, beat=lambda: play_sound('assets/test_sound.wav'))
with model:
    window = tk.Tk()
    view = TkView(master=window)
    controller = Controller(view=view, model=model)
    window.mainloop()
