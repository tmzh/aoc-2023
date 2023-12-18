import math

from utils import parse_challenge, matches_to_list
from itertools import cycle


def build_lookup(lines):
    return {
        source: target
        for source, *target in
        [
            matches_to_list(line, r'\w{3}', parser=str) for line in lines
        ]}


def count_steps(instruction, lookup, start='AAA'):
    count = 0
    for inst in cycle(instruction):
        count += 1
        pos = 'LR'.index(inst)
        start = lookup[start][pos]
        if start.endswith('Z'):
            return count


def count_multi_paths(instruction, lookup):
    starts = [k for k in lookup.keys() if k.endswith('A')]
    counts = [count_steps(instruction, lookup, start=start) for start in starts]
    return math.lcm(*counts)


if __name__ == '__main__':
    challenge = parse_challenge(8)
    instructions = challenge[0]
    lookups = build_lookup(challenge[2:])
    print('Part 1: ', count_steps(instructions, lookups))
    print('Part 2: ', count_multi_paths(instructions, lookups))
