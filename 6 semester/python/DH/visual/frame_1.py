import tkinter
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from humans.alise import Alise
from humans.bob import Bob



class Frame1:

    def __init__(self, control_window):
        self.alise = Alise(4, 5, 17)
        self.window_1 = Frame(control_window)
        self.public_key = [self.alise.get_primitive_root(), self.alise.get_mod()]
        self.bob = Bob(self.public_key, 17)
        self.mod_input = Entry(self.window_1)
        self.root_input = Entry(self.window_1)
        self.size = [600, 450]
        self.img_1 = ImageTk.PhotoImage(Image.open("/home/sergeb/Desktop/MIIT/6 semester/python/DH/img/dh.jpg").resize(self.size))

    def get_public_key(self):
        if self.root_input.get() and self.mod_input.get():
            return [int(self.root_input.get()), int(self.mod_input.get())]
        else:
            return self.public_key

    def get_window(self):
        return self.window_1

    def show_frame_1(self):
        intro = Label(self.window_1, text="Формирование публичного ключа:", background='red')
        intro_input_root = Label(self.window_1, text="Введите примитивный корень:", background='red')
        intro_input_mod = Label(self.window_1, text="Введите модуль:", background='red')
        image_1 = Label(self.window_1, image=self.img_1)
        button_public = ttk.Button(self.window_1, text="Ввести публичный ключ", command=self.get_public_key())

        image_1.pack(padx=8, pady=8)
        intro.pack(padx=8, pady=8)
        intro_input_root.pack(padx=8, pady=8)
        self.root_input.pack(padx=8, pady=8)
        intro_input_mod.pack(padx=8, pady=8)
        self.mod_input.pack(padx=8, pady=8)
        button_public.pack(padx=8, pady=8)





