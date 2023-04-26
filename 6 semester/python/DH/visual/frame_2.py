
from tkinter import *
from PIL import Image, ImageTk


class Frame2:

    def __init__(self, control_window):
        self.window_2 = Frame(control_window)
        self.size = [600, 500]
        self.img_2 = ImageTk.PhotoImage(
            Image.open("/home/sergeb/Desktop/MIIT/6 semester/python/DH/img/dh2.png").resize(self.size))
        self.image_2 = Label(self.window_2, image=self.img_2)

    def get_window(self):
        return self.window_2

    def show_frame_2(self, public_key):
        intro_public_key = Label(self.window_2, text="Публичный ключ:", background='red')
        frame_public_key = Label(self.window_2, text="Корень: " + str(public_key[0]) + " , модуль: "
                                                          + str(public_key[1]), background='grey')

        self.image_2.pack(padx=8, pady=8)
        intro_public_key.pack(padx=8, pady=8)
        frame_public_key.pack(padx=8, pady=8)


