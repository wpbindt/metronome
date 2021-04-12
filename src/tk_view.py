import tkinter as tk

from .observer import Event, EventObserver


class TkView(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self._configure_layout()
        self._configure_actions()

        self.observers = []

    def _configure_layout(self) -> None:
        bpm_frame = tk.Frame(borderwidth=5, height=2, master=self)
        self.bpm_value = tk.Label(text='125', master=bpm_frame)
        bpm = tk.Label(text='bpm', master=bpm_frame)
        self.bpm_value.pack(side=tk.LEFT)
        bpm.pack(side=tk.RIGHT)
        bpm_frame.pack(side=tk.LEFT)

        button_frame = tk.Frame(master=self)
        self.up_button = tk.Button(text='+', width=2, master=button_frame)
        self.down_button = tk.Button(text='-', width=2, master=button_frame)
        self.up_button.pack()
        self.down_button.pack()
        button_frame.pack(side=tk.RIGHT)
        self.pack()

    def _configure_actions(self) -> None:
        self.up_button.bind(
            '<Button 1>',
            lambda tk_event: self._notify(Event.UP)
        )
        self.down_button.bind(
            '<Button 1>',
            lambda tk_event: self._notify(Event.DOWN)
        )

    def set_bpm(self, value: int) -> None:
        self.bpm_value['text'] = str(value)

    def _notify(self, event: Event):
        for observer in self.observers:
            observer.send_event(event)

    def register(self, observer: EventObserver) -> None:
        self.observers.append(observer)
