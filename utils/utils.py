import json


def load_data():
    """ Функция открывает и читает файл """
    with open('data', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


