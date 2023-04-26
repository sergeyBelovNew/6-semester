from tkinter import *

from PIL import Image, ImageTk


class FramePublicKey:

    def __init__(self, control_window):
        self.window_intro = Frame(control_window)
        self.size = [600, 450]
        self.img_1 = ImageTk.PhotoImage(
            Image.open("/home/sergeb/Desktop/MIIT/6 semester/python/DH/img/prim_root.png").resize(self.size))

    def get_window(self):
        return self.window_intro

    def show_frame_public_key_formation(self):
        intro = Label(self.window_intro, text="Формирование публичного ключа:", background='red')
        image_1 = Label(self.window_intro, image=self.img_1)
        public_key_idea_1 = Label(self.window_intro,
                          text="У нас есть выражение y = g ^ x mod p, где p — большое простое число,\n"
                               " g — примитивный элемент группы, x - степень в которую мы будем возводить"
                               "(a - Алиса, b - Боб)", background='yellow')
        public_key_idea_2 = Label(self.window_intro,
                                  text="Примитивный элемент группы - элемент группы, который при возведение в степени"
                                       ",\n"
                                       "равные элементам группы, после взятия модуля формирует значения равные\n"
                                       "всем возможным эл-ам группы", background='yellow')
        public_key_idea_3 = Label(self.window_intro,
                                  text="Алиса отправляет Бобу: p,g (публичный ключ)", background='yellow')
        intro.pack(padx=8, pady=8)
        public_key_idea_1.pack(padx=8, pady=8)
        public_key_idea_2.pack(padx=8, pady=8)
        image_1.pack(padx=8, pady=8)
        public_key_idea_3.pack(padx=8, pady=8)

