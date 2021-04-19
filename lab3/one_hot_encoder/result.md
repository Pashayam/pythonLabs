#### Запуск unittest
```
python -m unittest -v test_one_hot_encoder.py
```
#### Результат unittest
```
test_cities_with_copy (test_one_hot_encoder.TestTF) ... ok
test_cities_without_copy (test_one_hot_encoder.TestTF) ... ok
test_exception (test_one_hot_encoder.TestTF) ... ok
test_not_london (test_one_hot_encoder.TestTF) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

#### Запуск pytest
```
pytest pytest_one_hot_encoder.py
```
#### Результат pytest
```
========================================================================================================= test session starts =========================================================================================================
platform win32 -- Python 3.8.6, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\Pavel\PycharmProjects\pythonProject1\lab3
plugins: Faker-6.6.0
collected 4 items                                                                                                                                                                                                                      

pytest_one_hot_encoder.py ....                                                                                                                                                                                                   [100%]

========================================================================================================== 4 passed in 0.09s ==========================================================================================================
```
