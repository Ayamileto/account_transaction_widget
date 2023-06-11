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


def get_sorted_data(data):
    """ Функция принимает список, сортирует его по ключу в обратном порядке и возвращает 5 последних операций """
    sorted_list = sorted(data, key=lambda x: x['data'], reverse=True)
    sliced_list = sorted_list[:5]
    return sliced_list
