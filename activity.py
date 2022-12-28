from game_map_zone import GamesWindow
# from screeninfo import get_monitors
# monitor_parameters = get_monitors()[0]
#
#
# game = GamesWindow(width_window_game=monitor_parameters.width, height_window_game=monitor_parameters.height)

game = GamesWindow()

# pyinstaller activity.py --onefile --noconsole --icon=logo.ico -n Activity
# Рабочая команда для преобразования кода в формат exe:
# 1) --onefile делает один файл
# 2) --noconsole консоль не выводится при запуске
# 3) --icon=название ico файла взять иконку чтобы она стала ярлыком игры
# 4) -n и вводим название игры какое хотим, по дефолту будет название файла////!!!!!
