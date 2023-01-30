from all_setting_game import path_file_words_from_3, path_file_words_from_4, path_file_words_from_5
from re import sub


# Проверка на дубли и повторение слов
def checking_duplicates():
    """Функция не применяется в проекте(игре).
    Это вспомогательная функция для проверки наличия дублей в файлах для карточек 3,4 и 5.
    Удаление дублей лучше производить вручную."""
    print("Проверка на дубли и повторение слов")

    f1 = path_file_words_from_3
    f2 = path_file_words_from_4
    f3 = path_file_words_from_5

    def give_list(name):
        with open(name, 'r', encoding='utf-8') as file_txt:
            return [i.lower() for i in file_txt.readline().split(', ')]

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


checking_duplicates()
list_words = deleting_characters()
print(list_words)
