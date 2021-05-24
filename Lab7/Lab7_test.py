import pytest
import Lab7

def test_potentially_unsafe_func():
    result = Lab7.potentially_unsafe_func('name')
    assert result == 'test'


def test_potentially_unsafe_func_silented():
    result = Lab7.potentially_unsafe_func('abc')
    assert result is None


def test_potentially_unsafe_func_none():
    with pytest.raises(TypeError):
        Lab7.potentially_unsafe_func(None, None)


def test_sum_of_values():
    result = Lab7.sum_of_values((1, 3, 5))
    assert result == 9


def test_sum_of_values_err():
    with pytest.raises(ValueError):
        Lab7.sum_of_values((1, 3, 5, 7))


def test_sum_of_values_none():
    with pytest.raises(TypeError):
        Lab7.sum_of_values(None)


def test_show_message():
    assert Lab7.show_message('Howdy, howdy my little friend') == "Hi, you sent: Howdy, howdy my little friend"


def test_show_message_none():
    assert Lab7.show_message(None) == "Hi, you sent: None"


def test_process_text():
    result = Lab7.process_text(
        'the French revolution resulted in 3 concepts: freedom,equality,fraternity')
    assert result == 'thE FrencH RevolutioN ResulteD IN 3 Concepts  Freedom equality fraternity'


def test_process_text_none():
    with pytest.raises(TypeError):
        Lab7.process_text(None)


def test_another_process():
    result = Lab7.another_process(
        'the French revolution resulted in 3 concepts: freedom,equality,fraternity')
    assert result == 'thE FrencH RevolutioN ResulteD IN 3 ConceptS  FreedoM EqualitY Fraternity'


def test_another_process_none():
    with pytest.raises(AttributeError):
        Lab7.another_process(None)