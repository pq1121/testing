from main1 import Logger1
import pytest
import os

@pytest.fixture()
def logger():
    path_file_logger = "test.txt"

    yield Logger1(path_file_logger)

    os.remove(path_file_logger)

@pytest.mark.logger
@pytest.mark.parametrize("message, expected_result",
                         [
                             ("что то", "что то"),
                             ("ничего", "ничего"),
                             ("было и было", "было и было")
                         ])
def test_logger_positive(logger, message, expected_result):
    logger.log(message)

    assert  logger.get_logs()[0].replace("\n","") == expected_result


@pytest.mark.logger
@pytest.mark.parametrize("message, expected_result",
                         [
                             (-1000, TypeError),
                             (3123, TypeError),
                             (3123.321, TypeError)
                         ])
def test_logger_negative(logger, message, expected_result):

    with pytest.raises(expected_result):
        logger.log(message)


@pytest.mark.logger
@pytest.mark.parametrize("message, expected_result",
                         [
                             ("", ""),
                             (" ", " "),
                             ("''", "''"),
                         ])
def test_logger_bound(logger, message, expected_result):
    logger.log(message)

    assert  logger.get_logs()[0].replace("\n","") == expected_result