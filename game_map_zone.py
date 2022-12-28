from math import floor
from random import choice, randint
from tkinter import *
from tkinter import Toplevel
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import ttk

from all_setting_game import *
from common_func import *


class GamesWindow:

    def __init__(self, width_window_game=WIDTH_WINDOW_GAME, height_window_game=HEIGHT_WINDOW_GAME,
                 count_team=NUMBER_TEAMS):
        number_field = 0
        # Для окна
        self.window = Tk()
        self.window.title(NAME_GAME)
        self.width_window_game = width_window_game
        self.height_window_game = height_window_game
        self.window.geometry(f'{self.width_window_game}x{self.height_window_game}')  # параметры окна игры
        self.window.config(padx=0, pady=0, bg=BG_COLOR)  # Устанавливаем отступ от границ
        # self.window.wm_attributes('-transparentcolor',
        #                           COLOR_INVISIBLE)  # делает конкретный цвет прозрачным (будет видно экран пк)
        # self.window.wm_attributes('-topmost', 1)  # если оставить данную команды то окно настроек всегда будет уходить
        # на задний фон при изменении цвета фигуры
        self.window.protocol('WM_DELETE_WINDOW', self.close_win_game)

        # Для холста карты
        self.width_field = int(self.width_window_game / 1.37)
        self.height_field = int(self.height_window_game / 1.2)
        self.step_x, self.step_y = int(self.width_field / 7), int(self.height_field / 15)
        self.x1, self.y1 = x1, y_1
        self.x2, self.y2 = self.x1 + self.step_x, self.y1 + self.step_y
        self.line_indent = int(self.step_y / 3)
        self.number_line = NUMBER_LINE
        self.step_zero = step_zero
        self.random_game_map = {}

        # Для холста карточек
        self.width_field_card = int(self.width_window_game / 4)
        self.height_field_card = int(self.height_window_game / 1.2)
        self.size_rectangle_card = int(self.width_field_card / 5.3)
        self.y_line_card = int(self.height_field_card / 3)
        self.y_line_card_step = self.size_rectangle_card + 10
        self.label_list = []
        self.num = 24

        # Для команд
        self.indent_line_team = INDENT_LINE_TEAM
        self.count_team = count_team
        self.poly_dict, self.poly_dict_set = {}, {}
        self.x_position_team = int(self.width_field * 0.77)

        # Для окна настроек
        self.width_win_setting = int(self.width_window_game / 1.6)
        self.height_win_setting = int(self.height_window_game / 1.5)
        self.height_canvas_setting = int(self.height_window_game / 6)

        self.x1_rectangle, self.y1_rectangle = x1_rectangle, y1_rectangle
        self.y2_rectangle = int(self.height_canvas_setting / 1.6)
        self.step_x1_rectangle = int(self.width_win_setting / 6 / 1.1)
        self.step_x1_create_rectangle = int(self.width_win_setting / 6 / 6.6)

        self.COUNT_TEAM_LIST = COUNT_TEAM_LIST  # список кол-ва команд
        self.name_team, self.color_team = NAME_TEAM, COLOR_TEAM

        # CОЗДАЁМ МЕНЮ НАСТРОЕК
        self.main_menu = Menu(self.window)
        self.window.config(menu=self.main_menu)
        self.main_menu.add_command(label='Настройки игры', command=self.open_win_setting_game)
        self.main_menu.add_command(label='Правила игры',
                                   command=lambda: open_win_rules_game(width_window_rules=self.width_window_game,
                                                                       height_window_rules=self.height_window_game))
        self.main_menu.add_command(label='Управление игры',
                                   command=lambda: open_win_rules_game(width_window_rules=self.width_window_game,
                                                                       height_window_rules=self.height_window_game,
                                                                       name_list="Управление игры",
                                                                       name_file_txt=path_file_control))
        # пока открыт текстовый документ играть нельзя

        # CОЗДАЁМ ПОЛОСЫ ПРОКРУТКИ НА СЛУЧАЙ ЕСЛИ РАЗРЕШЕНИЕ ЭКРАНА БУДЕН НЕ fullHD
        # 1 Создаём основной фрейм
        self.main_frame = Frame(self.window)
        self.main_frame.pack(fill=BOTH, expand=1)

        # 2 Создаём рамку для X полосы прокрутки
        self.sec = Frame(self.main_frame)
        self.sec.pack(fill=X, side=BOTTOM)

        # 3 Создаём Холст
        self.my_canvas = Canvas(self.main_frame, bg=BG_COLOR)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # 4 Добавляем полосу прокрутки на холст
        self.x_scrollbar = ttk.Scrollbar(self.sec, orient=HORIZONTAL, command=self.my_canvas.xview)
        self.x_scrollbar.pack(side=BOTTOM, fill=X)
        self.y_scrollbar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.y_scrollbar.pack(side=RIGHT, fill=Y)

        # 5 Настройка холста
        self.my_canvas.configure(xscrollcommand=self.x_scrollbar.set)
        self.my_canvas.configure(yscrollcommand=self.y_scrollbar.set)
        self.my_canvas.bind("<Configure>", lambda e: self.my_canvas.config(scrollregion=self.my_canvas.bbox(ALL)))

        # 6 Создаём еще одну рамку ВНУТРИ холста
        self.second_frame = Frame(self.my_canvas, bg=BG_COLOR)

        # 7 Добавляем эту Новую Рамку в окно на Холсте
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # CОЗДАЁМ ИЗОБРАЖЕНИЯ ДЛЯ ПОЛЕЙ КАРТЫ И КАРТОЧЕК
        self.image_dialogue = PhotoImage(file=name_image_dialogue)
        self.image_gestures = PhotoImage(file=name_image_gestures)
        self.image_painting = PhotoImage(file=name_image_painting)

        self.button_card_3 = PhotoImage(file=name_image_card3)
        self.button_card_4 = PhotoImage(file=name_image_card4)
        self.button_card_5 = PhotoImage(file=name_image_card5)

        # Словарь для создания карты (значки действий и цвет поля)
        self.DICT_ACTIONS = {
            'PINK': (self.image_gestures, PINK),
            'ORANGE': (self.image_gestures, ORANGE),
            'BLUE': (self.image_dialogue, BLUE),
            'DARK_BLUE': (self.image_dialogue, DARK_BLUE),
            'GREEN': (self.image_painting, GREEN),
            'YELLOW': (self.image_painting, YELLOW),
        }

        # # Словарь для создания стандартной карты (значки действий и цвет поля).
        # # Для игры на данной карте нужно в данном коде заменить self.random_game_map на self.game_map
        # self.game_map = {
        #     1: (BLUE, self.label_dialogue),
        #     2: (YELLOW, self.label_painting),
        #     3: (PINK, self.label_gestures),
        #     4: (BLUE, self.label_dialogue),
        #     5: (BLUE, self.label_dialogue),
        #     6: (ORANGE, self.label_gestures),
        #     7: (DARK_BLUE, self.label_dialogue),
        #     8: (GREEN, self.label_painting),
        #     9: (PINK, self.label_gestures),
        #     10: (BLUE, self.label_dialogue),
        #     11: (GREEN, self.label_gestures),
        #     12: (DARK_BLUE, self.label_dialogue),
        #     13: (YELLOW, self.label_painting),
        #     14: (PINK, self.label_gestures),
        #     15: (ORANGE, self.label_gestures),
        #     16: (YELLOW, self.label_painting),
        #     17: (BLUE, self.label_dialogue),
        #     18: (PINK, self.label_gestures),
        #     19: (ORANGE, self.label_gestures),
        #     20: (PINK, self.label_gestures),
        #     21: (GREEN, self.label_painting),
        #     22: (YELLOW, self.label_painting),
        #     23: (GREEN, self.label_painting),
        #     24: (ORANGE, self.label_gestures),
        #     25: (GREEN, self.label_painting),
        #     26: (DARK_BLUE, self.label_dialogue),
        #     27: (PINK, self.label_gestures),
        #     28: (BLUE, self.label_dialogue),
        #     29: (ORANGE, self.label_gestures),
        #     30: (DARK_BLUE, self.label_dialogue),
        #     31: (YELLOW, self.label_painting),
        #     32: (GREEN, self.label_painting),
        #     33: (YELLOW, self.label_painting),
        #     34: (ORANGE, self.label_gestures),
        #     35: (ORANGE, self.label_gestures),
        #     36: (BLUE, self.label_dialogue),
        #     37: (PINK, self.label_gestures),
        #     38: (GREEN, self.label_painting),
        #     39: (YELLOW, self.label_painting),
        #     40: (PINK, self.label_gestures),
        #     41: (GREEN, self.label_painting),
        #     42: (DARK_BLUE, self.label_dialogue),
        #     43: (DARK_BLUE, self.label_dialogue),
        #     44: (ORANGE, self.label_gestures),
        #     45: (BLUE, self.label_dialogue),
        #     46: (YELLOW, self.label_painting),
        #     47: (PINK, self.label_gestures),
        #     48: (ORANGE, self.label_gestures),
        # }

        # Словарь для случайной карты на основе данных из self.DICT_ACTIONS.
        # Если игра будет на стандартной карте, то данный цикл нужно закомментировать

        for ind in range(FINISH - 1):
            self.key_DICT_ACTIONS = choice(tuple(self.DICT_ACTIONS.keys()))
            action, color = self.DICT_ACTIONS[self.key_DICT_ACTIONS][0], self.DICT_ACTIONS[self.key_DICT_ACTIONS][1]
            self.random_game_map[ind + 1] = (color, action)

        # СОЗДАЁМ ЛОГОТИП ИГРЫ И РАЗМЕЩАЕМЕГО
        self.label_info = Label(self.second_frame, text=NAME_GAME, font=PARAMETERS_FONT_LABEL, bg=BG_COLOR, fg=YELLOW,
                                highlightthickness=0)
        self.label_info.grid(row=0, column=2, pady=0, padx=0, columnspan=3)

        # СОЗДАЁМ ХОЛСТ ДЛЯ КАРТЫ
        # Игровая карта
        self.canvas_map = Canvas(self.second_frame, width=self.width_field, height=self.height_field, bg=BG_COLOR,
                                 highlightthickness=4)  # сделать highlightthickness=0, если рамка не нужна

        self.canvas_map.grid(row=1, column=2, pady=0, padx=0)

        # Поле старта
        self.canvas_map.create_text(self.width_field - 150, self.step_y / 2, text='Старт', fill=YELLOW, font=FONT_NAME)

        # Цикл для создания игровых клеток(игровой карты)
        for num, color in self.random_game_map.items():
            number_field += 1
            num -= 1
            while num >= COUNT_CAGE_IN_LINE:
                num %= COUNT_CAGE_IN_LINE

            if self.number_line % 2 == 0:
                self.canvas_map.create_rectangle(self.x1 + self.step_x * num, self.y1, self.x2 + self.step_x * num,
                                                 self.y2, fill=color[0], outline=BLACK, width=WIDTH_RECTANGLE_LINE)
                self.canvas_map.create_image(self.x1 + self.step_x * num + (self.step_x / 6), self.y1 + self.step_y / 2,
                                             image=color[1])
                self.canvas_map.create_text(self.x1 + self.step_x * num + (self.step_x * 0.9),
                                            self.y1 + self.step_y - (self.step_y / 4),
                                            text=f'{number_field}', fill=BLACK, font=FONT_TEXT_NUMBER)

            else:
                abs_coefficient = abs(num - COUNT_CAGE_IN_LINE_1)
                self.canvas_map.create_rectangle(self.x1 + self.step_x * abs_coefficient, self.y1,
                                                 self.x2 + self.step_x * abs_coefficient, self.y2,
                                                 fill=color[0], outline=BLACK, width=WIDTH_RECTANGLE_LINE)
                self.canvas_map.create_image(self.x1 + self.step_x * abs_coefficient + (self.step_x / 6),
                                             self.y1 + self.step_y / 2, image=color[1])
                self.canvas_map.create_text(self.x1 + self.step_x * abs_coefficient + (self.step_x * 0.9),
                                            self.y1 + self.step_y * 0.75, text=f'{number_field}', fill=BLACK,
                                            font=FONT_TEXT_NUMBER)

            # РАЗДЕЛИТЕЛЬНАЯ ЛИНИЯ между строками и переход на следующую линию
            if num + 1 == COUNT_CAGE_IN_LINE:
                if self.number_line % 2 > 0:
                    self.canvas_map.create_rectangle(self.x1, self.y1 + self.step_y, self.x2,
                                                     self.y2 + self.line_indent, fill=BLACK, outline=BLACK,
                                                     width=WIDTH_RECTANGLE_LINE)
                    self.y1 += self.step_y + self.line_indent
                    self.y2 += self.step_y + self.line_indent
                    self.number_line += 1
                else:
                    self.canvas_map.create_rectangle(self.x1 + self.step_x * (COUNT_CAGE_IN_LINE - 1),
                                                     self.y1 + self.step_y,
                                                     self.x2 + self.step_x * (COUNT_CAGE_IN_LINE - 1),
                                                     self.y2 + self.line_indent, fill=BLACK,
                                                     outline=BLACK, width=WIDTH_RECTANGLE_LINE)
                    self.y1 += self.step_y + self.line_indent
                    self.y2 += self.step_y + self.line_indent
                    self.number_line += 1

            self.step_zero = num

        # Поле Финиша
        self.canvas_map.create_text(self.x1 + self.step_x * self.step_zero + (self.step_x * 1.5),
                                    self.y1 + self.step_y / 2, text='ФИНИШ', fill=WHITE, font=FONT_NAME)

        # Таймер
        self.canvas_map.create_text(self.width_field - 150, self.height_field - self.step_y * 4, text='Таймер',
                                    fill=YELLOW,
                                    font=FONT_NAME)
        self.timer_text = self.canvas_map.create_text(self.width_field - 150, self.height_field - self.step_y * 3.25,
                                                      text='00:00', fill=WHITE, font=FONT_NAME)

        # Кнопки таймера
        self.button_start = Button(text='Старт', font=PARAMETERS_FONT_BUTTON, command=self.push_start,
                                   highlightthickness=0)
        self.button_start.configure(width=26, activebackground=YELLOW, relief=FLAT)
        self.button_start_win = self.canvas_map.create_window(self.width_field - self.step_x * 1.5,
                                                              self.height_field - self.step_y * 2.75,
                                                              anchor=NW, window=self.button_start)

        self.button_pause = Button(text='Пауза', font=PARAMETERS_FONT_BUTTON, command=self.push_stop,
                                   highlightthickness=0)
        self.button_pause.configure(width=26, activebackground=YELLOW, relief=FLAT)
        self.button_pause_win = self.canvas_map.create_window(self.width_field - self.step_x * 1.5,
                                                              self.height_field - self.step_y * 1.75,
                                                              anchor=NW, window=self.button_pause)

        self.button_res = Button(text='Продолжить', font=PARAMETERS_FONT_BUTTON, command=self.resume,
                                 highlightthickness=0)
        self.button_res.configure(width=26, activebackground=YELLOW, relief=FLAT)
        self.button_res_win = self.canvas_map.create_window(self.width_field - self.step_x * 1.5,
                                                            self.height_field - self.step_y * 0.75,
                                                            anchor=NW, window=self.button_res)

        # СОЗДАЁМ ХОЛСТ ДЛЯ КАРТОЧЕК
        self.canvas_cards = Canvas(self.second_frame, width=self.width_field_card, height=self.height_field_card,
                                   bg=BG_COLOR,
                                   highlightthickness=4)  # сделать highlightthickness=0, если рамка не нужна

        self.canvas_cards.create_text(int(self.width_field_card / 2), FONT_NAME[1], text='Карточки', fill=YELLOW,
                                      font=FONT_NAME)

        # Кнопки карточек (карточки это кнопки)
        # image=переменная изображения # аргумент превращающий вн-ий вид кнопки в изо-ие, например, self.label_finish

        button_card_3 = Button(command=self.push_card_3, highlightthickness=0, bd=0, text='3', bg=GREEN, fg=YELLOW,
                               font=PARAMETERS_FONT_BUTTON_CARD)
        button_card_3.configure(activebackground=YELLOW, relief=FLAT)
        button_card_3_win = self.canvas_cards.create_window(10 + int(self.width_field_card / 3 * 0), FONT_NAME[1] * 2,
                                                            anchor=NW, window=button_card_3)

        button_card_4 = Button(command=self.push_card_4, highlightthickness=0, bd=0, text='4', bg=GREEN, fg=YELLOW,
                               font=PARAMETERS_FONT_BUTTON_CARD)
        button_card_4.configure(activebackground=YELLOW, relief=FLAT)
        button_card_4_win = self.canvas_cards.create_window(10 + int(self.width_field_card / 3 * 1), FONT_NAME[1] * 2,
                                                            anchor=NW, window=button_card_4)

        button_card_5 = Button(command=self.push_card_5, highlightthickness=0, bd=0, text='5', bg=GREEN, fg=YELLOW,
                               font=PARAMETERS_FONT_BUTTON_CARD)
        button_card_5.configure(activebackground=YELLOW, relief=FLAT)
        button_card_5_win = self.canvas_cards.create_window(10 + int(self.width_field_card / 3 * 2), FONT_NAME[1] * 2,
                                                            anchor=NW, window=button_card_5)

        for num_line_card in range(6):
            key = TUPLE_COLOR[num_line_card]
            self.canvas_cards.create_rectangle(10, self.y_line_card + self.y_line_card_step * num_line_card,
                                               10 + self.size_rectangle_card,
                                               self.y_line_card + self.y_line_card_step * num_line_card + self.size_rectangle_card,
                                               fill=self.DICT_ACTIONS[key][1], outline=BLACK,
                                               width=WIDTH_RECTANGLE_LINE)

            self.canvas_cards.create_rectangle(10 + self.size_rectangle_card,
                                               self.y_line_card + self.y_line_card_step * num_line_card,
                                               self.width_field_card - 10,
                                               self.y_line_card + self.y_line_card_step * num_line_card + self.size_rectangle_card,
                                               fill=WHITE, outline=BLACK,
                                               width=WIDTH_RECTANGLE_LINE)

            self.canvas_cards.create_image(int(self.size_rectangle_card / 1.7),
                                           self.y_line_card + self.y_line_card_step * num_line_card + 40,
                                           image=self.DICT_ACTIONS[key][0])
            self.label_line = self.canvas_cards.create_text(20 + self.size_rectangle_card,
                                                            4 + self.y_line_card + self.y_line_card_step * num_line_card,
                                                            text='', justify=LEFT, fill=BLACK,
                                                            font=PARAMETERS_FONT_LABEL_LINE_CARD, anchor=NW)
            self.label_list.append(self.label_line)

        self.update_figur_map()
        self.canvas_cards.grid(row=1, column=3, pady=0, padx=0)
        self.window.mainloop()

    # Функции для уточнения закрытия окон
    # def close_win_setting(self):
    #     """Уточняющее окно при закрытии окна настроек"""
    #     if messagebox.askokcancel('Выход из настроек', 'Хотите выйти из настроек?'):
    #         self.setting_win.destroy()

    # def close_win_rules(self):
    #     """Уточняющее окно при закрытии окна правил игры"""
    #     if messagebox.askokcancel('Выход из настроек', 'Хотите закрыть правила игры?'):
    #         self.rules_win.destroy()

    def close_win_game(self):
        """Функция запускает уточняющее окно при закрытии окна игры"""
        if messagebox.askokcancel('Выход из игры', 'Хотите выйти из игры?'):
            self.window.destroy()

    # Функции для Таймера и его кнопок
    def push_stop(self):
        """Останавливает таймер и активирует функцию запуск аудиофайла"""
        play(NAME_SOUND_TIME_PAUSE)
        self.window.after_cancel(self.timer)

    def push_start(self):
        """Запускает таймер заново и активирует функцию запуск аудиофайла,
        обязательно должна быть нажата кнопка стоп/пауза перед использованием если таймер уже идёт"""
        play(NAME_SOUND_TIME_START)
        self.timer_start(time_round)
        # read_text('Время пошло')

    def timer_start(self, count):
        """Обновляет значения на экране таймера 59,58,57 и т.д.
        Когда время кончится, будет активирована функцию запуск аудиофайла"""

        self.count_min = floor(count / 60)
        if 10 > self.count_min:
            self.count_min = f'0{self.count_min}'

        self.count_sec = count % 60
        if 10 > self.count_sec:
            self.count_sec = f'0{self.count_sec}'

        self.canvas_map.itemconfig(self.timer_text, text=f'{self.count_min}:{self.count_sec}')

        if count > 0:
            self.count_pause = count

            self.timer = self.window.after(TIMER_MILLISECONDS, self.timer_start, count - 1)
        else:
            play(NAME_SOUND_TIME_UP)
            messagebox.showinfo(title="Внимание!", message="Время кончилось!")

    def resume(self):
        """Запускается только если таймер был на паузе т.е. запускает таймер с того значения где он был остановлен и
        активирует функцию запуск аудиофайла"""
        play(NAME_SOUND_TIME_CONTINUE)
        self.timer = self.window.after(TIMER_MILLISECONDS, self.timer_start, self.count_pause - 1)

    # Функции для карточек

    def get_card(self, lst_words):
        """
        Функция для создания карточки для команды, активируется если кликнуть по карте 3,4 или 5.
        Функции передаётся аргумент - это список со словами для случайного отбора в карточку.
        Также случайно делает текст одной из позиций карточки красной, 50/50 вероятность что этого не произойдёт.
        Если есть позиция для всех, то будет аудио-уведомление.
        """
        random_line = randint(0, 6)
        for num_line_card in range(6):
            item = self.label_list[num_line_card]

            self.canvas_cards.itemconfig(item, text=create_line(next(lst_words)), fill=BLACK)

            if random_line == num_line_card:
                if choice((True, False)):
                    self.canvas_cards.itemconfig(item, fill=RED)
                    play(NAME_SOUND_ALL)
                    messagebox.showinfo(title="Внимание!", message="Присутствует общее слово!")

    def push_card_3(self):
        """Функция активирует функцию get_card с передачей ей аргумента words.
        Для улучшения генерации карточек по сложности использовать words_from_3 вместо words.
        Для пополнения базы слов нужно заносить слова в файл 'txt_files/words_from_3.txt'"""
        self.get_card(words_from_3)

    def push_card_4(self):
        """Функция активирует функцию get_card с передачей ей аргумента words.
        Для улучшения генерации карточек по сложности использовать words_from_4 вместо words.
        Для пополнения базы слов нужно заносить слова в файл 'txt_files/words_from_4.txt'"""
        self.get_card(words_from_4)

    def push_card_5(self):
        """Функция активирует функцию get_card с передачей ей аргумента words.
        Для улучшения генерации карточек по сложности использовать words_from_5 вместо words.
        Для пополнения базы слов нужно заносить слова в файл 'txt_files/words_from_5.txt'"""
        self.get_card(words_from_5)

    def move(self, event):
        """Функция позволяет передвигать указанные лейблы или фигуры по экрану. Это облегчает движок игры.
        Можно двигать фишки в любой момент игры"""
        mouse_x = self.window.winfo_pointerx() - self.window.winfo_rootx()
        mouse_y = self.window.winfo_pointery() - self.window.winfo_rooty()
        event.widget.place(x=mouse_x, y=mouse_y, anchor=CENTER)

    # Функции для работы с окном настроек, его созданием и обновлением
    def update_figur_map(self):
        """Функция создаёт фигурки игроков на карте.
        Если нажать обновить в настройках, то фигуры отобразятся, но на позиции старт.
        Цвета и название команд сохраняются даже если уменьшить кол-во команд, а потом снова сделать больше.
        Цвет и название меняются сразу из настроек"""
        self.el_list = [str(i + 1) for i in range(self.count_team)]  # список с номерами команд для бокса номеров команд
        self.indent_line_team = INDENT_LINE_TEAM

        for i in range(self.count_team):
            # Для карты
            self.indent_line_team += 0.5
            self.text_num_team = self.canvas_map.create_text(self.x_position_team,
                                                             self.step_y * (self.indent_line_team + i),
                                                             text=f'Команда №{i + 1}', fill=YELLOW,
                                                             font=FONT_TEAM, anchor=W)  # Порядковый номер Команды
            self.text_name_team = self.canvas_map.create_text(self.x_position_team,
                                                              self.step_y * (self.indent_line_team + 0.5 + i),
                                                              text=self.name_team[i], fill=YELLOW, justify=LEFT,
                                                              font=FONT_NAME_TEAM, anchor=W, )  # Название Команды

            self.label_fig_team = Label(text=f"{i + 1}", font=FONT_NUM_TEAM_SET, bg=self.color_team[i], fg='black',
                                        highlightthickness=2, highlightbackground=BLACK)  # Фигурка Команды

            self.binding = self.label_fig_team.bind("<B1-Motion>", self.move)  # активация движка на перемещение мышкой
            self.label_fig_team_s = self.canvas_map.create_window(self.x_position_team - 36,
                                                                  self.step_y * (self.indent_line_team - 0.25 + i),
                                                                  anchor=NW, window=self.label_fig_team)
            self.poly_dict[i] = [self.text_num_team, self.text_name_team, self.label_fig_team, self.binding,
                                 self.label_fig_team_s]

    def update_figur_setting(self):
        """Функция обновления фигур в окне настроек на основании числа команд.
        Это чисто визуальное отображение в окне настроек, но они показывают как это будет выглядеть на игровой карте"""

        for i in range(self.count_team):
            self.text_team_set = self.canvas_fig.create_text(
                self.x1_rectangle + self.step_x1_create_rectangle * 0 + self.step_x1_rectangle * i, 5,
                text=f'Команда №{i + 1}', fill=YELLOW, font=FONT_TEXT_TEAM_SET, anchor=NW)

            self.points_set = [
                self.x1_rectangle + self.step_x1_create_rectangle * 0 + self.step_x1_rectangle * i, self.y1_rectangle,
                self.x1_rectangle + self.step_x1_create_rectangle * 2 + self.step_x1_rectangle * i, self.y2_rectangle,
            ]
            self.polygon_team_set = self.canvas_fig.create_rectangle(self.points_set, fill=self.color_team[i],
                                                                     outline='#000', width=1.5)
            self.num_team_fig = self.canvas_fig.create_text(
                self.x1_rectangle + self.step_x1_create_rectangle + self.step_x1_rectangle * i,
                self.y2_rectangle // 2,
                text=f'{i + 1}', fill=BLACK, anchor=W, font=FONT_NUM_TEAM_SET)

            self.name_team_set = self.canvas_fig.create_text(
                self.x1_rectangle + self.step_x1_create_rectangle * 0 + self.step_x1_rectangle * i, self.y2_rectangle,
                text=self.name_team[i], fill=YELLOW, anchor=NW)

            self.poly_dict_set[i] = [self.text_team_set, self.name_team_set, self.polygon_team_set, self.num_team_fig]

            # Список-бокс выбора номера команды для изменения цвета, меняется если обновить данные по кол-ву команд
            self.combobox = ttk.Combobox(self.setting_win, values=self.el_list, state="readonly")
            self.combobox.bind("<<ComboboxSelected>>", self.selected)
            self.combobox.grid(row=6, column=0, sticky=W, padx=10, pady=0)

    def update_figur_map_and_setting(self):
        """Функция для обновления кол-ва команд-фигур после нажатия кнопки обновить.
        Обновляется кол-во фигур, цвет и название команд сначала всё удаляется,
        а потом заново заполняется в окне настроек и на карте через функции"""

        for i in range(self.count_team):
            try:
                self.list_from_del = self.poly_dict[i]

            except:
                self.count_team = 3
                self.update_figur_map()
                self.update_figur_map_and_setting()

            self.canvas_map.delete(self.list_from_del[0])
            self.canvas_map.delete(self.list_from_del[1])
            self.list_from_del[2].destroy()
            self.canvas_map.delete(self.list_from_del[3])
            self.canvas_map.delete(self.list_from_del[4])

            self.list_from_del_set = self.poly_dict_set[i]
            [self.canvas_fig.delete(self.list_from_del_set[ind]) for ind in range(len(self.list_from_del_set))]
            # вместо однострочного когда выше можно использовать поэлементное удаление
            # self.canvas_fig.delete(self.list_from_del_set[0])
            # self.canvas_fig.delete(self.list_from_del_set[1])
            # self.canvas_fig.delete(self.list_from_del_set[2])
            # self.canvas_fig.delete(self.list_from_del_set[3])
        self.poly_dict_set.clear()
        self.poly_dict.clear()

        try:
            self.count_team = int(self.box_count_team.get())

        except:
            self.count_team = 3

        self.update_figur_map()
        self.update_figur_setting()

    def selected(self, event):
        """Функция для списка-бокса выбора номера команд в окне настроек.
        Устанавливает номер команды из выпадающего списка."""
        self.number_team = int(self.combobox.get()) - 1

    def select_color(self, key_dict):
        """Функция для изменения цвета фигуры выбранной команды в окне настроек и на игровой карте,
        причём фигура остаётся там где и была. Также данный цвет заносится в словарь цветом для запоминания
        на момент работы игры. При новом пуске словарь будет со значения по умолчанию"""
        try:
            result = colorchooser.askcolor(initialcolor="white")
            self.color_team[self.number_team] = result[1]
            self.canvas_fig.itemconfig(self.poly_dict_set[key_dict][2], fill=result[1])
            self.poly_dict[key_dict][2].config(bg=result[1])
        except (IndexError, KeyError):
            messagebox.showwarning("Предупреждение", "Выберете номер команды")

    def select_name_team(self, key_dict):
        """Функция для изменения названия выбранной команды в окне настроек.
        Название команды не должно превышать 26 символов!
        Названию берётся из поля, которое должно быть заполнено иначе название будет пустым.
        Также данное название заносится в словарь названий для запоминания
        на момент работы игры. При новом пуске словарь будет со значения по умолчанию"""
        new_name_team = self.entry_name_team.get()
        if len(new_name_team) > 24:
            new_name_team = f'{new_name_team[:24]}-\n{new_name_team[24:]}'
            if len(new_name_team) > 50:
                new_name_team = f'{new_name_team[:50]}-\n{new_name_team[50:]}'
        self.name_team[key_dict] = new_name_team
        self.canvas_fig.itemconfig(self.poly_dict_set[key_dict][1], text=new_name_team)
        self.canvas_map.itemconfig(self.poly_dict[key_dict][1], text=new_name_team)

    def open_win_setting_game(self):
        """Функция для создания окна настроек."""
        self.setting_win = Toplevel()
        self.setting_win.config(padx=20, pady=20, bg=BG_COLOR)  # Устанавливаем отступ от границ
        self.setting_win.wm_attributes('-topmost', 1)  # окно будет поверх других
        self.setting_win.title("Изменение цвета команд")
        self.setting_win.geometry(f'{self.width_win_setting}x{self.height_win_setting}')
        # self.setting_win.protocol('WM_DELETE_WINDOW',
        #                           self.close_win_setting)  # активирует окно уточнения на закрытие окна настроек

        # Лейбл Предупреждение!
        label_warning = Label(self.setting_win, text=TEXT_WARNING, justify=CENTER,
                              wraplength=self.width_win_setting * 0.95,
                              bg=BG_COLOR, fg=RED, font=FONT_WARNING_SET)
        label_warning.grid(row=0, column=0, sticky=W, padx=10, pady=10)

        # Лейбл кол-во команд
        label_count_team = Label(self.setting_win, text="Количество команд", bg=BG_COLOR, fg=YELLOW, font=FONT_NAME_SET)
        label_count_team.grid(row=1, column=0, sticky=W, padx=10, pady=10)

        # Список для выбора кол-ва команд
        self.box_count_team = ttk.Combobox(self.setting_win, values=COUNT_TEAM_LIST, state="readonly")
        self.box_count_team.grid(row=2, column=0, sticky=W, padx=10, pady=0)

        # Кнопка обновления холста с фигурами
        button_update = Button(self.setting_win, text='Обновить', command=self.update_figur_map_and_setting)
        button_update.configure(width=20, activebackground=YELLOW, relief=FLAT)
        button_update.grid(row=3, column=0, sticky=W, padx=10, pady=10)

        # Холст на котором будут фигуры и их нумерация №1-6 с названием
        self.canvas_fig = Canvas(self.setting_win, width=self.width_win_setting, height=self.height_canvas_setting,
                                 bg=BG_COLOR, borderwidth=0, highlightthickness=0)
        self.canvas_fig.grid(row=4, column=0, sticky=W, padx=10, pady=0, columnspan=2)

        # Лейбл выбора команды для изменения цвета
        label_team = Label(self.setting_win, text="Выберите номер команды для изменения цвета", bg=BG_COLOR, fg=YELLOW,
                           font=FONT_NAME_SET)
        label_team.grid(row=5, column=0, sticky=W, padx=10, pady=10)

        # Кнопка изменения цвета выбранной команды
        button_config_color = Button(self.setting_win, text="Изменить цвет",
                                     command=lambda: self.select_color(self.number_team))
        button_config_color.configure(width=20, activebackground=YELLOW, relief=FLAT)
        button_config_color.grid(row=7, column=0, sticky=W, padx=10, pady=10)

        # Лейбл ввода нового названия команды
        label_name_team = Label(self.setting_win, text="Новое название команды", bg=BG_COLOR, fg=YELLOW,
                                font=FONT_TEXT_SET)
        label_name_team.grid(row=8, column=0, sticky=NW, padx=10, pady=0)

        # Полоса ввода имени команды
        self.entry_name_team = Entry(self.setting_win, width=30)  # Окно ввода названия команды
        self.entry_name_team.grid(row=8, column=0, sticky=N, padx=0, pady=5)
        self.entry_name_team.focus()

        # Кнопка изменения названия выбранной команды
        button_config_name_team = Button(self.setting_win, text="Изменить название команды",
                                         command=lambda: self.select_name_team(self.number_team))
        button_config_name_team.configure(width=30, activebackground=YELLOW, relief=FLAT)
        button_config_name_team.grid(row=9, column=0, sticky=W, padx=10, pady=10)

        self.update_figur_setting()
        self.setting_win.mainloop()

    # def open_win_rules_game(self):
    #     """Функция для создания окна с правилами игры."""
    #     self.rules_win = Toplevel()
    #     self.width_window_rules = self.width_window_game
    #     self.height_window_rules = self.height_window_game
    #     self.rules_win.config(padx=0, pady=0, bg=BG_COLOR)  # Устанавливаем отступ от границ
    #     self.rules_win.wm_attributes('-topmost', 1)  # окно будет поверх других
    #     self.rules_win.title("Правила игры")
    #     self.rules_win.geometry(f'{self.width_window_rules}x{self.height_window_rules}')
    #     # self.rules_win.protocol('WM_DELETE_WINDOW',
    #     #                           self.close_win_rules)  # активирует окно уточнения на закрытие окна настроек
    #
    #     # СОЗДАЁМ ПОЛОСЫ ПРОКРУТКИ
    #     self.rules_frame = Frame(self.rules_win)
    #     self.rules_frame.pack(fill=BOTH, expand=1)
    #
    #     # 2 Создаём рамку для X полосы прокрутки
    #     self.sector = Frame(self.rules_frame)
    #     self.sector.pack(fill=X, side=BOTTOM)
    #
    #     # 3 Создаём Холст
    #     self.rules_canvas = Canvas(self.rules_frame, bg=BG_COLOR)
    #     self.rules_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #
    #     # 4 Добавляем полосу прокрутки на холст
    #     self.x_scrollbar_rules = ttk.Scrollbar(self.sector, orient=HORIZONTAL, command=self.rules_canvas.xview)
    #     self.x_scrollbar_rules.pack(side=BOTTOM, fill=X)
    #     self.y_scrollbar_rules = ttk.Scrollbar(self.rules_frame, orient=VERTICAL, command=self.rules_canvas.yview)
    #     self.y_scrollbar_rules.pack(side=RIGHT, fill=Y)
    #
    #     # 5 Настройка холста
    #     self.rules_canvas.configure(xscrollcommand=self.x_scrollbar_rules.set)
    #     self.rules_canvas.configure(yscrollcommand=self.y_scrollbar_rules.set)
    #     self.rules_canvas.bind("<Configure>",
    #                            lambda e: self.rules_canvas.config(scrollregion=self.rules_canvas.bbox(ALL)))
    #
    #     # 6 Создаём еще одну рамку ВНУТРИ холста
    #     self.second_frame_rules = Frame(self.rules_canvas, bg=BG_COLOR)
    #
    #     # 7 Добавляем эту Новую Рамку в окно на Холсте
    #     self.rules_canvas.create_window((0, 0), window=self.second_frame_rules, anchor="nw")
    #
    #     # Размещаем текст правил
    #
    #     label_name_rules = Label(self.second_frame_rules, text="Правила игры", bg=BG_COLOR, fg=WHITE,
    #                              font=FONT_NAME_SET)
    #     label_name_rules.grid(row=0, column=0, sticky=W, padx=10, pady=10)
    #
    #     with open(path_file_rules, 'r', encoding='utf-8') as file_txt:
    #         text_rules = file_txt.read()
    #     label_name_rules = Label(self.second_frame_rules, text=text_rules, bg=BG_COLOR, fg=WHITE, font=FONT_TEXT_RULES,
    #                              justify=LEFT, wraplength=self.width_window_rules * 0.95)
    #     label_name_rules.grid(row=1, column=0, sticky=W, padx=10, pady=10)
    #
    #     self.rules_win.mainloop()
