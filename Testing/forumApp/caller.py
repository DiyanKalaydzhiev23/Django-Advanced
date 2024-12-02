from unittest import TestCase


def sum_two_numbers(num1, num2):
    return num1 + num2


class TestMyFunc(TestCase):
    def test_sum_two_numbers_valid(self):
        result = sum_two_numbers(5, 4)
        expected = 9

        self.assertEqual(result, expected)
