import random


def cout(label: str, collection, extra=None):
    """Выводит заданную строку и элементы коллекции.

    Аргументы:
        label (str): Строка для вывода.
        collection (iterable): Коллекция элементов, которые нужно вывести.
        extra (any, optional): Дополнительный аргумент для вывода. По умолчанию None.
    """
    # Проверка, является ли collection словарем
    if isinstance(collection, dict):
        # Форматирование вывода для словаря
        output = f"{label}: " + ', '.join(f"{key}: {value}" for key, value in collection.items())
    else:
        # Форматирование вывода для остальных коллекций
        output = f'{label}: ' + ', '.join(map(str, collection))

    if extra is not None:
        output = f"{label} '{extra}': " + ', '.join(map(str, collection))

    print(output)


def create_dictionary() -> dict:
    """Создает словарь с ключами от 2 до 14 и случайными целыми значениями от 0 до 100.

    Возвращает:
        dict: Словарь с ключами и случайными значениями.
    """
    return {key: random.randint(0, 100) for key in range(2, 15)}


def remove_keys(dictionary: dict, keys_to_remove: list):
    """Удаляет заданные ключи из словаря.

    Аргументы:
        dictionary (dict): Словарь, из которого нужно удалить ключи.
        keys_to_remove (list): Список ключей для удаления.
    """
    for key in keys_to_remove:
        dictionary.pop(key, None)


def insert_element(dictionary: dict, key: int, value: int):
    """Вставляет новый элемент в словарь.

    Аргументы:
        dictionary (dict): Словарь, в который нужно вставить элемент.
        key (int): Ключ нового элемента.
        value (int): Значение нового элемента.
    """
    dictionary[key] = value


def group_and_sort_values(dictionary: dict) -> list:
    """Группирует значения из словаря в список и сортирует его по убыванию.

    Аргументы:
        dictionary (dict): Словарь, из которого нужно извлечь значения.

    Возвращает:
        list: Список значений, отсортированный по убыванию.
    """
    return sorted(dictionary.values(), reverse=True)


def main():
    """Основная функция программы.

    Создает словарь, выполняет удаление, вставку и сортировку значений,
    а затем выводит результаты на экран.
    """
    # Создание словаря A
    A = create_dictionary()
    print("Словарь A:", A)

    # Удаление элементов с ключами 13 и 14
    remove_keys(A, [13, 14])
    print("Словарь A после удаления ключей 13 и 14:", A)

    # Вставка элемента 1:0
    insert_element(A, 1, 0)
    print("Словарь A после вставки элемента 1:0:", A)

    # Группировка и сортировка значений в список B
    B = group_and_sort_values(A)
    print("Список B (отсортированные значения словаря A по убыванию):", B)


if __name__ == "__main__":
    main()
