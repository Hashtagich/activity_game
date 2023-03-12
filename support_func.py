from re import sub

f1 = 'txt_files/words_from_3.txt'
f2 = 'txt_files/words_from_4.txt'
f3 = 'txt_files/words_from_5.txt'
f_all = 'txt_files/words_from_cards.txt'


# Проверка на дубли и повторение слов
def give_list(name):
    with open(name, 'r', encoding='utf-8') as file_txt:
        return [i.lower() for i in file_txt.readline().split(', ')]


def open_file(name):
    with open(name, 'r', encoding='utf-8') as file_txt:
        return [i for i in file_txt.readline().split(', ')]


def checking_duplicates():
    """Функция не применяется в проекте(игре).
    Это вспомогательная функция для проверки наличия дублей в файлах для карточек 3,4 и 5.
    Удаление дублей лучше производить вручную."""
    print("Проверка на дубли и повторение слов")

    l1, l2, l3 = give_list(f1), give_list(f2), give_list(f3)

    comparison3_3 = [i for i in l1 if l1.count(i) > 1]
    comparison4_4 = [i for i in l2 if l2.count(i) > 1]
    comparison5_5 = [i for i in l3 if l3.count(i) > 1]
    print(comparison3_3, comparison4_4, comparison5_5, sep='\n')
    print()

    comparison3_4 = [i for i in l1 if i in l2]
    comparison3_5 = [i for i in l1 if i in l3]
    print(comparison3_4, comparison3_5, sep='\n')
    print()

    comparison4_3 = [i for i in l2 if i in l1]
    comparison4_5 = [i for i in l2 if i in l3]
    print(comparison4_3, comparison4_5, sep='\n')
    print()

    comparison5_3 = [i for i in l3 if i in l1]
    comparison5_4 = [i for i in l3 if i in l2]
    print(comparison5_3, comparison5_4, sep='\n')


def deleting_characters(string: str = "112 sadd dfdf 21 dfheif 12,23 12") -> list[str]:
    """Вспомогательная функция для того чтобы из строки убрать цифры и символы и оставить только буквы и пробелы.
    На выходе получаем список со словами для дальнейшего распределения по карточкам заданий 3,4 и 5. """
    return sub(r'[^\w\s]+|[\d]+', r'', string).strip().split()


def del_duplicates(fun_list: str) -> list:
    """Функция удаляет дубли из переданного файла."""
    list_1 = give_list(fun_list)

    if len(list_1) == len(set(list_1)):
        print("Повторов не обнаружено.")
        result = list_1
    else:
        print(f"Обнаружены дубли в кол-ве {len(list_1) - len(set(list_1))} шт.\nДубли удалены!\nВнимание!!! Все слова в нижнем регистре.")
        result = list(set(list_1))
    return result
