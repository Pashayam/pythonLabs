from random import random
from string import punctuation
from time import time, sleep


def calc_duration(func):
    def dec_fun():
        start_func = time()
        func()
        end_func = time()
        print(f"Функция работала {end_func-start_func} секунд")
    return dec_fun


@calc_duration
def long_executing_task():   # func(*args, **kwargs) ==== long_executing_task
    for index in range(3):
        print(f'Iteration {index}')
        sleep(random())


def suppress_errors(errors):

    def decorator_1(func):
        def decorator_2(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors as error:
                print(f"ОШИБКА: {error}")
        return decorator_2
    return decorator_1


@suppress_errors((
    KeyError,
    ValueError,
))
def potentially_unsafe_func(key: str):
    print(f'Get data by the key {key}')
    data = {'name': 'test', 'age': 30}
    return data[key]


def result_between(value_min, value_max):
    def decorator_1(func):
        def decorator_2(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if value_min <= func_result <= value_max:
                return func_result
            else:
                raise ValueError
        return decorator_2
    return decorator_1


def len_more_than(str_len):
    def decorator_1(func):
        def decorator_2(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if len(func_result) >= str_len:
                return func_result
            else:
                raise ValueError
        return decorator_2
    return decorator_1


@result_between(0, 10)
def sum_of_values(numbers):
    return sum(numbers)


@len_more_than(10)
def show_message(message: str) -> str:
    return f'Hi, you sent: {message}'


def replace_commas(func):
    def dec_fun(text):
        for char in punctuation:
            text = text.replace(char, ' ')
        return func(text)

    return dec_fun


def words_title(func):
    def dec_fun(text):
        result_str = ""
        for i in range(len(text)):
            if i == 0 or i == len(text)-1:
                result_str += text[i]
                continue
            if text[i-1] == ' ' or text[i+1] == ' ':
                result_str += str.upper(text[i])
                continue
            result_str += text[i]
        return func(result_str)
    return dec_fun


@words_title
@replace_commas
def process_text(text: str) -> str:
    return text.replace(':', ',')


@replace_commas
@words_title
def another_process(text: str) -> str:
    return text.replace(':', ',')


def cache_result(func):
    cache = {}

    def dec_fun(*args, **kwargs):
        key = args.__str__() + kwargs.__str__()
        if key in cache:
            return cache[key]
        else:
            cache[key] = func(*args, **kwargs)
            return cache[key]

    return dec_fun


@cache_result
def some_func(last_name, first_name, age):
    return f'Hi {last_name} {first_name}, you are {age} years old'


# print(some_func('shulyak', 'dmitry', 30))  # call
# print(some_func('ivanov', 'ivan', 25))     # call
# print(some_func('shulyak', 'dmitry', 30))  # cache
#
#
# print(process_text('the French revolution resulted in 3 concepts: freedom,equality,fraternity'))
# print(another_process('the French revolution resulted in 3 concepts: freedom,equality,fraternity'))
# print(potentially_unsafe_func("abc"))
# potentially_unsafe_func("abc")
# # print(sum_of_values((1, 3, 5, 7)))
# # sum_of_values((1, 3, 5, 7))
# print(show_message(None) )

