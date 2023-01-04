# GAME PARAMETERS
NAME_GAME = 'ACTIVITY'
WIDTH_WINDOW_GAME = 1920
HEIGHT_WINDOW_GAME = 1080
COUNT_CAGE_IN_LINE = 5
COUNT_CAGE_IN_LINE_1 = COUNT_CAGE_IN_LINE - 1
FINISH = 49

# Timer
TIMER_MILLISECONDS = 1000  # микросекунды
time_round = 60  # сколько секунд команда будет отгадывать слово

# Canvas_map parameters
# WIDTH_FIELD = 1400
# HEIGHT_FIELD = 900
WIDTH_RECTANGLE_LINE = 3

# Map setting
# step_x, step_y = 200, 60  # размер клетки
x1, y_1 = 20, 20
# x2 = x1 + step_x
# y_2 = y_1 + step_y
# line_indent = 20  # размер разделительно полосы
NUMBER_LINE = 1  # разделение линий игрового поля на чётный и нечётные для корректного отображения на экране
step_zero = 0  # переменная для размещения финиша после последней клетки

# Canvas_card parameters
# WIDTH_FIELD_CARD = 480
# HEIGHT_FIELD_CARD = 900

# y_image_card = 100
# y_line_card = 300
# y_line_card_step = 100

# Team
NUMBER_TEAMS = 6
INDENT_LINE_TEAM = 1
# X_POSITION_TEAM = WIDTH_FIELD - 300

# color
BLACK = '#000'
WHITE = '#fff'
BG_COLOR = "#006400"
PINK = '#e986d8'
ORANGE = '#ea7500'
BLUE = '#00BFFF'
DARK_BLUE = '#122FAA'
GREEN = '#138808'
YELLOW = '#FAD201'
RED = '#EF3038'
COLOR_INVISIBLE = '#78DBE2'
TUPLE_COLOR = ("YELLOW", "BLUE", "PINK", "GREEN", "DARK_BLUE", "ORANGE")  # стандартная очередь цвета линий в карточке


# Font parameters
FONT_NAME = ('Courier', 32, 'bold')
FONT_TEAM = ('Courier', 24, 'bold')
FONT_NAME_TEAM = ('Courier', 14, 'italic')
FONT_NAME_SET = ('Courier', 20, 'bold')
FONT_WARNING_SET = ('Courier', 20, 'bold')
FONT_TEXT_SET = ('Courier', 16, 'bold')
FONT_TEXT_TEAM_SET = ('Courier', 12, 'bold')
FONT_NUM_TEAM_SET = ('Courier', 30, 'bold')
FONT_NAME_TEAM_SET = ('Courier', 10, 'italic')
PARAMETERS_FONT_LABEL = ('Courier', 35, 'bold')
PARAMETERS_FONT_LABEL_LINE_CARD = ('Courier', 18, 'bold')
PARAMETERS_FONT_SES = ('Courier', 18, 'bold')
PARAMETERS_FONT_BUTTON = ('Courier', 14, 'bold')
PARAMETERS_FONT_BUTTON_CARD = ('Courier', 70, 'bold')
FONT_TEXT_NUMBER = ('Courier', 16, 'bold')
FONT_TEXT_RULES = ('Courier', 16)


# Для настроек цвета фигур команды
# WIDTH_CANVAS_SETTING = 1200
# HEIGHT_CANVAS_SETTING = 160
# PARAMETERS_WINDOW_SETTING = f"{WIDTH_CANVAS_SETTING}x700"
# count_team = 2

x1_rectangle = 20
y1_rectangle = 30
# y2_rectangle = 100
# step_x1_rectangle = 180
# step_x1_create_rectangle = 30

COUNT_TEAM_LIST = ('2', '3', '4', '5', '6')  # картеж кол-ва команд для списка-бокса выбора команд
COLOR_TEAM = [RED, BLUE, GREEN, YELLOW, ORANGE, PINK]  # список цветов команд по умолчанию, потом будет меняться
NAME_TEAM = ["Название №1", "Название №2", "Название №3", "Название №4", "Название №5",
             "Название №6"]  # список стандартных названий команд, потом будет меняться

TEXT_WARNING = """Внимание! 
Не меняйте кол-во команд и не нажимайте 'Обновить' во время игры! Это приведёт к возврату фишек на стартовую позицию."""

# path txt file
directory_txt_file = 'txt_files/'
path_file_all_words = f'{directory_txt_file}words_from_cards.txt'
path_file_words_from_3 = f'{directory_txt_file}words_from_3.txt'
path_file_words_from_4 = f'{directory_txt_file}words_from_4.txt'
path_file_words_from_5 = f'{directory_txt_file}words_from_5.txt'
path_file_rules = 'txt_files\\rules.txt'
path_file_control = 'txt_files\\control.txt'

# image path/name
directory_images = "images/"
# для разрешений 2к fullHD
name_image_dialogue = f'{directory_images}речь.png'
name_image_gestures = f'{directory_images}мим.png'
name_image_painting = f'{directory_images}рисовать.png'
name_image_card3 = f'{directory_images}карта3.png'
name_image_card4 = f'{directory_images}карта4.png'
name_image_card5 = f'{directory_images}карта5.png'
# для разрешений 4к
name_image_dialogue_4k = f'{directory_images}речь.png'
name_image_gestures_4k = f'{directory_images}мим.png'
name_image_painting_4k = f'{directory_images}рисовать.png'
# для разрешений 720p и ниже
name_image_dialogue_720 = f'{directory_images}речь.png'
name_image_gestures_720 = f'{directory_images}мим.png'
name_image_painting_720 = f'{directory_images}рисовать.png'


# sounds name
directory_sounds = 'sounds/'
NAME_SOUND_START = f'{directory_sounds}хочешь сыграть.mp3'
NAME_SOUND_TIME_START = f'{directory_sounds}гонг.mp3'
NAME_SOUND_TIME_PAUSE = f'{directory_sounds}zawordo.mp3'
NAME_SOUND_TIME_CONTINUE = f'{directory_sounds}moody blues.mp3'
NAME_SOUND_TIME_UP = f'{directory_sounds}время деньги.mp3'
NAME_SOUND_ALL = f'{directory_sounds}все сюда.mp3'
NAME_SOUND_END = f'{directory_sounds}moody blues.mp3'

