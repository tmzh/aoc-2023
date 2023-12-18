import math
import re

from utils import parse_challenge, matches_to_list


def calculate_points(lines):
    points = {}
    for line in lines:
        card, winning, our_num = re.fullmatch(r'^Card\s+(\d+): (.*)\|(.*)$', line).groups()
        card = int(card)
        winning = set(matches_to_list(winning, r'\d+'))
        our_num = set(matches_to_list(our_num, r'\d+'))
        points[card] = len(winning & our_num)
    return points


def part_1(p):
    return sum(math.pow(2, v - 1) for v in p.values() if v)


def part_2(points):
    def f(i):
        if i > len(points):
            return 0
        elif not points[i]:
            return 1
        return 1 + sum(f(i + v) for v in range(1, points[i] + 1))
    return sum(f(i) for i in points.list_endpoints())


if __name__ == '__main__':
    challenge = parse_challenge(4)
    points = calculate_points(challenge)
    print('Part 1: ', part_1(points))
    print('Part 2: ', part_2(points))
