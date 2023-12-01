def calibration_value(text):
    nums = [int(v) for v in text if v.isnumeric()]
    return nums[0] * 10 + nums[-1]


def calibration_values_sum(lines):
    return sum(calibration_value(l) for l in lines)
