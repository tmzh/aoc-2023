import math

from utils import parse_challenge, matches_to_list


def trial(total, press) -> int:
    return (total - press) * press


def get_races(lines):
    durations = matches_to_list(lines[0], r'\d+', int)
    distances = matches_to_list(lines[1], r'\d+', int)
    return durations, distances


def part_1(lines):
    return math.prod(map(count_winning_ways, *get_races(lines)))


def part_2(lines):
    duration = int(lines[0].split(':')[1].replace(' ', ''))
    distance = int(lines[1].split(':')[1].replace(' ', ''))
    return count_winning_ways(duration, distance)


def count_winning_ways(duration, distance) -> int:
    for i in range(duration // 2):
        if trial(duration, i) > distance:
            return 2 * (duration / 2 - i) + 1


if __name__ == '__main__':
    challenge = parse_challenge(6)
    print("Part 1: ", part_1(challenge))
    print("Part 2: ", part_2(challenge))
