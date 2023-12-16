from unittest import TestCase

from day07.main import Hand, score
from utils import parse_challenge


class TestHand(TestCase):
    sample_input = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

    def test_hand_cmp(self):
        self.assertGreater(Hand('QQQJA', None).value(), Hand('T55J5', None).value())

    def test_score(self):
        lines = parse_challenge(self.sample_input)
        self.assertEqual(score(lines), 6440)

    def test_score_2(self):
        lines = parse_challenge(self.sample_input)
        self.assertEqual(score(lines, True), 5905)
