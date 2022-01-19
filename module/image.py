from os import listdir
from turtle import width

import mss
import numpy as np
from cv2 import cv2

from .logger import logger
from .utils import *


class Image:
    TARGETS = []

    @staticmethod
    def load_targets():
        path = "assets/images/targets/"
        file_names = listdir(path)

        targets = {}
        for file in file_names:
            targets[replace(file, ".png")] = cv2.imread(path + file)

        Image.TARGETS = targets

    @staticmethod
    def screen():
        with mss.mss() as sct:
            monitor = sct.monitors[0]
            sct_img = np.array(sct.grab(monitor))
            return sct_img[:, :, :3]

    @staticmethod
    def get_target_positions(target:str):
        target_img = Image.TARGETS[target]
        screen_img = Image.print_screen()
        return cv2.matchTemplate(screen_img, target_img, cv2.TM_CCOEFF_NORMED)
    
    @staticmethod
    def get_one_target_position(target:str, threshold:float=0.8):
        target_img = Image.TARGETS[target]
        screen_img = Image.print_screen()
        result = cv2.matchTemplate(screen_img, target_img, cv2.TM_CCOEFF_NORMED)

        if result.max() < threshold:
            raise Exception(f"{target} not found")
            
        width, hight = target.shape[:2]
        yloc, xloc = np.argmax(result)
        return xloc, yloc, width, hight




