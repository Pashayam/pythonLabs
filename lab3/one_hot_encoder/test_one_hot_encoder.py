import unittest
import one_hot_encoder


class TestTF(unittest.TestCase):

    def test_cities_with_copy(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = one_hot_encoder.fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_cities_without_copy(self):
        cities = ['Moscow', 'New York', 'Moscow']
        actual = one_hot_encoder.fit_transform(cities)
        expected = [
            ('Moscow', [0, 1]),
            ('New York', [1, 0]),
            ('Moscow', [0, 1]),
        ]
        self.assertEqual(actual, expected)

    def test_not_london(self):
        cities = ['Moscow', 'New York']
        actual = one_hot_encoder.fit_transform(cities)
        self.assertNotIn(('London', [1, 0]), actual)

    def test_exception(self):
        with self.assertRaises(Exception):
            one_hot_encoder.fit_transform(342)


if __name__ == '__main__':
    unittest.main()