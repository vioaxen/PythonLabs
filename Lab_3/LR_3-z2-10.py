import random
import nltk
from nltk.corpus import words


def cout(label: str, collection, extra=None):
    """Выводит заданную строку и элементы коллекции.

    Аргументы:
        label (str): Строка для вывода.
        collection(iterable): Коллекция элементов, которые нужно вывести.
        extra (any, optional): Дополнительный аргумент для вывода. По умолчанию None.
    """
    output = f'{label} ' + ', '.join(map(str, collection))

    if extra is not None:
        output = f"{label} '{extra}' " + ', '.join(map(str, collection))

    print(output)


def load_russian_words(file_path: str):
    """Загружает русские слова из файла.

    Аргументы:
        file_path (str): Путь к файлу с русскими словами.

    Возвращает:
        list: Список русских слов, прочитанных из файла.
    """
    with open(file_path, 'r', encoding='windows-1251') as file:
        return file.read().splitlines()


def main():
    """Основная функция программы.

    Загружает русские слова из файла, выбирает случайные слова,
    преобразует их в кортеж и сет, проверяет уникальность элементов,
    и выполняет операции удаления элементов из сета.
    """
    # Загрузка русских слов
    russian_words = load_russian_words(
        'C:\\Users\\aksen\\Documents\\РХТУ им. Д. И. Менделеева\\3 семестр\\Основы языка программирования '
        'Python\\PythonLabs\\src\\russian.txt'
    )

    # Генерация 5 случайных слов
    random_words = random.sample(russian_words, 5)
    A = tuple(random_words)
    cout("Кортеж A:", A)

    # A. Преобразовать кортеж A в сет B
    B = set(A)
    cout("Сет B:", B)

    # B. Проверить, все ли элементы кортежа A были уникальны
    if len(A) == len(B):
        print("Все элементы кортежа A уникальны")
    else:
        print("Некоторые элементы кортежа A не уникальны")

    # C. Удалить из сета B последний элемент, входивший в исходный кортеж A.
    last_element = A[-1]
    B.discard(last_element)
    cout("Сет B после удаления последнего элемента:", B, last_element)

    # D. Удалить из сета B элементы сета C {"удалить", "эти", "элементы"}
    C = {"удалить", "эти", "элементы"}
    B -= C
    cout("Сет B после удаления элементов сета C:", B)


if __name__ == "__main__":
    main()
