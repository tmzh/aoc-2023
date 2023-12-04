from utils import parse_challenge
import math
import re


def min_cubes(game):
    cubes = {'red': 0, 'green': 0, 'blue': 0}
    for count, color in re.findall(r'(\d+) (\w+)', game):
        cubes[color] = max(int(count), cubes[color])
    return math.prod(cubes.values())


def possible_games(games):
    return sum(min_cubes(game) for game in games)


def valid_game_ids(games):
    valid_games = 0
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    for game in games:
        game_id, draws = game.split(':')
        for draw in draws.split(';'):
            for colors in draw.split(','):
                count, color = colors.strip().split(' ')
                if int(count) > max_cubes[color]:
                    break
            else:
                continue
            break
        else:
            valid_games += int(game_id.rstrip().replace('Game ', ''))
    return valid_games


if __name__ == '__main__':
    games = parse_challenge(2)
    print("Part 1: ", valid_game_ids(games))
    print("Part 2:", possible_games(games))
