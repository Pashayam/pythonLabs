import pytest
import what_is_year_now
from unittest.mock import patch, MagicMock


@patch('urllib.request.urlopen')
def test_first_format(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",' \
                             '"currentDateTime":"2021-03-22T01:12Z",' \
                             '"utcOffset":"00:00:00",' \
                             '"isDayLightSavingsTime":false,' \
                             '"dayOfTheWeek":"Monday",' \
                             '"timeZoneName":"UTC",' \
                             '"currentFileTime":132608491427816346,' \
                             '"ordinalDate":"2021-81",' \
                             '"serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    year = what_is_year_now.what_is_year_now()
    assert year == 2021


@patch('urllib.request.urlopen')
def test_second_format(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",' \
                             '"currentDateTime":"01.03.2021T01:12Z",' \
                             '"utcOffset":"00:00:00",' \
                             '"isDayLightSavingsTime":false,' \
                             '"dayOfTheWeek":"Monday",' \
                             '"timeZoneName":"UTC",' \
                             '"currentFileTime":132608491427816346,' \
                             '"ordinalDate":"2021-81",' \
                             '"serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    year = what_is_year_now.what_is_year_now()
    assert year == 2021


@patch('urllib.request.urlopen')
def test_exception_format(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",' \
                             '"currentDateTime":"2021T01:12Z",' \
                             '"utcOffset":"00:00:00",' \
                             '"isDayLightSavingsTime":false,' \
                             '"dayOfTheWeek":"Monday",' \
                             '"timeZoneName":"UTC",' \
                             '"currentFileTime":132608491427816346,' \
                             '"ordinalDate":"2021-81",' \
                             '"serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    with pytest.raises(Exception):
        what_is_year_now.what_is_year_now()

