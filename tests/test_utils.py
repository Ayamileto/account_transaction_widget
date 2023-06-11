import os
import pytest
from utils.utils import load_data, get_filtered_data, get_sorted_data


@pytest.fixture()
def testing_data():
    temp_data = os.path.join(os.path.dirname(__file__), "test_data_file.json")
    return temp_data


def test_load_data(testing_data):
    """ Тест на корректность загрузки файла """
    loaded_data = load_data(testing_data)
    assert loaded_data == [
        {"id": 1, "name": "Mary", "state": "EXECUTED"},
        {"id": 2, "name": "Jerry", "state": "CANCELED"},
        {},
        {"id": 3, "name": "Piter", "state": "EXECUTED"}
    ]


@pytest.mark.parametrize('testing_data, expected', [
    ([
        {"id": 1, "name": "Mary", "state": "EXECUTED"},
        {"id": 2, "name": "Jerry", "state": "CANCELED"},
        {},
        {"id": 3, "name": "Piter", "state": "EXECUTED"}
        ],
        [
        {"id": 1, "name": "Mary", "state": "EXECUTED"},
        {"id": 3, "name": "Piter", "state": "EXECUTED"}
    ])
])
def test_get_filtered_data(testing_data, expected):
    """ Тест на фильтрацию данных """
    filtered_data = get_filtered_data(testing_data)
    assert filtered_data == expected


@pytest.mark.parametrize('testing_data, expected', [
    ([
        {"id": 1, "name": "Mary", "state": "EXECUTED"},
        {"id": 2, "name": "Jerry"}],
        KeyError)
])
def test_get_filtered_dataKeyError(testing_data, expected):
    """ Тест на ошибку по ключу """
    with pytest.raises(expected):
        get_filtered_data(testing_data)


@pytest.mark.parametrize('testing_data, expected', [
    ([{'data': 3}, {'data': 1}, {'data': 2}, {'data': 7}, {'data': 12}, {'data': 71}, {'data': 20}],
        [{'data': 71}, {'data': 20}, {'data': 12}, {'data': 7}, {'data': 3}]),
    ([{'data': 5}, {'data': 2}, {'data': 8}], [{'data': 8}, {'data': 5}, {'data': 2}])
])
def test_get_sorted_data(testing_data, expected):
    """ Тест на проверку корректности сортировки данных по ключу и порядку"""
    assert get_sorted_data(testing_data) == expected