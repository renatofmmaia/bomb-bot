from cv2 import cv2
from enum import Enum

class BombScreenEnum(Enum):
    LOGIN = 1
    HOME = 1
    HEROES = 1
    TREASURE_HUNT = 1
    
class BombScreen():
    
    @staticmethod
    def get_currentScreen():
        print(BombScreenEnum.LOGIN)
        
    def login():
        pass
    
    def home():
        pass
    
    def heroes():
        pass

    def treasure_hunt():
        pass
    
    