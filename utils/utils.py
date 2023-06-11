import json


def load_data(filename):
    """ Функция открывает и читает файл """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data):
    """ Функция фильтрует операции по выполненным и исключает пустые операции"""
    filtered_list = [operation for operation in data if operation and operation['state'] == 'EXECUTED']
    return filtered_list



