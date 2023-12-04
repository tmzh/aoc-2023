from unittest import TestCase
from day03.main import *


class Test(TestCase):
    sample_input = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.splitlines()

    def test_adjacent_numbers(self):
        self.assertEquals(adjacent_numbers_sum(self.sample_input), 4361)

    def test_adjacent_numbers(self):
        self.assertEquals(two_part_product(self.sample_input), 467835)
