from collections import Counter
from enum import IntEnum

from utils import parse_challenge


class Hand:

    def __init__(self, hand: str, bid=0, part_2=False):
        self.hand = hand
        self.bid = bid
        # make face cards sortable
        if part_2:
            self.hand = hand.translate(str.maketrans('TJQKA', 'A0CDE'))
        else:
            self.hand = hand.translate(str.maketrans('TJQKA', 'ABCDE'))

    def value(self):
        best_hand = max(self.hand_value(self.hand.replace('0', r)) for r in self.hand)
        return [best_hand, self.hand, self.bid]

    def hand_value(self, hand):
        return sorted(map(hand.count, hand), reverse=True)

    def __repr__(self):
        return f'Hand({self.hand}, {self.bid})'


def score(challenge, part_2=False):
    hands = [Hand(h, s, part_2) for h, s in map(str.split, challenge)]
    winnings = 0
    for i, (h_type, hand, bid) in enumerate(sorted(h.value() for h in hands)):
        winnings += (1 + i) * int(bid)
    return winnings


if __name__ == '__main__':
    challenge = parse_challenge(7)
    print("Part 1: ", score(challenge))
    print("Part 2: ", score(challenge, part_2=True))
