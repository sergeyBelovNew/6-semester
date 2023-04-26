from tkinter import *

from PIL import Image, ImageTk


class Frame1:

    def __init__(self, control_window):
        self.window_1 = Frame(control_window)
        self.size = [600, 450]
        self.img_1 = ImageTk.PhotoImage(
            Image.open("/home/sergeb/Desktop/MIIT/6 semester/python/DH/img/dh.jpg").resize(self.size))

    def get_window(self):
        return self.window_1

    def show_frame_1(self):
        intro = Label(self.window_1, text="Формирование публичного ключа:", background='red')
        image_1 = Label(self.window_1, image=self.img_1)

        image_1.pack(padx=8, pady=8)
        intro.pack(padx=8, pady=8)
