numerals = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def calibration_value(text):
    nums = [int(v) for v in text if v.isnumeric()]
    return nums[0] * 10 + nums[-1]


def calibration_values_sum(lines):
    return sum(calibration_value(l) for l in lines)


def fix_nums(text):
    for t, n in numerals.items():
        text = text.replace(t, t + str(n) + t)
    return text


if __name__ == '__main__':
    lines = open('input.txt', 'r').read()
    print("Part 1: ", calibration_values_sum(lines.split()))
    corrected_lines = fix_nums(lines)
    print("Part 2: ", calibration_values_sum(corrected_lines.split()))
