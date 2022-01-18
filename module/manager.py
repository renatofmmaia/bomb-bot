import time
from .bombScreen import BombScreen
from enum import Enum
from .window import get_windows
from .image import Image


def create_bombcrypto_managers():
    return [BombcryptoManager(w) for w in get_windows()]
    
class BombcryptoManager:
    def __init__(self, window) -> None:
        self.window = window
        self.login = 0
        self.heroes = 0
        self.new_map = 0
        self.print_coins = 0
        self.refresh_heroes = 0
        print(Image.TARGETS, "!!!")   

    def __enter__(self):
        self.window.activate()
        time.sleep(2)
        return self
    
    def __exit__(self, type, value, tb):
        return
    
    def identify_screen(self):
        print(BombScreen.get_currentScreen(self.image_targets))
        
