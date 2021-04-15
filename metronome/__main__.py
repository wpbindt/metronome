from argparse import ArgumentParser
import tkinter as tk

from .model import Model
from .sound import play_sound
from .view import View


def get_bpm() -> int:
    parser = ArgumentParser()
    parser.add_argument('bpm', type=int, default=120)
    return parser.parse_args().bpm


def run_metronome(bpm: int) -> None:
    model = Model(bpm=bpm, beat=lambda: play_sound('assets/test_sound.wav'))
    with model:
        window = tk.Tk()
        view = View(master=window, model=model)
        window.mainloop()


def main() -> None:
    bpm = get_bpm()
    run_metronome(bpm)


if __name__ == '__main__':
    main()
