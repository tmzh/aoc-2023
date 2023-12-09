import math
import re

from utils import parse_challenge

symbols_pattern = r'[^0-9\.]'
numbers_pattern = r'[0-9]+'


def spot_syms(line):
    pattern = re.compile(symbols_pattern)
    pos = set()
    for m in pattern.finditer(line):
        pos.add(m.span()[0])
    return pos


def spot_nums(line):
    pattern = re.compile(numbers_pattern)
    matches = {}
    for m in pattern.finditer(line):
        matches[int(m.group())] = set(range(m.span()[0] - 1, m.span()[1] + 1))
    return matches


def adjacent_numbers_sum(lines):
    return sum(sum(v) for v in adjacent_numbers(lines).values())


def two_part_product(lines):
    return sum(math.prod(v) for v in adjacent_numbers(lines).values() if len(v) == 2)


def adjacent_numbers(lines):
    sym_pos = {(r, c): [] for r in range(len(lines)) for c in range(len(lines[0])) if lines[r][c] not in '0123456789.'}

    for i, line in enumerate(lines):
        for m in re.finditer(r'\d+', line):
            borders = {(r, c) for r in (i - 1, i, i + 1) for c in range(m.start() - 1, m.end() + 1)}
            for border in borders & sym_pos.keys():
                sym_pos[border].append(int(m.group()))
    return sym_pos


if __name__ == '__main__':
    schematic = parse_challenge(3)
    print("Part 1: ", adjacent_numbers_sum(schematic))
    print("Part 2: ", two_part_product(schematic))
