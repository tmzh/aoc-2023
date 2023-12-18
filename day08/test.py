from unittest import TestCase

from day08.main import *
from utils import parse_challenge, matches_to_list


class Test(TestCase):
    sample_input = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''

    def test_count_steps(self):
        lines = parse_challenge(self.sample_input)
        instruction = lines[0]
        lookup = build_lookup(lines[2:])
        self.assertEqual(count_steps(instruction, lookup), 2)

    def test_count_multi_paths(self):
        lines = parse_challenge('''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, 22C)
22A = (22B, 22Z)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)''')
        instruction = lines[0]
        lookup = build_lookup(lines[2:])
        self.assertEqual(count_multi_paths(instruction, lookup), 6)

    def test_build_lookup(self):
        lines = parse_challenge(self.sample_input)
        self.assertEqual(build_lookup(lines[2:]), {'AAA': ['BBB', 'CCC'],
                                                   'BBB': ['DDD', 'EEE'],
                                                   'CCC': ['ZZZ', 'GGG'],
                                                   'DDD': ['DDD', 'DDD'],
                                                   'EEE': ['EEE', 'EEE'],
                                                   'GGG': ['GGG', 'GGG'],
                                                   'ZZZ': ['ZZZ', 'ZZZ']})
