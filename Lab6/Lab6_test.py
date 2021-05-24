import pytest
import Lab6


def test_ilen_none():
    with pytest.raises(TypeError):
        Lab6.ilen(None)


def test_ilen_str():
    assert Lab6.ilen("String") == 6


def test_ilen_gen():
    assert Lab6.ilen(x for x in range(10)) == 10


def test_ilen_list():
    assert Lab6.ilen([1, 2, 3, 4, 5, 5]) == 6


def test_flatten_none():
    with pytest.raises(TypeError):
        list(Lab6.flatten(None))


def test_flatten_string():
    with pytest.raises(RecursionError):
        list(Lab6.flatten("String"))


def test_flatten_list():
    assert list(Lab6.flatten([0, [1, [2, 3]]])) == [0, 1, 2, 3]


def test_flatten_tuple():
    assert list(Lab6.flatten((1, 2, 3, (2, 3)))) == [1, 2, 3, 2, 3]


def test_distinct_none():
    with pytest.raises(TypeError):
        list(Lab6.distinct(None))


def test_distinct_string():
    assert list(Lab6.distinct("sstring")) == ['s', 't', 'r', 'i', 'n', 'g']


def test_distinct_list():
    assert list(Lab6.distinct([1, 2, 0, 1, 3, 0, 2])) == [1, 2, 0, 3]


def test_distinct_tuple():
    assert list(Lab6.distinct((1, 2, 3, 3, (2, 3)))) == [1, 2, 3, (2, 3)]


def test_groupby_key():
    users = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21},
    ]
    expect = {'female': [{'gender': 'female', 'age': 33}, {'gender': 'female', 'age': 21}], 'male': [{'gender': 'male', 'age': 20}]}

    assert Lab6.groupby('gender', users) == expect


def test_groupby_error_key():
    users = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21},
    ]
    with pytest.raises(KeyError):
        Lab6.groupby('key', users)


def test_groupby_none():
    with pytest.raises(TypeError):
        Lab6.groupby(None, None)


def test_chunks_list():
    assert (list(Lab6.chunks(3, [0, 1, 2, 3, 4]))) == [(0, 1, 2), (3, 4)]


def test_chunks_str():
    assert (list(Lab6.chunks(3, "String"))) == [('S', 't', 'r'), ('i', 'n', 'g')]


def test_chunks_none():
    with pytest.raises(TypeError):
        list(Lab6.chunks(None, None))


def test_first_gen():
    assert Lab6.first(x for x in range(10)) == 0


def test_first_str():
    assert (Lab6.first("String")) == 'S'


def test_first_none():
    with pytest.raises(TypeError):
        Lab6.first(None)

def test_last_list():
    assert Lab6.last([x for x in range(10)]) == 9


def test_last_str():
    assert (Lab6.last("String")) == 'g'


def test_last_none():
    with pytest.raises(TypeError):
        Lab6.last(None)




