from unittest import TestCase

from day06.main import *


class Test(TestCase):
    sample_input = '''Time:      7  15   30
Distance:  9  40  200'''

    def test_press(self):
        total = 7
        for press, expected in zip(range(8), [0, 6, 10, 12, 12, 10, 6, 0]):
            self.assertEquals(trial(total, press), expected)

    def test_count_winning_ways(self):
        self.assertEqual(4, count_winning_ways(7, 9))
        self.assertEqual(8, count_winning_ways(15, 40))
        self.assertEqual(9, count_winning_ways(30, 200))

    def test_get_races(self):
        lines = parse_challenge(self.sample_input)
        self.assertEqual(([7, 15, 30], [9, 40, 200]), get_races(lines))

    def test_part_1(self):
        lines = parse_challenge(self.sample_input)
        self.assertEqual(288, part_1(lines))

    def test_part_1(self):
        lines = parse_challenge(self.sample_input)
        self.assertEqual(71503, part_2(lines))
