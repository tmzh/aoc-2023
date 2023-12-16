from collections import Counter
from enum import IntEnum

from utils import parse_challenge


def cmp(hand_1, hand_2, strengths):
    for i in range(5):
        if hand_1[i] != hand_2[i]:
            return strengths.index(hand_1[i]) > strengths.index(hand_2[i])


class HandType(IntEnum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


class Hand:
    strengths = 'AKQJT98765432'[::-1]
    strengths_2 = 'AKQT98765432J'[::-1]

    def __init__(self, hand, bid=0, part_2=False):
        self.hand = hand
        self.bid = bid
        self.part_2 = part_2

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type == other.hand_type:
            return cmp(other.hand, self.hand, self.strengths_2 if self.part_2 else self.strengths)
        return False

    @property
    def hand_type(self):
        hand = self.hand
        if self.part_2:
            if 'J' in self.hand:
                c = Counter(hand)
                if c.most_common()[0][0] == 'J':
                    if len(c) > 1:
                        top_card = c.most_common(2)[1][0]
                    else:
                        top_card = 'J'
                else:
                    top_card = c.most_common(1)[0][0]
                hand = self.hand.replace('J', top_card)

        match sorted(Counter(hand).values(), reverse=True):
            case [5]:
                return HandType.FIVE_OF_A_KIND
            case [4, 1]:
                return HandType.FOUR_OF_A_KIND
            case [3, 2]:
                return HandType.FULL_HOUSE
            case [3, 1, 1]:
                return HandType.THREE_OF_A_KIND
            case [2, 2, 1]:
                return HandType.TWO_PAIR
            case [2, 1, 1, 1]:
                return HandType.ONE_PAIR
            case _:
                return HandType.HIGH_CARD

    def __repr__(self):
        return f'Hand({self.hand}, {self.bid})'


def score(challenge, part_2=False):
    hands = [Hand(h, s, part_2) for h, s in map(str.split, challenge)]
    winnings = 0
    for i, h in enumerate(sorted(hands)):
        winnings += (1 + i) * int(h.bid)
    return winnings


if __name__ == '__main__':
    challenge = parse_challenge(7)
    print("Part 1: ", score(challenge))
    print("Part 2: ", score(challenge, part_2=True))
