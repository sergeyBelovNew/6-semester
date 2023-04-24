
from tkinter import *
from tkinter import ttk

from exchange_keys_dh import ExchangeKeysDH
from humans.alise import Alise
from visual.frame_1 import Frame1
from visual.frame_2 import Frame2


class Frame3:
    def __init__(self, control_window, public_key, private_params):
        self.window_3 = Frame(control_window)
        self.public_key = public_key
        self.private_params = private_params
        self.dh = ExchangeKeysDH(public_key,  private_params)

    def show_frame_3(self):
        intro_public_key = Label(self.window_3, text="Публичный ключ:", background='red')
        frame_public_key = Label(self.window_3, text="Корень: " + str(self.public_key[0]) + ", модуль: "
                                                     + str(self.public_key[1]), background='grey')
        frame_degrees = Label(self.window_3, text="Степень Алисы: " + str(self.private_params[0]) + ", степень Боба: "
                                                     + str(self.private_params[1]), background='grey')
        frame_1 = Label(self.window_3,
                        text="Вычисление резульата Алисы(передаем Бобу): " + str(self.dh.get_alise_private_key()),
                        background='green')
        frame_2 = Label(self.window_3,
                        text="Вычисление результата Боба(передаем Алисе): " + str(self.dh.get_bob_galua_field_result()),
                        background='green')
        frame_3 = Label(self.window_3, text="Секретный ключ Алисы: " +
                                            str(self.dh.get_alise_private_key()), background='grey')
        frame_4 = Label(self.window_3, text="Секретный ключ Боба: " +
                                            str(self.dh.get_bob_private_key()), background='grey')

        intro_public_key.pack(padx=8, pady=8)
        frame_public_key.pack(padx=8, pady=8)
        frame_degrees.pack(padx=8, pady=8)
        frame_1.pack(padx=8, pady=8)
        frame_2.pack(padx=8, pady=8)
        frame_3.pack(padx=8, pady=8)
        frame_4.pack(padx=8, pady=8)

    def get_window(self):
        return self.window_3
