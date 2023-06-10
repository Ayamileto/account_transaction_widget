import json


def load_data(filename):
    """ Функция открывает и читает файл """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data






