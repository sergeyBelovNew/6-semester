import tkinter
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk


class Frame2:

    def __init__(self, control_window, public_key):
        self.window_2 = Frame(control_window)

        self.private_params = [0, 0]
        self.public_key = public_key
        self.size = [600, 450]
        self.img_2 = ImageTk.PhotoImage(
            Image.open("/home/sergeb/Desktop/MIIT/6 semester/python/DH/img/dh2.png").resize(self.size))

        self.intro_public_key = Label(self.window_2, text="Публичный ключ:", background='red')
        self.frame_public_key = Label(self.window_2, text="Корень: " + str(public_key[0]) + " , модуль: "
                                                          + str(public_key[1]), background='grey')
        self.frame_alise_degree = Label(self.window_2, text="Введите степень Алисы:", background='grey')
        self.frame_bob_degree = Label(self.window_2, text="Введите степень Боб:", background='grey')

        self.image_2 = Label(self.window_2, image=self.img_2)

        self.degree_alise = Entry(self.window_2)
        self.degree_bob = Entry(self.window_2)

    def get_private_key(self):
        if self.degree_alise.get() and self.degree_bob.get():
            return [int(self.degree_alise.get()), int(self.degree_bob.get())]
        else:
            return [17, 17]

    def get_window(self):
        return self.window_2

    def show_frame_2(self):
        self.image_2.pack(padx=8, pady=8)
        self.intro_public_key.pack(padx=8, pady=8)
        self.frame_public_key.pack(padx=8, pady=8)
        self.frame_alise_degree.pack(padx=8, pady=8)
        self.degree_alise.pack(padx=8, pady=8)
        self.frame_bob_degree.pack(padx=8, pady=8)
        self.degree_bob.pack(padx=8, pady=8)
        button_private = ttk.Button(self.window_2, text="Ввести секретный ключ", command=self.get_private_key())
        button_private.pack(padx=8, pady=8)
