from itertools import cycle
from random import shuffle
from tkinter import *
from tkinter import ttk

from all_setting_game import path_file_rules, path_file_words_from_3, path_file_words_from_4, \
    path_file_words_from_5, BG_COLOR, WHITE, FONT_TEXT_RULES, FONT_NAME_SET

# from os import system
# import pyttsx3
# from pygame import mixer


# mixer.init()
# engine = pyttsx3.init()  # инициализация движка


def play(name_sound):
    """Общая функция для воспроизведения аудиофайла, путь и название аудиофайлов в модуле all_setting_game"""
    pass
    # mixer.music.load(name_sound)
    # mixer.music.play(loops=0)


# def show_rules():
#     """Функция открывает файл txt. В данном случаи с правилами."""
#     system(path_file_rules)  # T.к. мы используем system на windows нужно ставить \\ в других ОС /


# # Зададим свойства
# engine.setProperty('rate', 150)  # скорость речи
# engine.setProperty('volume', 1)  # громкость (0-1)


# def read_text(text_for_read):
#     """Функция воспроизводит введённую фразу, озвучивает текст."""
#     engine.say(text_for_read)  # запись фразы в очередь
#     engine.runAndWait()  # очистка очереди и воспроизведение текста


def create_iter_words_list(path_file):
    """Функция открывает файл txt. Перемешивает список и превращает его в итератор."""
    with open(path_file, 'r', encoding='utf-8') as file_txt:
        list_words = file_txt.readline().split(', ')
        shuffle(list_words)
    return tuple(list_words)


def create_line(string: str, num: int = 24) -> str:
    """Функция получает строку, преобразовывает её в список, делает первое слово с заглавной буквой.
    Возвращает преобразованную строку"""
    list_string = string.split()
    new_string = f'{list_string[0].capitalize()} {" ".join(list_string[1:])}'
    # return new_string
    return f'{new_string[0:num]}\n{new_string[num:]}' if len(new_string) > num else new_string


# words = cycle(create_iter_words_list(path_file_all_words))
words_from_3 = cycle(create_iter_words_list(path_file_words_from_3))
words_from_4 = cycle(create_iter_words_list(path_file_words_from_4))
words_from_5 = cycle(create_iter_words_list(path_file_words_from_5))


def open_win_rules_game(width_window_rules: int = 1920, height_window_rules: int = 1080,
                        name_list: str = "Правила игры", name_file_txt: str = path_file_rules,
                        font_text_rules=FONT_TEXT_RULES):
    """Функция для создания окна с правилами игры или другим текстом.
    В качества аргументов можно предать размеры окна,
    название окна - заглавие и не посредственно путь к файлу txt откуда непосредственно будет взять текст."""
    rules_win = Toplevel()
    rules_win.config(padx=0, pady=0, bg=BG_COLOR)  # Устанавливаем отступ от границ
    rules_win.wm_attributes('-topmost', 1)  # окно будет поверх других
    rules_win.title(name_list)
    rules_win.geometry(f'{width_window_rules}x{height_window_rules}')
    # self.rules_win.protocol('WM_DELETE_WINDOW',
    #                           self.close_win_rules)  # активирует окно уточнения на закрытие окна настроек

    # СОЗДАЁМ ПОЛОСЫ ПРОКРУТКИ
    rules_frame = Frame(rules_win)
    rules_frame.pack(fill=BOTH, expand=1)

    # 2 Создаём рамку для X полосы прокрутки
    sector = Frame(rules_frame)
    sector.pack(fill=X, side=BOTTOM)

    # 3 Создаём Холст
    rules_canvas = Canvas(rules_frame, bg=BG_COLOR)
    rules_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # 4 Добавляем полосу прокрутки на холст
    x_scrollbar_rules = ttk.Scrollbar(sector, orient=HORIZONTAL, command=rules_canvas.xview)
    x_scrollbar_rules.pack(side=BOTTOM, fill=X)
    y_scrollbar_rules = ttk.Scrollbar(rules_frame, orient=VERTICAL, command=rules_canvas.yview)
    y_scrollbar_rules.pack(side=RIGHT, fill=Y)

    # 5 Настройка холста
    rules_canvas.configure(xscrollcommand=x_scrollbar_rules.set)
    rules_canvas.configure(yscrollcommand=y_scrollbar_rules.set)
    rules_canvas.bind("<Configure>",
                      lambda e: rules_canvas.config(scrollregion=rules_canvas.bbox(ALL)))

    # 6 Создаём еще одну рамку ВНУТРИ холста
    second_frame_rules = Frame(rules_canvas, bg=BG_COLOR)

    # 7 Добавляем эту Новую Рамку в окно на Холсте
    rules_canvas.create_window((0, 0), window=second_frame_rules, anchor="nw")

    # Размещаем текст правил

    label_name_rules = Label(second_frame_rules, text=name_list, bg=BG_COLOR, fg=WHITE,
                             font=FONT_NAME_SET)
    label_name_rules.grid(row=0, column=0, sticky=W, padx=10, pady=10)

    with open(name_file_txt, 'r', encoding='utf-8') as file_txt:
        text_rules = file_txt.read()
    label_name_rules = Label(second_frame_rules, text=text_rules, bg=BG_COLOR, fg=WHITE, font=font_text_rules,
                             justify=LEFT, wraplength=width_window_rules * 0.95)
    label_name_rules.grid(row=1, column=0, sticky=W, padx=10, pady=10)

    rules_win.mainloop()
