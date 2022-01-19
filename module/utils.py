import time
import pyautogui

from random import random ,uniform


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

def randomize(loc: float, width: float, safe_factor=0):
    """randomize a number between loc and width with a safe distance (safe_factor*width).

    Returns
    -------
    float
        random float
    """
    if safe_factor > 0.5:
        raise ValueError("safe_factor must be between 0 and 0.5")

    safe_dist = width * safe_factor
    min_value = loc + safe_dist
    max_value = loc + width - safe_dist
    
    return uniform(min_value, max_value)

def randomize_int(loc: float, width: float, safe_factor=0):
    """randomize a number between loc and width with a safe distance (safe_factor*width).

    Returns
    -------
    int
        random integer
    """
    return round(randomize(loc, width, safe_factor))

def refresh_page(delay:int = 5):
    pyautogui.hotkey('ctrl','f5')
    time.sleep(5)

