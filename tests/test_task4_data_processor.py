from main1 import DataProcessor
import pytest
import os, json


@pytest.fixture(scope="module")
def data_processor():
    path_file_json = "test.json"
    data_json = {
        "1": "первое",
        "2": "второе",
        "3": "третье",
        "4": "четвертое"
    }

    with open(path_file_json, "w", encoding="utf-8") as file:
        json.dump(data_json, file)

    yield DataProcessor(path_file_json)

    os.remove(path_file_json)

@pytest.mark.data_processor
@pytest.mark.parametrize("key, expected_result",
                         [
                             ("1", "первое"),
                             ("2", "второе"),
                             ("3", "третье")
                         ])
def test_data_processor_positive(data_processor, key, expected_result):
    data_processor.load_data()

    assert  data_processor.get_value(key) == expected_result


@pytest.mark.data_processor
@pytest.mark.parametrize("key, expected_result",
                         [
                             ("-1000", None),
                             ("22", None),
                             ("11", None)
                         ])
def test_data_processor_negative(data_processor, key, expected_result):
    data_processor.load_data()

    assert  data_processor.get_value(key) == expected_result


@pytest.mark.data_processor
@pytest.mark.parametrize("key, expected_result",
                         [
                             (["1"], TypeError)
                         ])
def test_data_processor_bound(data_processor, key, expected_result):
    data_processor.load_data()

    with pytest.raises(expected_result):
        data_processor.get_value(key)