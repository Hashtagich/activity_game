from math import floor
from random import choice, randint
from tkinter import colorchooser, messagebox

from all_setting_game import *
from common_func import *


# from screeninfo import get_monitors
# monitor_parameters = get_monitors()[0]
# width_monitor = monitor_parameters.width
# height_monitor = monitor_parameters.height


# pyinstaller activity.py --onefile --noconsole --icon=logo.ico -n Activity
# Рабочая команда для преобразования кода в формат exe:
# 1) --onefile делает один файл
# 2) --noconsole консоль не выводится при запуске
# 3) --icon=название ico файла взять иконку чтобы она стала ярлыком игры
# 4) -n и вводим название игры какое хотим, по дефолту будет название файла

class StartMenu:
    def __init__(self, start_menu_width=width_monitor, start_menu_height=height_monitor):
        # Параметры окна
        self.start_width = start_menu_width
        self.start_height = start_menu_height

        self.font_k = self.start_width / 1980

        # Шрифты кнопок
        self.PARAMETERS_FONT_NAME_GAME_MENU = (STILE_FONT, int(52 * self.font_k), 'bold')
        self.PARAMETERS_FONT_BUTTON_MENU = (STILE_FONT, int(40 * self.font_k))

        # Шрифты правил игры
        # self.FONT_TEXT_RULES = (STILE_FONT, int(16 * WIDTH_WINDOW_GAME / 1980))
        # self.FONT_NAME_SET = (STILE_FONT, int(20 * WIDTH_WINDOW_GAME / 1980), 'bold')

        self.indent_button = self.PARAMETERS_FONT_BUTTON_MENU[1] // 2

        # Основные переменные и коэффициенты

        # self.color_team = COLOR_TEAM
        # self.count_team = 5

        # Окно меню
        self.window = Tk()
        self.window.title(NAME_GAME)

        self.window.geometry(f'{self.start_width}x{self.start_height}')  # параметры окна меню
        self.window.config(padx=20, pady=20, bg=BG_COLOR)
        self.window.protocol('WM_DELETE_WINDOW', self.close_win_menu)

        self.window.columnconfigure(1, weight=2)  # команда для установки кнопок по центру

        # Название игры
        self.logo_game = Label(text=NAME_GAME, font=self.PARAMETERS_FONT_NAME_GAME_MENU, bg=BG_COLOR, fg=YELLOW)
        self.logo_game.grid(row=0, column=1, pady=self.PARAMETERS_FONT_BUTTON_MENU[1])

        # Кнопки меню
        self.start_game = Button(text='Начать игру', font=self.PARAMETERS_FONT_BUTTON_MENU, highlightthickness=0,
                                 command=self.push_start_game, width=12, activebackground=YELLOW,
                                 relief=RAISED)  # bg=BG_COLOR

        self.setting_game = Button(text='Настройки', font=self.PARAMETERS_FONT_BUTTON_MENU, highlightthickness=0,
                                   command=self.push_setting_game, width=12, activebackground=YELLOW,
                                   relief=RAISED)  # bg=BG_COLOR

        self.rules_game = Button(text='Правила', font=self.PARAMETERS_FONT_BUTTON_MENU, highlightthickness=0, width=12,
                                 activebackground=YELLOW, relief=RAISED,
                                 command=lambda: open_win_rules_or_task(self.window,
                                                                        width_window_rules=WIDTH_WINDOW_GAME,
                                                                        height_window_rules=HEIGHT_WINDOW_GAME,
                                                                        name_list="Правила игры",
                                                                        name_file_txt=path_file_control))

        self.control_game = Button(text='Управление', font=self.PARAMETERS_FONT_BUTTON_MENU, highlightthickness=0,
                                   width=12, activebackground=YELLOW, relief=RAISED,
                                   command=lambda: open_win_rules_or_task(self.window,
                                                                          width_window_rules=WIDTH_WINDOW_GAME,
                                                                          height_window_rules=HEIGHT_WINDOW_GAME,
                                                                          name_list="Управление игры",
                                                                          name_file_txt=path_file_control))  # bg=BG_COLOR

        self.about = Button(text='Об игре', font=self.PARAMETERS_FONT_BUTTON_MENU, highlightthickness=0,
                            width=12, activebackground=YELLOW, relief=RAISED,
                            command=lambda: open_win_rules_or_task(self.window, width_window_rules=WIDTH_WINDOW_GAME,
                                                                   height_window_rules=HEIGHT_WINDOW_GAME,
                                                                   name_list="Об игре", name_file_txt=path_file_about))  # bg=BG_COLOR

        self.exit_game = Button(text='Выход', font=self.PARAMETERS_FONT_BUTTON_MENU, highlightthickness=0, width=12,
                                command=self.close_win_menu, activebackground=YELLOW, relief=RAISED)  # bg=BG_COLOR

        # self.test_prog = Button(text='Test', font=self.PARAMETERS_FONT_BUTTON_MENU, highlightthickness=0, width=12,
        #                         command=self.test_prog, activebackground=YELLOW, relief=RAISED)  # bg=BG_COLOR
        # self.test_prog.grid(row=7, column=1, pady=self.indent_button)

        self.start_game.grid(row=1, column=1, pady=self.indent_button)
        self.setting_game.grid(row=2, column=1, pady=self.indent_button)
        self.rules_game.grid(row=3, column=1, pady=self.indent_button)
        self.control_game.grid(row=4, column=1, pady=self.indent_button)
        self.about.grid(row=5, column=1, pady=self.indent_button)
        self.exit_game.grid(row=6, column=1, pady=self.indent_button)

        self.window.mainloop()

    def test_prog(self):
        """Временная функция для тестирования того, что глобальные переменные обновились."""
        print('Разрешение экрана')
        print(WIDTH_WINDOW_GAME, HEIGHT_WINDOW_GAME)
        print(type(WIDTH_WINDOW_GAME), type(HEIGHT_WINDOW_GAME))
        print('\nКол-во команд, первый отбор')
        print(count_team, type(count_team))
        print('\nСписок цветов')
        print(COLOR_TEAM)
        print('\nСписок имен команд')
        print(NAME_TEAM)
        print('\nСловарь команды для окна настроек')
        print(poly_dict_set)
        print('\nСписок цветов цифр команд в меню настроек')
        print(NUMBER_COLOR)
        print('\nСписок названия команд')
        print(NAME_TEAM)
        print('\nКарта стандартная?')
        print(STANDARD_CARD)
        print('\nВремя раунда')
        print(TIME_ROUND)

    def close_win_menu(self):
        """Функция запускает уточняющее окно при закрытии окна игры"""
        if messagebox.askokcancel('Выход из игры', 'Хотите выйти из игры?'):
            self.window.destroy()

    def push_start_game(self):
        game = GameWindow(self.window, game_width_window_game=WIDTH_WINDOW_GAME,
                          game_height_window_game=HEIGHT_WINDOW_GAME)

    def push_setting_game(self):
        setting_win = SettingMenu(self.window, setting_width_window_game=WIDTH_WINDOW_GAME,
                                  setting_height_window_game=HEIGHT_WINDOW_GAME)


class SettingMenu:
    def __init__(self, master, setting_width_window_game=800, setting_height_window_game=600):

        # Параметры окна
        self.setting_width = setting_width_window_game
        self.setting_height = setting_height_window_game

        # Параметры холста где отображаются игровые фигурки для предварительного просмотра
        self.width_win_setting = int(self.setting_width * 0.9)
        self.height_canvas_setting = int(self.setting_height / 6)

        # Основные переменные и коэффициенты
        self.font_k = self.setting_width / 1980
        self.count_team = count_team

        self.x1_rectangle = x1_rectangle
        self.step_x1_rectangle = int(self.width_win_setting / 6 / 1.1)
        self.step_x1_create_rectangle = int(self.width_win_setting / 6 / 6.6)
        self.y2_rectangle = int(self.height_canvas_setting / 1.6)

        # Шрифты текста
        self.FONT_NAME_SET = (STILE_FONT, int(24 * self.font_k), 'bold')
        self.FONT_TEXT_TEAM_SET = (STILE_FONT, int(20 * self.font_k), 'bold')
        self.FONT_NUM_TEAM_SET = (STILE_FONT, int(24 * self.font_k), 'bold')
        self.FONT_NAME_TEAM_SET = (STILE_FONT, int(14 * self.font_k))  # , 'italic'

        # Шрифты кнопок
        self.FONT_BUTTON_SETTING = (STILE_FONT, int(16 * self.font_k))
        self.indent_y = self.FONT_BUTTON_SETTING[1] // 2

        # Создаём окно
        self.window_setting = Toplevel(master)
        self.window_setting.title('Настройки')

        self.window_setting.geometry(f'{self.setting_width}x{self.setting_height}')  # параметры окна игры
        self.window_setting.config(padx=20, pady=20, bg=BG_COLOR)

        self.label_screen_resolution = Label(self.window_setting, text="Разрешение экрана", bg=BG_COLOR, fg=YELLOW,
                                             font=self.FONT_NAME_SET)

        self.box_screen_resolution = ttk.Combobox(self.window_setting, values=TUPLE_SCREEN_SETTINGS, state="readonly",
                                                  font=self.FONT_BUTTON_SETTING)

        self.label_count_team = Label(self.window_setting, text="Количество команд", bg=BG_COLOR, fg=YELLOW,
                                      font=self.FONT_NAME_SET)

        self.box_count_team = ttk.Combobox(self.window_setting, values=TUPLE_EL, state="readonly",
                                           font=self.FONT_BUTTON_SETTING)

        self.label_choice_map = Label(self.window_setting, text="Выбор карты", bg=BG_COLOR, fg=YELLOW,
                                      font=self.FONT_NAME_SET)
        self.box_choice_map = ttk.Combobox(self.window_setting, values=TUPLE_MAP, state="readonly",
                                           font=self.FONT_BUTTON_SETTING)

        self.label_time_round = Label(self.window_setting, text="Время на раунд (мин.)", bg=BG_COLOR, fg=YELLOW,
                                      font=self.FONT_NAME_SET)
        self.box_time_round = ttk.Combobox(self.window_setting, values=TUPLE_TIME, state="readonly",
                                           font=self.FONT_BUTTON_SETTING)

        self.canvas_fig = Canvas(self.window_setting, width=self.width_win_setting, height=self.height_canvas_setting,
                                 bg=BG_COLOR, borderwidth=0, highlightthickness=0)

        self.label_team = Label(self.window_setting, text="Выберите номер команды для изменения цвета", bg=BG_COLOR,
                                fg=YELLOW, font=self.FONT_NAME_SET)

        self.box_number_team = ttk.Combobox(self.window_setting, values=tuple(map(str, range(1, count_team + 1))),
                                            state="readonly", font=self.FONT_BUTTON_SETTING)

        self.button_config_color = Button(self.window_setting, text="Изменить цвет", activebackground=YELLOW,
                                          relief=FLAT, command=self.select_color, font=self.FONT_BUTTON_SETTING)

        self.label_name_team = Label(self.window_setting, text="Новое название команды", bg=BG_COLOR, fg=YELLOW,
                                     font=self.FONT_NAME_SET)

        self.entry_name_team = Entry(self.window_setting, font=self.FONT_BUTTON_SETTING)  # Окно ввода названия команды
        self.entry_name_team.focus()

        self.button_config_name_team = Button(self.window_setting, text="Изменить название команды",
                                              command=self.select_name_team, font=self.FONT_BUTTON_SETTING,
                                              activebackground=YELLOW, relief=FLAT)

        self.label_screen_resolution.grid(row=1, column=0, sticky=W, padx=0, pady=self.indent_y)
        self.box_screen_resolution.grid(row=1, column=1, sticky=W, padx=0, pady=self.indent_y)

        self.label_count_team.grid(row=2, column=0, sticky=W, padx=0, pady=self.indent_y)
        self.box_count_team.grid(row=2, column=1, sticky=W, padx=0, pady=self.indent_y)

        self.label_choice_map.grid(row=3, column=0, sticky=W, padx=0, pady=self.indent_y)
        self.box_choice_map.grid(row=3, column=1, sticky=W, padx=0, pady=self.indent_y)

        self.label_time_round.grid(row=4, column=0, sticky=W, padx=0, pady=self.indent_y)
        self.box_time_round.grid(row=4, column=1, sticky=W, padx=0, pady=self.indent_y)

        self.canvas_fig.grid(row=5, column=0, sticky=W, padx=0, pady=self.FONT_BUTTON_SETTING[1] * 2, columnspan=2)
        self.label_team.grid(row=6, column=0, sticky=W, padx=0, pady=0)
        self.box_number_team.grid(row=7, column=0, sticky=W, padx=0, pady=0)
        self.button_config_color.grid(row=8, column=0, sticky=W, padx=0, pady=self.indent_y)
        self.label_name_team.grid(row=9, column=0, sticky=W, padx=0, pady=self.indent_y)
        self.entry_name_team.grid(row=10, column=0, sticky=W, padx=0, pady=0)
        self.button_config_name_team.grid(row=11, column=0, sticky=W, padx=0, pady=self.indent_y)

        self.create_figur_setting()

        self.box_screen_resolution.bind("<<ComboboxSelected>>", self.selected_screen_resolution)
        self.box_count_team.bind("<<ComboboxSelected>>", self.selected_count_team)
        self.box_number_team.bind("<<ComboboxSelected>>", self.selected_number_team)
        self.box_choice_map.bind("<<ComboboxSelected>>", self.selected_map)
        self.box_time_round.bind("<<ComboboxSelected>>", self.selected_minute)

        self.window_setting.grab_set()
        self.window_setting.focus_set()
        self.window_setting.wait_window()

    def selected_screen_resolution(self, event):
        """Функция берёт значение из списка разрешения экрана и преобразует его в две переменные
        (ширину и высоту экрана) тип int для дальнейшего применения в игровой карте"""
        global WIDTH_WINDOW_GAME, HEIGHT_WINDOW_GAME
        WIDTH_WINDOW_GAME, HEIGHT_WINDOW_GAME = map(int, self.box_screen_resolution.get().split('x'))

    def selected_count_team(self, event):
        """Функция задаёт кол-во команд в игре, также создаётся новый список-бокс для выбора конкретной команды
        для дальнейшего изменения названия или цвета команды"""
        global count_team
        try:
            count_team = int(self.box_count_team.get())
        except ValueError:
            count_team = self.count_team
        finally:
            self.box_number_team = ttk.Combobox(self.window_setting, values=tuple(map(str, range(1, count_team + 1))),
                                                state="readonly", font=self.FONT_BUTTON_SETTING)
            self.box_number_team.bind("<<ComboboxSelected>>", self.selected_number_team)
            self.box_number_team.grid(row=7, column=0, sticky=W, padx=0, pady=0)
            self.clear_figur_setting()
            self.create_figur_setting()

    def selected_number_team(self, event):
        """Функция задаёт номер конкретной команды для изменения цвета или названия. Номер команды уменьшается на 1 т.к.
        данный номер это индекс для изменения значений в списках цветов и названий команд.
        В случаи ошибки 'нет атрибута' стандартное значение 0."""
        try:
            self.num_team = int(self.box_number_team.get()) - 1
        except AttributeError:
            self.num_team = 0

    def selected_map(self, event):
        """Функция берёт значение из списка выбора карты и задаёт глобальной переменной STANDARD_CARD bool значение"""
        global STANDARD_CARD
        try:
            STANDARD_CARD = True if self.box_choice_map.get() == TUPLE_MAP[0] else False
        except AttributeError:
            STANDARD_CARD = False

    def selected_minute(self, event):
        """Функция берёт значение из списка выбора карты и задаёт глобальной переменной STANDARD_CARD bool значение"""
        global TIME_ROUND
        try:
            TIME_ROUND = int(float(self.box_time_round.get()) * 60)
        except AttributeError:
            TIME_ROUND = 60

    def select_color(self):
        """Функция для изменения цвета фигуры выбранной команды в окне настроек и на игровой карте.
        Цифра внутри фигуры меняется на белый если цвет слишком темный.
        Также данный цвет (фигуры и цифры) заносится в словари для запоминания на момент работы игры.
        При новом пуске словари будет со значения по умолчанию"""
        # global COLOR_TEAM, poly_dict_set  # poly_dict
        try:
            result = colorchooser.askcolor(initialcolor="white", parent=self.window_setting)
            COLOR_TEAM[self.num_team] = result[1]
            self.canvas_fig.itemconfig(poly_dict_set[self.num_team][2], fill=result[1])
            if result[0][0] in range(100) and result[0][1] in range(100) and result[0][2] in range(100):
                self.canvas_fig.itemconfig(poly_dict_set[self.num_team][3], fill=WHITE)
                NUMBER_COLOR[self.num_team] = WHITE
            else:
                self.canvas_fig.itemconfig(poly_dict_set[self.num_team][3], fill=BLACK)
                NUMBER_COLOR[self.num_team] = BLACK
        except AttributeError:
            messagebox.showwarning("Предупреждение", "Выберете номер команды", parent=self.window_setting)

    def select_name_team(self, num=NUM_INDENT):
        """Функция осуществляет перенос слов названия команды и добавляет пробел если название было слишком длинное.
        Новое название команды заносится в словарь для дальнейшего использования на время работы программы."""
        new_name_team = self.entry_name_team.get()
        number_enter = num
        while len(new_name_team) > number_enter:

            while new_name_team[:number_enter].count(' ') == 0:  # цикл на случай если в слове вообще не будет пробелов
                new_name_team = f'{new_name_team[number_enter:]} {new_name_team[:number_enter + 1]}'

            ind_end_space = new_name_team[:number_enter].rfind(' ')
            new_name_team = f'{new_name_team[:ind_end_space]}\n{new_name_team[ind_end_space + 1:]}'
            number_enter += num

        NAME_TEAM[self.num_team] = new_name_team
        self.canvas_fig.itemconfig(poly_dict_set[self.num_team][1], text=new_name_team)

    def create_figur_setting(self):
        """Функция создаёт игровые фигурки, их название и обозначение в меню настроек.
        Данные о цвете фигурки, названии команды и цвет цифры команды сохраняется в словари для дальнейшего
        использования в других разделах программы."""
        # global count_team
        try:
            count_team = int(self.box_count_team.get())
        except ValueError:
            count_team = self.count_team

        for i in range(count_team):
            self.text_team_set = self.canvas_fig.create_text(self.step_x1_rectangle * i, 0, text=f'Команда №{i + 1}',
                                                             fill=YELLOW, font=self.FONT_TEXT_TEAM_SET, anchor=NW)

            self.points_set = [
                self.step_x1_rectangle * i,
                self.FONT_TEXT_TEAM_SET[1] * 2,
                self.x1_rectangle + self.step_x1_create_rectangle * 2 + self.step_x1_rectangle * i,
                self.y2_rectangle,
            ]
            self.polygon_team_set = self.canvas_fig.create_rectangle(self.points_set, fill=COLOR_TEAM[i],
                                                                     outline='#000', width=1.5)
            self.num_team_fig = self.canvas_fig.create_text(
                (self.x1_rectangle + self.step_x1_rectangle * i) + self.FONT_NUM_TEAM_SET[1],
                (self.FONT_TEXT_TEAM_SET[1] * 2 + self.y2_rectangle) // 2, text=f'{i + 1}', fill=NUMBER_COLOR[i],
                anchor=W,
                font=self.FONT_NUM_TEAM_SET)

            self.name_team_set = self.canvas_fig.create_text(self.step_x1_rectangle * i,
                                                             self.y2_rectangle + self.FONT_NAME_TEAM_SET[1] // 2,
                                                             text=NAME_TEAM[i], fill=YELLOW, anchor=NW,
                                                             font=self.FONT_NAME_TEAM_SET)

            poly_dict_set[i] = [self.text_team_set, self.name_team_set, self.polygon_team_set, self.num_team_fig]

    def clear_figur_setting(self):
        """Функция очищает словарь от данных и зачищает его."""
        # global poly_dict_set
        for i in range(len(poly_dict_set.keys())):
            # try:
            self.list_from_del_set = poly_dict_set[i]
            [self.canvas_fig.delete(self.list_from_del_set[ind]) for ind in range(len(self.list_from_del_set))]
            # вместо однострочного когда выше можно использовать поэлементное удаление
            # self.canvas_fig.delete(self.list_from_del_set[0])
            # self.canvas_fig.delete(self.list_from_del_set[1])
            # self.canvas_fig.delete(self.list_from_del_set[2])
            # self.canvas_fig.delete(self.list_from_del_set[3])
        poly_dict_set.clear()


class GameWindow:
    def __init__(self, master, game_width_window_game=WIDTH_WINDOW_GAME, game_height_window_game=HEIGHT_WINDOW_GAME):
        number_field = 0
        self.dict_tasks = {}
        # Для окна игры
        self.window_game = Toplevel(master)
        self.window_game.title(NAME_GAME)
        self.width_window_game = game_width_window_game
        self.height_window_game = game_height_window_game
        self.window_game.geometry(f'{self.width_window_game}x{self.height_window_game}')  # параметры окна игры
        self.window_game.config(padx=0, pady=0, bg=BG_COLOR)  # Устанавливаем отступ от границ

        self.window_game.protocol('WM_DELETE_WINDOW', self.close_win_game)
        # self.window.wm_attributes('-transparentcolor',
        #                           COLOR_INVISIBLE)  # делает конкретный цвет прозрачным (будет видно экран пк)
        # self.window_game.wm_attributes('-topmost', 1)

        # Автоматическое изменение шрифтов исходя из ширины экрана
        font_k = self.width_window_game / 1980
        self.FONT_NAME = (STILE_FONT, int(32 * font_k), 'bold')
        self.FONT_TEAM = (STILE_FONT, int(24 * font_k), 'bold')
        self.FONT_NAME_TEAM = (STILE_FONT, int(16 * font_k), 'italic')
        self.FONT_NAME_SET = (STILE_FONT, int(20 * font_k), 'bold')
        self.FONT_WARNING_SET = (STILE_FONT, int(20 * font_k), 'bold')
        self.FONT_TEXT_SET = (STILE_FONT, int(16 * font_k), 'bold')
        self.FONT_TEXT_TEAM_SET = (STILE_FONT, int(12 * font_k), 'bold')
        self.FONT_NUM_TEAM_SET = (STILE_FONT, int(24 * font_k), 'bold')
        self.FONT_NAME_TEAM_SET = (STILE_FONT, int(10 * font_k), 'italic')
        self.PARAMETERS_FONT_LABEL = (STILE_FONT, int(32 * font_k), 'bold')
        self.PARAMETERS_FONT_LABEL_LINE_CARD = (STILE_FONT, int(18 * font_k), 'bold')
        self.PARAMETERS_FONT_BUTTON = (STILE_FONT, int(14 * font_k), 'bold')
        self.PARAMETERS_FONT_BUTTON_CARD = (STILE_FONT, int(70 * font_k), 'bold')
        self.FONT_TEXT_NUMBER = (STILE_FONT, int(14 * font_k), 'bold')
        self.FONT_TEXT_RULES = (STILE_FONT, int(16 * font_k))
        self.num = NUM_INDENT  # индекс на котором осуществляется перенос слов в задании и название команды
        self.width_but_timer = 24 if self.height_window_game in (664, 864) else 26

        self.window_game.grab_set()
        self.window_game.focus_set()
        # self.window_game.wait_window()

        # Для холста карты
        self.width_field = int(self.width_window_game / 1.37)
        self.height_field = int(self.height_window_game / 1.08)
        self.step_x, self.step_y = int(self.width_field / 7), int(self.height_field / 15)
        self.x1, self.y1 = x1, y_1
        self.x2, self.y2 = self.x1 + self.step_x, self.y1 + self.step_y
        self.line_indent = int(self.step_y / 3)
        self.number_line = NUMBER_LINE
        self.step_zero = step_zero
        self.game_map = {}

        # Для холста карточек
        self.width_field_card = int(self.width_window_game / 4)
        self.height_field_card = int(self.height_window_game / 1.08)
        self.size_rectangle_card = int(self.width_field_card / 5.3)
        self.y_line_card = int(self.height_field_card / 3)
        self.y_line_card_step = self.size_rectangle_card + 10
        self.label_list = []

        self.step_x1_create_rectangle = int(self.width_window_game / (1.6 * 6 * 6.6))

        # Для команд РАЗОБРАТЬСЯ
        self.indent_line_team = INDENT_LINE_TEAM
        self.count_team = count_team
        self.poly_dict, self.poly_dict_set = {}, {}
        self.x_position_team = int(self.width_field * 0.77)

        # CОЗДАЁМ МЕНЮ НАСТРОЕК ВО ВРЕМЯ ИГРЫ
        self.main_menu = Menu(self.window_game)
        self.window_game.config(menu=self.main_menu)
        self.main_menu.add_command(label='Дополнительные настройки',
                                   command=self.push_set_command)  # , command=self.open_win_setting_game
        self.main_menu.add_command(label='Правила игры',
                                   command=lambda: open_win_rules_or_task(self.window_game,
                                                                          width_window_rules=self.width_window_game,
                                                                          height_window_rules=self.height_window_game,
                                                                          name_file_txt=path_file_rules))
        self.main_menu.add_command(label='Управление',
                                   command=lambda: open_win_rules_or_task(self.window_game,
                                                                          width_window_rules=self.width_window_game,
                                                                          height_window_rules=self.height_window_game,
                                                                          name_list="Управление игры",
                                                                          name_file_txt=path_file_control))

        # CОЗДАЁМ ПОЛОСЫ ПРОКРУТКИ НА СЛУЧАЙ ЕСЛИ РАЗРЕШЕНИЕ ЭКРАНА БУДЕН НЕ fullHD
        # 1 Создаём основной фрейм
        self.main_frame = Frame(self.window_game)
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
        self.image_dialogue = PhotoImage(file=dict_path_image[f'{self.width_window_game}x{self.height_window_game}'][0])
        self.image_gestures = PhotoImage(file=dict_path_image[f'{self.width_window_game}x{self.height_window_game}'][1])
        self.image_painting = PhotoImage(file=dict_path_image[f'{self.width_window_game}x{self.height_window_game}'][2])

        # Словарь для создания карты (значки действий и цвет поля)
        self.DICT_ACTIONS = {
            'PINK': (self.image_gestures, PINK),
            'ORANGE': (self.image_gestures, ORANGE),
            'BLUE': (self.image_dialogue, BLUE),
            'DARK_BLUE': (self.image_dialogue, DARK_BLUE),
            'GREEN': (self.image_painting, GREEN),
            'YELLOW': (self.image_painting, YELLOW),
        }
        if STANDARD_CARD:
            # Словарь для создания стандартной карты (значки действий и цвет поля).
            field_1 = (BLUE, self.image_dialogue)
            field_2 = (YELLOW, self.image_painting)
            field_3 = (PINK, self.image_gestures)
            field_4 = (ORANGE, self.image_gestures)
            field_5 = (DARK_BLUE, self.image_dialogue)
            field_6 = (GREEN, self.image_painting)

            self.game_map = {
                1: field_1, 2: field_2, 3: field_3, 4: field_1, 5: field_1, 6: field_4, 7: field_5, 8: field_6,
                9: field_3, 10: field_1, 11: field_6, 12: field_5, 13: field_2, 14: field_3, 15: field_4, 16: field_2,
                17: field_1, 18: field_3, 19: field_4, 20: field_3, 21: field_6, 22: field_2, 23: field_6, 24: field_4,
                25: field_6, 26: field_5, 27: field_3, 28: field_1, 29: field_4, 30: field_5, 31: field_2, 32: field_6,
                33: field_2, 34: field_4, 35: field_4, 36: field_1, 37: field_3, 38: field_6, 39: field_2, 40: field_3,
                41: field_6, 42: field_5, 43: field_5, 44: field_4, 45: field_1, 46: field_2, 47: field_3, 48: field_4,
            }

        else:
            # Словарь для случайной карты на основе данных из self.DICT_ACTIONS.
            for ind in range(FINISH - 1):
                self.key_DICT_ACTIONS = choice(tuple(self.DICT_ACTIONS.keys()))
                action, color = self.DICT_ACTIONS[self.key_DICT_ACTIONS][0], self.DICT_ACTIONS[self.key_DICT_ACTIONS][1]
                self.game_map[ind + 1] = (color, action)

        # СОЗДАЁМ ЛОГОТИП ИГРЫ И РАЗМЕЩАЕМЕГО
        self.label_info = Label(self.second_frame, text=NAME_GAME, font=self.PARAMETERS_FONT_LABEL, bg=BG_COLOR,
                                fg=YELLOW,
                                highlightthickness=0)
        self.label_info.grid(row=0, column=2, pady=0, padx=0, columnspan=3)

        # СОЗДАЁМ ХОЛСТ ДЛЯ КАРТЫ
        # Игровая карта
        self.canvas_map = Canvas(self.second_frame, width=self.width_field, height=self.height_field, bg=BG_COLOR,
                                 highlightthickness=thickness)
        # сделать thickness=0 в окне all_setting_game, если рамка не нужна

        self.canvas_map.grid(row=1, column=2, pady=0, padx=0)

        # Поле старта
        self.canvas_map.create_text(self.width_field - int(self.width_field / 8), self.step_y / 2, text='Старт',
                                    fill=YELLOW, font=self.FONT_NAME)

        # Цикл для создания игровых клеток(игровой карты)
        for num, color in self.game_map.items():
            number_field += 1
            num -= 1
            while num >= COUNT_CAGE_IN_LINE:
                num %= COUNT_CAGE_IN_LINE

            if self.number_line % 2 == 0:
                self.canvas_map.create_rectangle(self.x1 + self.step_x * num, self.y1, self.x2 + self.step_x * num,
                                                 self.y2, fill=color[0], outline=BLACK, width=WIDTH_RECTANGLE_LINE)
                self.canvas_map.create_image(self.x1 + self.step_x * num + (self.step_x / 5), self.y1 + self.step_y / 2,
                                             image=color[1])
                self.canvas_map.create_text(self.x1 + self.step_x * num + (self.step_x * 0.9),
                                            self.y1 + self.step_y - (self.step_y / 4),
                                            text=f'{number_field}', fill=BLACK, font=self.FONT_TEXT_NUMBER)

            else:
                abs_coefficient = abs(num - COUNT_CAGE_IN_LINE_1)
                self.canvas_map.create_rectangle(self.x1 + self.step_x * abs_coefficient, self.y1,
                                                 self.x2 + self.step_x * abs_coefficient, self.y2,
                                                 fill=color[0], outline=BLACK, width=WIDTH_RECTANGLE_LINE)
                self.canvas_map.create_image(self.x1 + self.step_x * abs_coefficient + (self.step_x / 5),
                                             self.y1 + self.step_y / 2, image=color[1])
                self.canvas_map.create_text(self.x1 + self.step_x * abs_coefficient + (self.step_x * 0.9),
                                            self.y1 + self.step_y * 0.75, text=f'{number_field}', fill=BLACK,
                                            font=self.FONT_TEXT_NUMBER)

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
                                    self.y1 + self.step_y / 2, text='ФИНИШ', fill=WHITE, font=self.FONT_NAME)

        # Таймер
        self.canvas_map.create_text(self.width_field - int(self.width_field / 8),
                                    self.height_field - self.step_y * 4.75,
                                    text='Таймер',
                                    fill=YELLOW,
                                    font=self.FONT_NAME)
        self.timer_text = self.canvas_map.create_text(self.width_field - int(self.width_field / 8),
                                                      self.height_field - self.step_y * 4,
                                                      text='00:00', fill=WHITE, font=self.FONT_NAME)

        # Кнопки таймера
        self.button_start = Button(self.canvas_map, text='Старт', font=self.PARAMETERS_FONT_BUTTON,
                                   command=self.push_start, width=self.width_but_timer,
                                   activebackground=YELLOW, relief=FLAT, highlightthickness=0)
        self.button_start_win = self.canvas_map.create_window(self.width_field - self.step_x * 1.5,
                                                              self.height_field - self.step_y * 3.25,
                                                              anchor=NW, window=self.button_start)

        self.button_pause = Button(self.canvas_map, text='Пауза', font=self.PARAMETERS_FONT_BUTTON,
                                   command=self.push_stop, width=self.width_but_timer,
                                   activebackground=YELLOW, relief=FLAT, highlightthickness=0)
        self.button_pause_win = self.canvas_map.create_window(self.width_field - self.step_x * 1.5,
                                                              self.height_field - self.step_y * 2.5,
                                                              anchor=NW, window=self.button_pause)

        self.button_res = Button(self.canvas_map, text='Продолжить', font=self.PARAMETERS_FONT_BUTTON,
                                 command=self.resume, width=self.width_but_timer, activebackground=YELLOW,
                                 relief=FLAT, highlightthickness=0)
        self.button_res_win = self.canvas_map.create_window(self.width_field - self.step_x * 1.5,
                                                            self.height_field - self.step_y * 1.75,
                                                            anchor=NW, window=self.button_res)

        # СОЗДАЁМ ХОЛСТ ДЛЯ КАРТОЧЕК
        self.canvas_cards = Canvas(self.second_frame, width=self.width_field_card, height=self.height_field_card,
                                   bg=BG_COLOR,
                                   highlightthickness=thickness)
        # сделать thickness=0 в окне all_setting_game, если рамка не нужна

        self.canvas_cards.create_text(int(self.width_field_card / 2), self.step_y / 2, text='Карточки', fill=YELLOW,
                                      font=self.FONT_NAME)

        button_card_3 = Button(self.canvas_cards, command=self.push_card_3, highlightthickness=0, bd=0, text='3',
                               bg=GREEN, fg=YELLOW, activebackground=YELLOW, relief=FLAT,
                               font=self.PARAMETERS_FONT_BUTTON_CARD)
        button_card_3_win = self.canvas_cards.create_window(10 + int(self.width_field_card / 3 * 0),
                                                            self.step_y / 2 * 2,
                                                            anchor=NW, window=button_card_3)

        button_card_4 = Button(self.canvas_cards, command=self.push_card_4, highlightthickness=0, bd=0, text='4',
                               bg=GREEN, fg=YELLOW, activebackground=YELLOW, relief=FLAT,
                               font=self.PARAMETERS_FONT_BUTTON_CARD)
        button_card_4_win = self.canvas_cards.create_window(10 + int(self.width_field_card / 3 * 1),
                                                            self.step_y / 2 * 2,
                                                            anchor=NW, window=button_card_4)

        button_card_5 = Button(self.canvas_cards, command=self.push_card_5, highlightthickness=0, bd=0, text='5',
                               bg=GREEN, fg=YELLOW, activebackground=YELLOW, relief=FLAT,
                               font=self.PARAMETERS_FONT_BUTTON_CARD)
        button_card_5_win = self.canvas_cards.create_window(10 + int(self.width_field_card / 3 * 2),
                                                            self.step_y / 2 * 2,
                                                            anchor=NW, window=button_card_5)

        self.number_card_info = self.canvas_cards.create_text(int(self.width_field_card / 2),
                                                              self.y_line_card - self.FONT_NAME[1],
                                                              text='Карточка №', fill=YELLOW, font=self.FONT_NAME)

        for num_line_card in range(6):
            key = TUPLE_COLOR[num_line_card]
            self.canvas_cards.create_rectangle(10, self.y_line_card + self.y_line_card_step * num_line_card,
                                               10 + self.size_rectangle_card,
                                               self.y_line_card + self.y_line_card_step * num_line_card + self.size_rectangle_card,
                                               fill=self.DICT_ACTIONS[key][1], outline=BLACK,
                                               width=WIDTH_RECTANGLE_LINE)

            self.line_task = self.canvas_cards.create_rectangle(10 + self.size_rectangle_card,
                                                                self.y_line_card + self.y_line_card_step * num_line_card,
                                                                self.width_field_card - 10,
                                                                self.y_line_card + self.y_line_card_step * num_line_card + self.size_rectangle_card,
                                                                fill=WHITE, outline=BLACK,
                                                                width=WIDTH_RECTANGLE_LINE)

            self.canvas_cards.create_image(10 + int(self.size_rectangle_card / 2),
                                           self.y_line_card + self.y_line_card_step * num_line_card + int(
                                               self.size_rectangle_card / 2),
                                           image=self.DICT_ACTIONS[key][0])

            self.label_line = self.canvas_cards.create_text(20 + self.size_rectangle_card,
                                                            4 + self.y_line_card + self.y_line_card_step * num_line_card,
                                                            text='', justify=LEFT, fill=BLACK,
                                                            font=self.PARAMETERS_FONT_LABEL_LINE_CARD, anchor=NW)

            self.label_list.append(self.label_line)

            self.dict_tasks[num_line_card] = self.dict_tasks.get(num_line_card, []) + [self.line_task]

            self.line_tasks_but = self.canvas_cards.tag_bind(self.dict_tasks[num_line_card],
                                                             "<Button-1>",
                                                             lambda x: open_win_rules_or_task(self.window_game,
                                                                                              width_window_rules=self.width_window_game,
                                                                                              height_window_rules=self.height_window_game,
                                                                                              name_list="Задание",
                                                                                              name_file_txt=self.canvas_cards.itemcget(
                                                                                                  self.label_list[
                                                                                                      num_line_card],
                                                                                                  'text')))

        self.canvas_cards.tag_bind(self.dict_tasks[0],
                                   "<Button-1>",
                                   lambda x: open_win_rules_or_task(self.window_game,
                                                                    width_window_rules=self.width_window_game,
                                                                    height_window_rules=self.height_window_game,
                                                                    color_text=self.canvas_cards.itemcget(
                                                                        self.label_list[0], 'fill'),
                                                                    name_list=f"Задание ({TUPLE_ACTION[0]})",
                                                                    name_file_txt=self.canvas_cards.itemcget(
                                                                        self.label_list[0], 'text')))

        self.canvas_cards.tag_bind(self.dict_tasks[1],
                                   "<Button-1>",
                                   lambda x: open_win_rules_or_task(self.window_game,
                                                                    width_window_rules=self.width_window_game,
                                                                    height_window_rules=self.height_window_game,
                                                                    color_text=self.canvas_cards.itemcget(
                                                                        self.label_list[1], 'fill'),
                                                                    name_list=f"Задание ({TUPLE_ACTION[1]})",
                                                                    name_file_txt=self.canvas_cards.itemcget(
                                                                        self.label_list[1], 'text')))

        self.canvas_cards.tag_bind(self.dict_tasks[2],
                                   "<Button-1>",
                                   lambda x: open_win_rules_or_task(self.window_game,
                                                                    width_window_rules=self.width_window_game,
                                                                    height_window_rules=self.height_window_game,
                                                                    color_text=self.canvas_cards.itemcget(
                                                                        self.label_list[2], 'fill'),
                                                                    name_list=f"Задание ({TUPLE_ACTION[2]})",
                                                                    name_file_txt=self.canvas_cards.itemcget(
                                                                        self.label_list[2], 'text')))

        self.canvas_cards.tag_bind(self.dict_tasks[3],
                                   "<Button-1>",
                                   lambda x: open_win_rules_or_task(self.window_game,
                                                                    width_window_rules=self.width_window_game,
                                                                    height_window_rules=self.height_window_game,
                                                                    color_text=self.canvas_cards.itemcget(
                                                                        self.label_list[3], 'fill'),
                                                                    name_list=f"Задание ({TUPLE_ACTION[3]})",
                                                                    name_file_txt=self.canvas_cards.itemcget(
                                                                        self.label_list[3], 'text')))

        self.canvas_cards.tag_bind(self.dict_tasks[4],
                                   "<Button-1>",
                                   lambda x: open_win_rules_or_task(self.window_game,
                                                                    width_window_rules=self.width_window_game,
                                                                    height_window_rules=self.height_window_game,
                                                                    color_text=self.canvas_cards.itemcget(
                                                                        self.label_list[4], 'fill'),
                                                                    name_list=f"Задание ({TUPLE_ACTION[4]})",
                                                                    name_file_txt=self.canvas_cards.itemcget(
                                                                        self.label_list[4], 'text')))

        self.canvas_cards.tag_bind(self.dict_tasks[5],
                                   "<Button-1>",
                                   lambda x: open_win_rules_or_task(self.window_game,
                                                                    width_window_rules=self.width_window_game,
                                                                    height_window_rules=self.height_window_game,
                                                                    color_text=self.canvas_cards.itemcget(
                                                                        self.label_list[5], 'fill'),
                                                                    name_list=f"Задание ({TUPLE_ACTION[5]})",
                                                                    name_file_txt=self.canvas_cards.itemcget(
                                                                        self.label_list[5], 'text')))

        self.canvas_cards.grid(row=1, column=3, pady=0, padx=0)
        # self.my_canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        self.update_figur_map()

    # def on_mousewheel(self, event):
    #     """Функция для прокручивания окна колёсиком мыши, а не бегунком справа."""
    #     try:
    #         self.my_canvas.yview_scroll(-1 * int(event.delta / 120), "units")
    #     except:
    #         self.my_canvas.unbind_all("<MouseWheel>")

    def close_win_game(self):
        """Функция запускает уточняющее окно при закрытии окна игры"""
        if messagebox.askokcancel('Выход из игры', 'Хотите выйти из игры?', parent=self.window_game):
            self.window_game.destroy()

    # Функции для Таймера и его кнопок
    def push_stop(self):
        """Останавливает таймер и активирует функцию запуск аудиофайла"""
        play(NAME_SOUND_TIME_PAUSE)
        self.window_game.after_cancel(self.timer)

    def push_start(self):
        """Запускает таймер заново и активирует функцию запуск аудиофайла,
        обязательно должна быть нажата кнопка стоп/пауза перед использованием если таймер уже идёт"""
        play(NAME_SOUND_TIME_START)
        self.timer_start(TIME_ROUND)
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

            self.timer = self.window_game.after(TIMER_MILLISECONDS, self.timer_start, count - 1)
        else:
            play(NAME_SOUND_TIME_UP)
            messagebox.showinfo(title="Внимание!", message="Время кончилось!", parent=self.window_game)

    def resume(self):
        """Запускается только если таймер был на паузе т.е. запускает таймер с того значения где он был остановлен и
        активирует функцию запуск аудиофайла"""
        play(NAME_SOUND_TIME_CONTINUE)
        self.timer = self.window_game.after(TIMER_MILLISECONDS, self.timer_start, self.count_pause - 1)

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

            self.canvas_cards.itemconfig(item, text=create_line(next(lst_words), num=self.num), fill=BLACK)

            if random_line == num_line_card:
                if choice((True, False)):
                    self.canvas_cards.itemconfig(item, fill=RED)
                    play(NAME_SOUND_ALL)
                    messagebox.showinfo(title="Внимание!", message="Присутствует общее слово!", parent=self.window_game)

    def push_card_3(self):
        """Функция активирует функцию get_card с передачей ей аргумента words.
        Для улучшения генерации карточек по сложности использовать words_from_3 вместо words.
        Для пополнения базы слов нужно заносить слова в файл 'txt_files/words_from_3.txt'"""
        self.canvas_cards.itemconfig(self.number_card_info, text='Карточка №3')
        self.get_card(words_from_3)

    def push_card_4(self):
        """Функция активирует функцию get_card с передачей ей аргумента words.
        Для улучшения генерации карточек по сложности использовать words_from_4 вместо words.
        Для пополнения базы слов нужно заносить слова в файл 'txt_files/words_from_4.txt'"""
        self.canvas_cards.itemconfig(self.number_card_info, text='Карточка №4')
        self.get_card(words_from_4)

    def push_card_5(self):
        """Функция активирует функцию get_card с передачей ей аргумента words.
        Для улучшения генерации карточек по сложности использовать words_from_5 вместо words.
        Для пополнения базы слов нужно заносить слова в файл 'txt_files/words_from_5.txt'"""
        self.canvas_cards.itemconfig(self.number_card_info, text='Карточка №5')
        self.get_card(words_from_5)

    def move(self, event):
        """Функция позволяет передвигать указанные лейблы или фигуры по экрану. Это облегчает движок игры.
        Можно двигать фишки в любой момент игры"""
        mouse_x = self.second_frame.winfo_pointerx() - self.second_frame.winfo_rootx()
        mouse_y = self.second_frame.winfo_pointery() - self.second_frame.winfo_rooty()
        event.widget.place(x=mouse_x, y=mouse_y, anchor=CENTER)

    def update_figur_map(self):
        # РАЗОБРАТЬСЯ ФИНАЛ
        """Функция создаёт фигурки игроков на карте. Цвет и название меняются сразу из настроек
        через глобальные переменные."""
        self.indent_line_team = INDENT_LINE_TEAM

        for i in range(self.count_team):
            # Для карты
            self.indent_line_team += 0.5
            self.text_num_team = self.canvas_map.create_text(self.x_position_team + self.step_x1_create_rectangle // 2,
                                                             self.step_y * (self.indent_line_team + i),
                                                             text=f'Команда №{i + 1}', fill=YELLOW,
                                                             font=self.FONT_TEAM, anchor=W)  # Порядковый номер Команды
            self.text_name_team = self.canvas_map.create_text(self.x_position_team + self.step_x1_create_rectangle // 2,
                                                              self.step_y * (self.indent_line_team + 0.5 + i),
                                                              text=NAME_TEAM[i], fill=YELLOW, justify=LEFT,
                                                              font=self.FONT_NAME_TEAM, anchor=W, )  # Название Команды

            self.label_fig_team = Label(self.second_frame, text=f"{i + 1}", font=self.FONT_NUM_TEAM_SET,
                                        bg=COLOR_TEAM[i],
                                        fg=NUMBER_COLOR[i], highlightthickness=2,
                                        highlightbackground=BLACK)

            self.binding = self.label_fig_team.bind("<B1-Motion>", self.move)  # активация движка на перемещение мышкой
            self.label_fig_team_s = self.canvas_map.create_window(self.x_position_team - self.step_x1_create_rectangle,
                                                                  self.step_y * (self.indent_line_team - 0.25 + i),
                                                                  anchor=NW, window=self.label_fig_team)
            poly_dict[i] = [self.text_num_team, self.text_name_team, self.label_fig_team, self.binding,
                            self.label_fig_team_s]

    def push_set_command(self):
        set_command = SetCommand(self.window_game, self.canvas_map, setting_width_window_game=WIDTH_WINDOW_GAME,
                                 setting_height_window_game=HEIGHT_WINDOW_GAME)


class SetCommand:
    def __init__(self, master, canvas, setting_width_window_game=800, setting_height_window_game=600):

        # Параметры окна
        self.setting_width_com = setting_width_window_game
        self.setting_height_com = setting_height_window_game
        self.canvas_update = canvas

        # Параметры холста где отображаются игровые фигурки для предварительного просмотра
        self.width_win_setting = int(self.setting_width_com * 0.9)
        self.height_canvas_setting = int(self.setting_height_com / 6)

        # Основные переменные и коэффициенты
        self.font_k = self.setting_width_com / 1980

        self.x1_rectangle = x1_rectangle
        self.step_x1_rectangle = int(self.width_win_setting / 6 / 1.1)
        self.step_x1_create_rectangle = int(self.width_win_setting / 6 / 6.6)
        self.y2_rectangle = int(self.height_canvas_setting / 1.6)

        # Шрифты текста
        self.FONT_NAME_SET = (STILE_FONT, int(24 * self.font_k), 'bold')
        self.FONT_TEXT_TEAM_SET = (STILE_FONT, int(20 * self.font_k), 'bold')
        self.FONT_NUM_TEAM_SET = (STILE_FONT, int(24 * self.font_k), 'bold')
        self.FONT_NAME_TEAM_SET = (STILE_FONT, int(14 * self.font_k))  # , 'italic'

        # Шрифты кнопок
        self.FONT_BUTTON_SETTING = (STILE_FONT, int(16 * self.font_k))
        self.indent_y = self.FONT_BUTTON_SETTING[1] // 2

        # Создаём окно
        self.window_setting = Toplevel(master)
        self.window_setting.title('Настройки')

        self.window_setting.geometry(f'{self.setting_width_com}x{self.setting_height_com}')  # параметры окна игры
        self.window_setting.config(padx=20, pady=20, bg=BG_COLOR)

        self.canvas_fig = Canvas(self.window_setting, width=self.width_win_setting, height=self.height_canvas_setting,
                                 bg=BG_COLOR, borderwidth=0, highlightthickness=0)

        self.label_team = Label(self.window_setting, text="Выберите номер команды для изменения цвета", bg=BG_COLOR,
                                fg=YELLOW, font=self.FONT_NAME_SET)

        self.box_number_team = ttk.Combobox(self.window_setting, values=tuple(map(str, range(1, count_team + 1))),
                                            state="readonly", font=self.FONT_BUTTON_SETTING)

        self.button_config_color = Button(self.window_setting, text="Изменить цвет", activebackground=YELLOW,
                                          relief=FLAT, command=self.select_color, font=self.FONT_BUTTON_SETTING)

        self.label_name_team = Label(self.window_setting, text="Новое название команды", bg=BG_COLOR, fg=YELLOW,
                                     font=self.FONT_NAME_SET)

        self.entry_name_team = Entry(self.window_setting, font=self.FONT_BUTTON_SETTING)  # Окно ввода названия команды
        self.entry_name_team.focus()

        self.button_config_name_team = Button(self.window_setting, text="Изменить название команды",
                                              command=self.select_name_team, font=self.FONT_BUTTON_SETTING,
                                              activebackground=YELLOW, relief=FLAT)

        self.label_time_round = Label(self.window_setting, text="Время на раунд (мин.)", bg=BG_COLOR, fg=YELLOW,
                                      font=self.FONT_NAME_SET)
        self.box_time_round = ttk.Combobox(self.window_setting, values=TUPLE_TIME, state="readonly",
                                           font=self.FONT_BUTTON_SETTING)

        self.canvas_fig.grid(row=6, column=0, sticky=W, padx=0, pady=0, columnspan=2)
        self.label_team.grid(row=7, column=0, sticky=W, padx=0, pady=self.indent_y)
        self.box_number_team.grid(row=8, column=0, sticky=W, padx=0, pady=0)
        self.button_config_color.grid(row=9, column=0, sticky=W, padx=0, pady=self.indent_y)
        self.label_name_team.grid(row=10, column=0, sticky=W, padx=0, pady=self.indent_y)
        self.entry_name_team.grid(row=11, column=0, sticky=W, padx=0, pady=0)
        self.button_config_name_team.grid(row=12, column=0, sticky=W, padx=0, pady=self.indent_y)
        self.label_time_round.grid(row=13, column=0, sticky=W, padx=0, pady=self.indent_y)
        self.box_time_round.grid(row=13, column=1, sticky=W, padx=0, pady=self.indent_y)

        self.create_figur_setting()

        self.box_number_team.bind("<<ComboboxSelected>>", self.selected_number_team)
        self.box_time_round.bind("<<ComboboxSelected>>", self.selected_minute)

        self.window_setting.grab_set()
        self.window_setting.focus_set()
        self.window_setting.wait_window()

    def selected_number_team(self, event):
        """Функция задаёт номер конкретной команды для изменения цвета или названия. Номер команды уменьшается на 1 т.к.
        данный номер это индекс для изменения значений в списках цветов и названий команд.
        В случаи ошибки 'нет атрибута' стандартное значение 0."""
        try:
            self.num_team = int(self.box_number_team.get()) - 1
        except AttributeError:
            self.num_team = 0

    def select_color(self):
        """Функция для изменения цвета фигуры выбранной команды в окне настроек и на игровой карте.
        Цифра внутри фигуры меняется на белый если цвет слишком темный.
        Также данный цвет (фигуры и цифры) заносится в словари для запоминания на момент работы игры.
        При новом пуске словари будет со значения по умолчанию"""
        # global COLOR_TEAM, poly_dict_set  # poly_dict
        try:
            result = colorchooser.askcolor(initialcolor="white", parent=self.window_setting)
            COLOR_TEAM[self.num_team] = result[1]
            self.canvas_fig.itemconfig(poly_dict_set[self.num_team][2], fill=result[1])
            poly_dict[self.num_team][2].config(bg=result[1])
            if result[0][0] in range(100) and result[0][1] in range(100) and result[0][2] in range(100):
                self.canvas_fig.itemconfig(poly_dict_set[self.num_team][3], fill=WHITE)
                NUMBER_COLOR[self.num_team] = WHITE
                poly_dict[self.num_team][2].config(fg=NUMBER_COLOR[self.num_team])
            else:
                self.canvas_fig.itemconfig(poly_dict_set[self.num_team][3], fill=BLACK)
                NUMBER_COLOR[self.num_team] = BLACK
                poly_dict[self.num_team][2].config(fg=NUMBER_COLOR[self.num_team])

        except AttributeError:
            messagebox.showwarning("Предупреждение", "Выберете номер команды", parent=self.window_setting)

    def select_name_team(self, num=NUM_INDENT):
        """Функция осуществляет перенос слов названия команды и добавляет пробел если название было слишком длинное.
        Новое название команды заносится в словарь для дальнейшего использования на время работы программы."""
        new_name_team = self.entry_name_team.get()
        number_enter = num
        while len(new_name_team) > number_enter:

            while new_name_team[:number_enter].count(
                    ' ') == 0:  # цикл на случай если в слове вообще не будет пробелов
                new_name_team = f'{new_name_team[number_enter:]} {new_name_team[:number_enter + 1]}'

            ind_end_space = new_name_team[:number_enter].rfind(' ')
            new_name_team = f'{new_name_team[:ind_end_space]}\n{new_name_team[ind_end_space + 1:]}'
            number_enter += num

        NAME_TEAM[self.num_team] = new_name_team
        self.canvas_fig.itemconfig(poly_dict_set[self.num_team][1], text=new_name_team)
        self.canvas_update.itemconfig(poly_dict[self.num_team][1], text=new_name_team)

    def create_figur_setting(self):
        """Функция создаёт игровые фигурки, их название и обозначение в меню настроек.
        Данные о цвете фигурки, названии команды и цвет цифры команды сохраняется в словари для дальнейшего
        использования в других разделах программы."""

        for i in range(count_team):
            self.text_team_set = self.canvas_fig.create_text(self.step_x1_rectangle * i, 0,
                                                             text=f'Команда №{i + 1}',
                                                             fill=YELLOW, font=self.FONT_TEXT_TEAM_SET, anchor=NW)

            self.points_set = [
                self.step_x1_rectangle * i,
                self.FONT_TEXT_TEAM_SET[1] * 2,
                self.x1_rectangle + self.step_x1_create_rectangle * 2 + self.step_x1_rectangle * i,
                self.y2_rectangle,
            ]
            self.polygon_team_set = self.canvas_fig.create_rectangle(self.points_set, fill=COLOR_TEAM[i],
                                                                     outline='#000', width=1.5)
            self.num_team_fig = self.canvas_fig.create_text(
                (self.x1_rectangle + self.step_x1_rectangle * i) + self.FONT_NUM_TEAM_SET[1],
                (self.FONT_TEXT_TEAM_SET[1] * 2 + self.y2_rectangle) // 2, text=f'{i + 1}', fill=NUMBER_COLOR[i],
                anchor=W,
                font=self.FONT_NUM_TEAM_SET)

            self.name_team_set = self.canvas_fig.create_text(self.step_x1_rectangle * i,
                                                             self.y2_rectangle + self.FONT_NAME_TEAM_SET[1] // 2,
                                                             text=NAME_TEAM[i], fill=YELLOW, anchor=NW,
                                                             font=self.FONT_NAME_TEAM_SET)

            poly_dict_set[i] = [self.text_team_set, self.name_team_set, self.polygon_team_set, self.num_team_fig]

    def selected_minute(self, event):
        """Функция берёт значение из списка выбора карты и задаёт глобальной переменной STANDARD_CARD bool значение"""
        global TIME_ROUND
        try:
            TIME_ROUND = int(float(self.box_time_round.get()) * 60)
        except AttributeError:
            TIME_ROUND = 60


start = StartMenu(start_menu_width=width_monitor, start_menu_height=height_monitor)
