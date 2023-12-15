from collections import Counter
from enum import IntEnum

from utils import parse_challenge


def cmp(hand_1, hand_2):
    for i in range(5):
        if hand_1[i] != hand_2[i]:
            return strengths.index(hand_1[i]) > strengths.index(hand_2[i])


strengths = 'AKQJT98765432'[::-1]
types = '543210'


class HandType(IntEnum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


class Hand:
    def __init__(self, hand, bid=0):
        self.hand = hand
        self.bid = bid

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type == other.hand_type:
            return cmp(other.hand, self.hand)
        return False

    @property
    def hand_type(self):
        counts = sorted(Counter(self.hand).values(), reverse=True)
        if counts[0] == 5:
            return HandType.FIVE_OF_A_KIND
        if counts[0] == 4:
            return HandType.FOUR_OF_A_KIND
        if counts[0] == 3:
            if counts[1] == 2:
                return HandType.FULL_HOUSE
            else:
                return HandType.THREE_OF_A_KIND
        if counts[0] == 2:
            if counts[1] == 2:
                return HandType.TWO_PAIR
            else:
                return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    def __repr__(self):
        return f'Hand({self.hand}, {self.bid})'


def score(challenge):
    hands = [Hand(h, s) for h, s in map(str.split, challenge)]
    winnings = 0
    for i, h in enumerate(sorted(hands)):
        winnings += (1+i) * int(h.bid)
    return winnings


if __name__ == '__main__':
    challenge = parse_challenge(7)
    print("Part 1: ", score(challenge))
