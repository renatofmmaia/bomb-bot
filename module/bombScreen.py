import time
from enum import Enum

import mss
import numpy as np
import PIL.Image
import pyautogui
from cv2 import cv2

from .config import Config
from .image import Image
from .logger import logger
from .utils import *


class BombScreenEnum(Enum):
    LOGIN = 0
    HOME = 1
    HEROES = 2
    TREASURE_HUNT = 3


class BombScreen:
    def print_screen():
        with mss.mss() as sct:
            monitor = sct.monitors[0]
            sct_img = np.array(sct.grab(monitor))
            # The screen part to capture
            # monitor = {"top": 160, "left": 160, "width": 1000, "height": 135}
            # PIL.Image.fromarray(sct_img).show()
            # Grab the data
            return sct_img[:, :, :3]

    def click_image_randomness(x, y, t):
        with mss.mss() as sct:
            monitor = sct.monitors[0]
            x += monitor["left"]
            y += monitor["top"]

        pyautogui.moveTo(
            randomness_number(x, 10), randomness_number(y, 10), t + random() / 2
        )

    def get_current_screen():
        targets = {
            BombScreenEnum.HOME.value: Image.TARGETS["identify_home"],
            BombScreenEnum.HEROES.value: Image.TARGETS["identify_heroes"],
            BombScreenEnum.LOGIN.value: Image.TARGETS["identify_login"],
            BombScreenEnum.TREASURE_HUNT.value: Image.TARGETS["identify_treasure_hunt"],
        }
        max_value = 0
        img = BombScreen.print_screen()
        screen_name = None

        for name, target_img in targets.items():
            result = cv2.matchTemplate(img, target_img, cv2.TM_CCOEFF_NORMED)
            max_value_local = result.max()
            if max_value_local > max_value:
                max_value = max_value_local
                screen_name = name

        # print(f"you are in {screen_name}")
        return screen_name

    def check_image_on_screen(target, img=None):
        threshold = Config.PROPERTIES["threshold"]["default"]
        result = cv2.matchTemplate(img, target, cv2.TM_CCOEFF_NORMED)
        w = target.shape[1]
        h = target.shape[0]

        yloc, xloc = np.where(result >= threshold)

        rectangles = []
        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), int(w), int(h)])
            rectangles.append([int(x), int(y), int(w), int(h)])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        return rectangles

    def target_image_positions(target, img=None):
        threshold = Config.PROPERTIES["threshold"]["default"]

        if img is None:
            img = BombScreen.print_screen()

        result = cv2.matchTemplate(img, target, cv2.TM_CCOEFF_NORMED)
        w = target.shape[1]
        h = target.shape[0]

        yloc, xloc = np.where(result >= threshold)

        rectangles = []
        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), int(w), int(h)])
            rectangles.append([int(x), int(y), int(w), int(h)])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        return rectangles

    def click_if_image_found(img, name=None, timeout=3):
        logger(None, progress_indicator=True)
        start = time.time()

        while True:
            matches = BombScreen.target_image_positions(img)
            if len(matches) == 0:
                hast_timed_out = time.time() - start > timeout
                if hast_timed_out:
                    if not name is None:
                        pass

                    return False

                continue

            x, y, w, h = matches[0]
            pos_click_x = x + w / 2
            pos_click_y = y + h / 2

            BombScreen.click_image_randomness(pos_click_x, pos_click_y, 1)
            pyautogui.click()
            return True

    def login():
        pass

    def home():
        pass

    def heroes():
        pass

    def treasure_hunt():
        pass
