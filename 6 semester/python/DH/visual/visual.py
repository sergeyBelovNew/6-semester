import tkinter
from tkinter import *
from tkinter import ttk

from visual.frame_1 import Frame1
from visual.frame_2 import Frame2
from visual.frame_3 import Frame3
from visual.frame_intro import FrameIntro
from visual.frame_session_key_formation import FrameSessionKey
from visual.frame_public_key_formation import FramePublicKey


class Visual:
    def __init__(self):
        self.window = Tk()
        self.window.title("Визуализация алгоритма обмена ключами")
        self.window.minsize(width=800, height=800)
        self.control_window = ttk.Notebook()

        self.frame_intro = FrameIntro(self.control_window)
        self.frame_public_key_formation = FramePublicKey(self.control_window)
        self.frame_session_key_formation = FrameSessionKey(self.control_window)
        self.frame_1 = Frame1(self.control_window)
        self.frame_2 = Frame2(self.control_window)
        self.frame_3 = Frame3(self.control_window)

        self.img = PhotoImage(file='/home/sergeb/Desktop/MIIT/6 semester/python/DH/img/favicon-16x16.png')
        self.window.iconphoto(False, self.img)

        self.control_window.add(self.frame_intro.get_window(), text="Вступление")
        self.control_window.add(self.frame_public_key_formation.get_window(), text="Формирование публичного ключа")
        self.control_window.add(self.frame_session_key_formation.get_window(), text="Формирование сессионного ключа")
        self.control_window.add(self.frame_1.get_window(), text="Публичный ключ")
        self.control_window.add(self.frame_2.get_window(), text="Приватный ключ")
        self.control_window.add(self.frame_3.get_window(), text="Приватный ключ(сформированный)")

        self.primitive_root = Entry(self.frame_1.get_window())
        self.mod = Entry(self.frame_1.get_window())
        self.degree_alise = Entry(self.frame_2.get_window())
        self.degree_bob = Entry(self.frame_2.get_window())

        self.public_key = [13, 17]
        self.private_params = [5, 9]

    def start_app(self):

        self.frame_intro.show_frame_intro()
        self.frame_public_key_formation.show_frame_public_key_formation()
        self.frame_session_key_formation.show_frame_session_key_formation()
        self.frame_1.show_frame_1()

        button_public = ttk.Button(self.frame_1.get_window(), text="Ввести публичный ключ",
                                   command=self.show_frame_2)
        intro_input_root = Label(self.frame_1.get_window(), text="Введите примитивный корень:", background='red')
        intro_input_mod = Label(self.frame_1.get_window(), text="Введите модуль:", background='red')

        intro_input_root.pack(padx=8, pady=8)
        self.primitive_root.pack(padx=8, pady=8)
        intro_input_mod.pack(padx=8, pady=8)
        self.mod.pack(padx=8, pady=8)
        button_public.pack(padx=8, pady=8)
        self.control_window.pack(expand=1, fill='both')
        self.window.mainloop()

    def show_frame_2(self):
        self.public_key = [int(self.primitive_root.get()), int(self.mod.get())]
        self.frame_2.show_frame_2(self.public_key)
        frame_alise_degree = Label(self.frame_2.get_window(), text="Введите степень Алисы:", background='grey')
        frame_bob_degree = Label(self.frame_2.get_window(), text="Введите степень Боб:", background='grey')

        frame_alise_degree.pack(padx=8, pady=8)
        self.degree_alise.pack(padx=8, pady=8)
        frame_bob_degree.pack(padx=8, pady=8)
        self.degree_bob.pack(padx=8, pady=8)
        button_private = ttk.Button(self.frame_2.get_window(), text="Ввести секретный ключ",
                                    command=self.show_frame_3)
        button_private.pack(padx=8, pady=8)

    def show_frame_3(self):
        self.private_params = [int(self.degree_alise.get()), int(self.degree_bob.get())]
        self.frame_3.show_frame_3(self.public_key, self.private_params)

