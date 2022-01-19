from os import listdir
from turtle import width

import mss
import numpy as np
from cv2 import cv2

from .logger import logger
from .utils import *
from .config import Config


class Image:
    TARGETS = []
    MONITOR_LEFT = None
    MONITOR_TOP = None

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
            Image.MONITOR_LEFT = monitor["left"]
            Image.MONITOR_TOP = monitor["top"]
            return sct_img[:, :, :3]

    @staticmethod
    def get_target_positions(target:str):
        target_img = Image.TARGETS[target]
        screen_img = Image.screen()
        return cv2.matchTemplate(screen_img, target_img, cv2.TM_CCOEFF_NORMED)
    
    @staticmethod
    def get_one_target_position(target:str, threshold:float=0.8):
        threshold_config = Config.PROPERTIES["threshold"]["default"]
        if(threshold_config):
            threshold = threshold_config
            
        target_img = Image.TARGETS[target]
        screen_img = Image.screen()
        result = cv2.matchTemplate(screen_img, target_img, cv2.TM_CCOEFF_NORMED)

        if result.max() < threshold:
            raise Exception(f"{target} not found")
            
        yloc, xloc = np.where(result == result.max())
        xloc += Image.MONITOR_LEFT
        yloc += Image.MONITOR_TOP
        hight, width = target_img.shape[:2]
        
        return xloc[0], yloc[0], width, hight




