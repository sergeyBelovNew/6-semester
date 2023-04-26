from tkinter import *

from PIL import Image, ImageTk


class FrameSessionKey:

    def __init__(self, control_window):
        self.window_intro = Frame(control_window)
        self.size = [600, 500]
        self.img_1 = ImageTk.PhotoImage(
            Image.open("/home/sergeb/Desktop/MIIT/6 semester/python/DH/img/dh2.png").resize(self.size))

    def get_window(self):
        return self.window_intro

    def show_frame_session_key_formation(self):
        intro = Label(self.window_intro, text="Формирование сессионного ключа:", background='red')
        image_1 = Label(self.window_intro, image=self.img_1)

        session_key_idea_1 = Label(self.window_intro,
                                  text="1)Вычисляем y(y = g ^ a mod p,) для Алисы\n"
                                       "2)Вычисляем y(y = g ^ b mod p,) для Боб\n"
                                       "3)Производим обмен сессионными ключами(y)\n"
                                       "4)Вычисляем приватный ключ: private_key = y ^ a mod g(Алиса),\n"
                                       "private_key = y ^ b mod g(Боб)", background='yellow')
        intro.pack(padx=8, pady=8)

        image_1.pack(padx=8, pady=8)
        session_key_idea_1.pack(padx=8, pady=8)

