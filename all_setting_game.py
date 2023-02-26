from screeninfo import get_monitors

monitor_parameters = get_monitors()[0]
width_monitor = monitor_parameters.width
height_monitor = monitor_parameters.height

# GAME PARAMETERS
NAME_GAME = 'ACTIVITY'
WIDTH_WINDOW_GAME = width_monitor
HEIGHT_WINDOW_GAME = height_monitor
NUM_INDENT = 26
FINISH = 49
STANDARD_CARD = True
thickness = 0  # Толщина рамки для игровой доски
count_team = 5
INDENT_LINE_TEAM = 1
COUNT_CAGE_IN_LINE = 5
COUNT_CAGE_IN_LINE_1 = COUNT_CAGE_IN_LINE - 1
poly_dict, poly_dict_set = {}, {}
TUPLE_ACTION = ("Нарисовать", "Объяснить словами", "Показать жестами",
                "Нарисовать", "Объяснить словами", "Показать жестами")
STILE_FONT = 'Times new roman'  # Общий стиль шрифта в игре
TUPLE_EL = ('2', '3', '4', '5', '6')
TUPLE_MAP = ('Стандартная', 'Случайная')
TUPLE_TIME = ('0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5',
              '5')  # tuple(map(lambda x: str(int(x * 0.5) if str(x * 0.5)[-1] != '5' else x * 0.5), range(1, 11)))

# Timer
TIMER_MILLISECONDS = 1000  # микросекунды
TIME_ROUND = 60  # сколько секунд команда будет отгадывать слово

# Canvas_map parameters
WIDTH_RECTANGLE_LINE = 3

# Map setting
x1, y_1 = 20, 20
NUMBER_LINE = 1  # разделение линий игрового поля на чётный и нечётные для корректного отображения на экране
step_zero = 0  # переменная для размещения финиша после последней клетки

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

# Для настроек цвета фигур команды
x1_rectangle = 20
y1_rectangle = 30
COLOR_TEAM = [RED, BLUE, GREEN, YELLOW, ORANGE, PINK]  # список цветов команд по умолчанию, потом будет меняться
NAME_TEAM = ["Название №1", "Название №2", "Название №3", "Название №4", "Название №5",
             "Название №6"]  # список стандартных названий команд, потом будет меняться
NUMBER_COLOR = [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]

# path txt file
directory_txt_file = 'txt_files/'
path_file_all_words = f'{directory_txt_file}words_from_cards.txt'
path_file_words_from_3 = f'{directory_txt_file}words_from_3.txt'
path_file_words_from_4 = f'{directory_txt_file}words_from_4.txt'
path_file_words_from_5 = f'{directory_txt_file}words_from_5.txt'
path_file_rules = 'txt_files\\rules.txt'
path_file_control = 'txt_files\\control.txt'
path_file_about = 'txt_files\\about.txt'

# image path/name
# сайт с иконками для игры https://iconarchive.com/
directory_images = "images/"
dict_path_image = {
    '3840x2160': (f'{directory_images}речь96.png', f'{directory_images}мим96.png', f'{directory_images}рисовать96.png'),
    '2560x1600': (f'{directory_images}речь72.png', f'{directory_images}мим72.png', f'{directory_images}рисовать72.png'),
    '2560x1440': (f'{directory_images}речь72.png', f'{directory_images}мим72.png', f'{directory_images}рисовать72.png'),
    '2048x1536': (f'{directory_images}речь64.png', f'{directory_images}мим64.png', f'{directory_images}рисовать64.png'),
    '1920x1440': (f'{directory_images}речь48.png', f'{directory_images}мим48.png', f'{directory_images}рисовать48.png'),
    '1920x1200': (f'{directory_images}речь48.png', f'{directory_images}мим48.png', f'{directory_images}рисовать48.png'),
    '1920x1080': (f'{directory_images}речь48.png', f'{directory_images}мим48.png', f'{directory_images}рисовать48.png'),
    '1680x1050': (f'{directory_images}речь48.png', f'{directory_images}мим48.png', f'{directory_images}рисовать48.png'),
    '1600x1200': (f'{directory_images}речь48.png', f'{directory_images}мим48.png', f'{directory_images}рисовать48.png'),
    '1600x1024': (f'{directory_images}речь48.png', f'{directory_images}мим48.png', f'{directory_images}рисовать48.png'),
    '1600x900': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '1440x900': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '1400x1050': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '1366x768': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '1360x768': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '1280x1024': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '1280x960': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '1280x800': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '1280x768': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '1280x720': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '1176x664': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '1152x864': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '1024x768': (f'{directory_images}речь32.png', f'{directory_images}мим32.png', f'{directory_images}рисовать32.png'),
    '800x600': (f'{directory_images}речь24.png', f'{directory_images}мим24.png', f'{directory_images}рисовать24.png'),
}

TUPLE_SCREEN_SETTINGS = tuple(map(str, dict_path_image.keys()))

# sounds name
directory_sounds = 'sounds/'
NAME_SOUND_START = f'{directory_sounds}хочешь сыграть.mp3'
NAME_SOUND_TIME_START = f'{directory_sounds}гонг.mp3'
NAME_SOUND_TIME_PAUSE = f'{directory_sounds}zawordo.mp3'
NAME_SOUND_TIME_CONTINUE = f'{directory_sounds}moody blues.mp3'
NAME_SOUND_TIME_UP = f'{directory_sounds}время деньги.mp3'
NAME_SOUND_ALL = f'{directory_sounds}все сюда.mp3'
NAME_SOUND_END = f'{directory_sounds}moody blues.mp3'
