import time
from random import random


def date_formatted(format="%Y-%m-%d %H:%M:%S"):
    return time.strftime(format, time.localtime())


def replace(string, strReplace):
    if strReplace and string.endswith(strReplace):
        return string[: -len(strReplace)]
    return string


def randomness_number(n, randomn_factor_size=None):
    if randomn_factor_size is None:
        randomness_percentage = 0.1
        randomn_factor_size = randomness_percentage * n

    random_factor = 2 * random() * randomn_factor_size
    if random_factor > 5:
        random_factor = 5
    without_average_random_factor = n - randomn_factor_size
    randomized_n = int(without_average_random_factor + random_factor)

    return int(randomized_n)
