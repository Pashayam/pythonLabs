import pytest
import one_hot_encoder


def test_pytest_cities_with_copy():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert one_hot_encoder.fit_transform(cities) == expected


def test_pytest_cities_without_copy():
    cities = ['Moscow', 'New York', 'Moscow']
    expected = [
        ('Moscow', [0, 1]),
        ('New York', [1, 0]),
        ('Moscow', [0, 1]),
    ]
    assert one_hot_encoder.fit_transform(cities) == expected


def test_pytest_ony_london():
    cities = ['London']
    expected = [
        ('London', [1]),
    ]
    assert one_hot_encoder.fit_transform(cities) == expected


def test_pytest_exception():
    with pytest.raises(Exception):
        one_hot_encoder.fit_transform(342)