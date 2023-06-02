# программа для рассчета КПД футболиста
# со специальных датчиков в форме игрока в компьютер поступают данные о дейсвтвиях на поле
# на основании алгоритмов рассчитывается его статистика как в карточке игрока ФИФА на плойке и КПД за матч
# попытка сделать на модулях и классах

# Главное меню
#     1. РАссчитать КПД за матч
#     2. РАссчитать стату
#     3. РАссчитать защиту
#     4. РАссчитать атаку
#     5. РАссчитать физику
#     6. Выход\n'''

import moduls
import text

def start_main_menu():
    while True:
        select=moduls.start_main_menu()
        match select:
                case 1:
                    player_number=moduls.select_player()
                    print(moduls.kpi(player_number))
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    break

start_main_menu()