# The following code is adapted from https://github.com/norvig/pytudes
import os
import requests
import re
from typing import Callable, Union

lines = str.splitlines
paras = lambda t: t.split("\n\n")


def preview_challenge(text):
    items = text.splitlines()
    print(f"Puzzle input: {len(items)}")
    for i in range(5):
        print(items[i])


def parse_challenge(text_or_day: Union[str, int], parser: Callable = str, sections: Callable = lines):
    text = retrieve_challenge(text_or_day)
    preview_challenge(text)
    records = tuple(map(parser, sections(text.rstrip())))
    return records


def retrieve_challenge(text_or_day):
    if isinstance(text_or_day, int):
        if not os.path.exists('input.txt'):
            download(text_or_day)
        text = open('input.txt', 'r').read()
    else:
        text = text_or_day
    return text


def download(day):
    cookie = os.environ['AOC_COOKIE']
    session = requests.Session()
    requests.utils.add_dict_to_cookiejar(session.cookies, {'session': cookie})
    response = session.get(f"https://adventofcode.com/2023/day/{day}/input")
    if response.status_code == 200:
        with open('input.txt', 'wb') as f:
            f.write(response.content)
        print('File downloaded successfully.')
    else:
        print('Error occurred while downloading the file.')
        exit(1)


def natural_range(start, end):
    if not end:
        return range(start + 1)
    else:
        return range(start + 1, end + 1)


def matches_to_list(text, parser: Callable = int):
    return set(parser(x.group(0)) for x in re.finditer(r'\d+', text))
