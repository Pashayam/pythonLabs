import json
from keyword import iskeyword


class ColorizeMixin:
    repr_color_code = 36

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};1m'\
               f'{self.title} | {self.price} ₽'


class Advert(ColorizeMixin):
    _price: int = 0

    # def __repr__(self):
    #     return f'{self.title} | {self.price} ₽'

    def __init__(self, date: dict):
        for key, v in date.items():
            if iskeyword(key):
                key = key+"_"

            if isinstance(v, dict):
                setattr(self, key, Advert(v))
                continue
            setattr(self, key, v)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, key: int):
        if key >= 0:
            self._price = key
        else:
            raise ValueError("price less 0")


if __name__ == '__main__':
    lesson_str = """{
          "title": "Вельш-корги",
          "price": 1000,
          "class": "dogs",
          "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
          }
        }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad)
    print(lesson_ad.title)
    print(lesson_ad.location.address)