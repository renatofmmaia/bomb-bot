from cv2 import cv2
from os import listdir
from .utils import *

class Image:
    TARGETS = []
    
    @staticmethod
    def check_image_on_screen(target, threshold,img = None):            
        result = cv2.matchTemplate(img,target,cv2.TM_CCOEFF_NORMED)
        w = target.shape[1]
        h = target.shape[0]

        yloc, xloc = np.where(result >= threshold)
        
        rectangles = []
        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), int(w), int(h)])
            rectangles.append([int(x), int(y), int(w), int(h)])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        return rectangles
    
    @staticmethod
    def load_targets():
        path = 'assets/images/targets/'
        file_names = listdir(path)
        
        targets = {}
        for file in file_names:
            targets[replace(file, '.png')] = cv2.imread(path + file)

        Image.TARGETS = targets
