
from tkinter import *
from exchange_keys_dh import ExchangeKeysDH


class Frame3:

    def __init__(self, control_window):
        self.window_3 = Frame(control_window)

    def show_frame_3(self, public_key, private_params):
        dh = ExchangeKeysDH(public_key, private_params)
        intro_public_key = Label(self.window_3, text="Публичный ключ:", background='red')
        frame_public_key = Label(self.window_3, text="Корень: " + str(public_key[0]) + ", модуль: "
                                                     + str(public_key[1]), background='grey')
        frame_degrees = Label(self.window_3, text="Степень Алисы: " + str(private_params[0]) + ", степень Боба: "
                                                     + str(private_params[1]), background='grey')
        frame_1 = Label(self.window_3,
                        text="Вычисление резульата Алисы(передаем Бобу): " + str(dh.get_alise_private_key()),
                        background='green')
        frame_2 = Label(self.window_3,
                        text="Вычисление результата Боба(передаем Алисе): " + str(dh.get_bob_galua_field_result()),
                        background='green')
        frame_3 = Label(self.window_3, text="Секретный ключ Алисы: " +
                                            str(dh.get_alise_private_key()), background='grey')
        frame_4 = Label(self.window_3, text="Секретный ключ Боба: " +
                                            str(dh.get_bob_private_key()), background='grey')

        intro_public_key.pack(padx=8, pady=8)
        frame_public_key.pack(padx=8, pady=8)
        frame_degrees.pack(padx=8, pady=8)
        frame_1.pack(padx=8, pady=8)
        frame_2.pack(padx=8, pady=8)
        frame_3.pack(padx=8, pady=8)
        frame_4.pack(padx=8, pady=8)

    def get_window(self):
        return self.window_3
