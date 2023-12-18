from utils import parse_challenge, matches_to_list


def history(line, step=1):
    values = [*map(int, line.split())][::step]
    result = []
    while values:
        result.append(values[-1])
        values = [curr - prev for prev, curr in zip(values, values[1:])]
    return result


def extrapolate(values):
    return sum(values)


def part_1(lines):
    return sum(sum(history(l)) for l in lines)


def part_2(lines):
    return sum(sum(history(l, step=-1)) for l in lines)


assert history('10 13 16 21  30  45') == [45, 15, 6, 2, 0, 0]
assert history('1 3 6 10 15 21') == [21, 6, 1, 0, 0, 0]

assert sum(history('10 13  16  21  30  45')) == 68
assert sum(history('1   3   6  10  15  21')) == 28
assert sum(history('0   3   6   9  12  15')) == 18

assert part_1('''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.splitlines()) == 114

if __name__ == '__main__':
    challenge = parse_challenge(9)
    print("Part 1: ", part_1(challenge))
    print("Part 2: ", part_2(challenge))
