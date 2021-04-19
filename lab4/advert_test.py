import json

import pytest

import advert


def test_negative_price_initialization():
    lesson_str = """{
          "title": "iPhone X",
          "price": -100,
          "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
          }
        }"""
    with pytest.raises(ValueError):
        advert.Advert(json.loads(lesson_str))


def test_setting_a_negative_price():
    lesson_str = """{
          "title": "iPhone X",
          "price": 100,
          "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
          }
        }"""
    obj = advert.Advert(json.loads(lesson_str))
    with pytest.raises(ValueError):
        obj.price = -1


def test_address():
    lesson_str = """{
          "title": "iPhone X", 
          "price": 100,
          "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
          }
        }"""
    obj = advert.Advert(json.loads(lesson_str))
    expected = "город Самара, улица Мориса Тореза, 50"
    assert obj.location.address == expected


def test_keyword():
    lesson_str ="""{
          "title": "iPhone X",
          "price": 100,
          "class": "Phone",
          "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
          }
        }"""
    obj = advert.Advert(json.loads(lesson_str))
    expected = "Phone"
    assert obj.class_ == expected


