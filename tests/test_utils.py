import pytest
from utils.utils import load_data


@pytest.fixture()
def testing_data():
    temp_data = "test_data_file.json"
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



