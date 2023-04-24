
from tkinter import *
from tkinter import ttk

from visual.frame_1 import Frame1
from visual.frame_2 import Frame2
from visual.frame_3 import Frame3


class Visual:
    def __init__(self):
        self.window = Tk()
        self.window.title("Визуализация алгоритма обмена ключами")
        self.window.minsize(width=800, height=600)
        self.control_window = ttk.Notebook()

        self.window_1 = Frame1(self.control_window)
        self.window_2 = Frame2(self.control_window, self.window_1.get_public_key())
        self.window_3 = Frame3(self.control_window, self.window_1.get_public_key(), self.window_2.get_private_key())
        self.control_window.add(self.window_1.get_window(), text="Публичный ключ")
        self.control_window.add(self.window_2.get_window(), text="Приватный ключ")
        self.control_window.add(self.window_3.get_window(), text="Приватный ключ(сформированный)")

    def start_app(self):
        self.window_1.show_frame_1()
        self.window_2.show_frame_2()
        self.window_3.show_frame_3()
        self.window.update()
        self.control_window.pack(expand=1, fill='both')
        self.window.mainloop()

