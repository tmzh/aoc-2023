from unittest import TestCase

from day01.main import *


class Test(TestCase):
    def test_calibration_value(self):
        test_cases = [
            ('1abc2', 12),
            ('pqr3stu8vwx', 38),
            ('a1b2c3d4e5f', 15),
            ('treb7uchet', 77),
        ]

        for given, expected in test_cases:
            self.assertEquals(calibration_value(given), expected)

    def test_calibration_values_sum(self):
        lines = ['1abc2',
                 'qr3stu8vwx',
                 'a1b2c3d4e5f',
                 'treb7uchet']
        self.assertEquals(calibration_values_sum(lines), 142)

