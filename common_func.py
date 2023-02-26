from itertools import cycle
from random import shuffle
from tkinter import *
from tkinter import ttk

from all_setting_game import path_file_words_from_3, path_file_words_from_4, path_file_words_from_5, \
    BG_COLOR, BLACK, WHITE, RED, WIDTH_WINDOW_GAME, HEIGHT_WINDOW_GAME, STILE_FONT


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
    """Функция получает строку, преобразовывает её в список, делает первое слово с заглавной буквой и переносит слова
    на новую строку если они превышают кол-во эл-тов в строке."""
    list_string = string.split()
    new_string = f'{list_string[0].capitalize()} {" ".join(list_string[1:])}'
    number_enter = num
    while len(new_string) > number_enter:
        index_end_spase = new_string[:number_enter].rfind(' ')
        new_string = f"{new_string[:index_end_spase]}\n{new_string[index_end_spase + 1:]}"
        number_enter += num
    return new_string


# words = cycle(create_iter_words_list(path_file_all_words))
words_from_3 = cycle(create_iter_words_list(path_file_words_from_3))
words_from_4 = cycle(create_iter_words_list(path_file_words_from_4))
words_from_5 = cycle(create_iter_words_list(path_file_words_from_5))


def open_win_rules_or_task(master, width_window_rules: int = WIDTH_WINDOW_GAME,
                           height_window_rules: int = HEIGHT_WINDOW_GAME, color_text: str = WHITE,
                           name_list: str = "Название раздела", name_file_txt: str = 'Текст отсутствует'):
    """Функция для создания окна с правилами игры или другим текстом. В качества аргументов можно предать размеры окна,
    название окна - заглавие и не посредственно путь к файлу txt откуда непосредственно будет взят текст."""
    if '.txt' in name_file_txt:
        with open(name_file_txt, 'r', encoding='utf-8') as file_txt:
            text_rules = file_txt.read()

        font_text_num, font_name_num = 18, 22

    else:
        text_rules = name_file_txt

        width_window_rules = int(width_window_rules * 0.7)
        height_window_rules = int(height_window_rules * 0.7)

        font_text_num, font_name_num = 96, 72
        color_text = WHITE if color_text == BLACK else color_text
        name_list = name_list.replace("(", "для всех!!! (") if color_text == RED else name_list

    rules_win = Toplevel(master)
    rules_win.config(padx=0, pady=0, bg=BG_COLOR)  # Устанавливаем отступ от границ
    # rules_win.wm_attributes('-topmost', 1)  # окно будет поверх других
    rules_win.title(name_list)
    rules_win.geometry(f'{width_window_rules}x{height_window_rules}')
    # self.rules_win.protocol('WM_DELETE_WINDOW',
    #                           self.close_win_rules)  # активирует окно уточнения на закрытие окна

    font_name_set = (STILE_FONT, int(font_name_num * width_window_rules / 1980), 'bold')
    font_text_rules = (STILE_FONT, int(font_text_num * width_window_rules / 1980))

    # СОЗДАЁМ ПОЛОСЫ ПРОКРУТКИ
    rules_frame = Frame(rules_win)
    rules_frame.pack(fill=BOTH, expand=1)

    # 2 Создаём рамку для X полосы прокрутки
    sector = Frame(rules_frame)
    sector.pack(fill=X, side=BOTTOM)

    # 3 Создаём Холст
    rules_canvas = Canvas(rules_frame, bg=BG_COLOR)
    rules_canvas.bind_all("<MouseWheel>", lambda x: on_mousewheel_rul(x))
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

    # Размещаем текст
    label_name_rules = Label(second_frame_rules, text=name_list, bg=BG_COLOR, fg=WHITE,
                             font=font_name_set)
    label_name_rules.grid(row=0, column=0, sticky=W, padx=10, pady=10)

    label_name_rules = Label(second_frame_rules, text=text_rules, bg=BG_COLOR, fg=color_text, font=font_text_rules,
                             justify=LEFT, wraplength=width_window_rules * 0.95)
    label_name_rules.grid(row=1, column=0, sticky=W, padx=10, pady=10)

    def on_mousewheel_rul(event):
        """Функция для прокручивания окна колёсиком мыши, а не бегунком справа."""
        try:
            rules_canvas.yview_scroll(-1 * int(event.delta / 120), "units")
        except TclError:
            rules_canvas.unbind_all("<MouseWheel>")
