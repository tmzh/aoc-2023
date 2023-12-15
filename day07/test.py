from unittest import TestCase

from day07.main import Hand, HandType, score
from utils import parse_challenge


class TestHand(TestCase):
    sample_input = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

    def test_hand_cmp(self):
        self.assertGreater(Hand('QQQJA', None), Hand('T55J5', None))

    def test_hand_type(self):
        self.assertEqual(Hand('QQQJA').hand_type, HandType.THREE_OF_A_KIND )
        self.assertEqual(Hand('KK677').hand_type, HandType.TWO_PAIR)

    def test_score(self):
        lines = parse_challenge(self.sample_input)
        self.assertEqual(score(lines), 6440)

