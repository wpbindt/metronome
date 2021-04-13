#!/usr/bin/env python
from argparse import ArgumentParser
import tkinter as tk

from src.model import Model
from src.sound import play_sound
from src.view import View


parser = ArgumentParser()
parser.add_argument('bpm', type=int, default=120)
args = parser.parse_args()

model = Model(bpm=args.bpm, beat=lambda: play_sound('assets/test_sound.wav'))
with model:
    window = tk.Tk()
    view = View(master=window, model=model)
    window.mainloop()
