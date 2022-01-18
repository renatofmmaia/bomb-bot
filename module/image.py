from os import listdir

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
