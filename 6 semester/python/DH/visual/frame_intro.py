from tkinter import *

from PIL import Image, ImageTk


class FrameIntro:

    def __init__(self, control_window):
        self.window_intro = Frame(control_window)
        self.size = [600, 450]
        self.img_1 = ImageTk.PhotoImage(
            Image.open("/home/sergeb/Desktop/MIIT/6 semester/python/DH/img/dh.jpg").resize(self.size))

    def get_window(self):
        return self.window_intro

    def show_frame_intro(self):
        intro = Label(self.window_intro, text="Проблематика передачи секретного ключа в "
                                              "ассимметричной криптографии:", background='red')
        image_1 = Label(self.window_intro, image=self.img_1)
        mitm_idea = Label(self.window_intro, text="Передовая секретный ключ мы сталкиваемся с проблемой возможного "
                                                  "перехвата ключа(MITM). \nРешением данной проблемы выступает алгоритм Диффи-Хеллмана.\n"
                                                  "Суть алгоритма состоит в том, чтобы передовать не сам ключ,\n"
                                                  "а передовать параметры для вычисления ключа, в случае перехвата которых,"
                                                  " человек\n"
                                                  "по середине не сможет вычислить ключ!",
                          background='yellow')
        intro.pack(padx=8, pady=8)
        image_1.pack(padx=8, pady=8)

        mitm_idea.pack(padx=8, pady=8)
