#### Запуск doctest
```
python -m doctest -o NORMALIZE_WHITESPACE -v morse.py
```

#### Результат doctest
```
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('sos') # doctest: +ELLIPSIS
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: 's'
ok
2 items had no tests:
    morse
    morse.decode
1 items passed all tests:
   2 tests in morse.encode
2 tests in 3 items.
2 passed and 0 failed.
Test passed.
```

#### Запуск pytest
```
pytest morse.py
```
#### Результат pytest
```
========================================================================================================= test session starts =========================================================================================================
platform win32 -- Python 3.8.6, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\Pavel\PycharmProjects\pythonProject1\lab3
plugins: Faker-6.6.0
collected 3 items                                                                                                                                                                                                                      

morse.py ...                                                                                                                                                                                                                     [100%]

========================================================================================================== 3 passed in 0.11s ==========================================================================================================
```

