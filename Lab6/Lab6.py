from collections.abc import Iterable


def ilen(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    count = 0
    for _ in iterable:
        count += 1
    return count


def flatten(iterable: Iterable):
    """
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """
    for x in iterable:
        if isinstance(x, Iterable):
            yield from flatten(x)
        else:
            yield x


def distinct(iterable: Iterable):
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    no_duplicates = set()
    for x in iterable:
        if x not in no_duplicates:
            no_duplicates.add(x)
            yield x


def groupby(key, iterable: Iterable):
    """
    >>> users = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21},
    ]
    >>> groupby('gender', users)
    {
        'female': [
            {'gender': 'female', 'age': 23},
            {'gender': 'female', 'age': 21},
        ],
        'male': [{'gender': 'male', 'age': 20}],
    }
    # Или так:
    >>> groupby('age', users)
    """
    out_dict = {}
    for x in iterable:
        if x[key] not in out_dict:
            out_dict[x[key]] = []
        out_dict[x[key]].append(x)

    return out_dict


def chunks(size: int, iterable: Iterable):
    """
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 2), (3, 4, )]
    """
    for i in range(0, ilen(iterable), size):
        yield tuple(iterable[i:i + size])


def first(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> first(range(0))
    None
    """
    return next(iter(iterable), None)


def last(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> last(range(0))
    None
    """
    last_element = None
    for i in iterable:
        last_element = i
    return last_element


