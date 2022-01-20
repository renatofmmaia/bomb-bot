import time
from enum import Enum

from .bombScreen import BombScreen, BombScreenEnum
from .hero import Hero
from .image import Image
from .login import Login
from .logger import logger
from .window import get_windows
from .config import Config
from .utils import *
from .mouse import *


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

    def __enter__(self):
        self.window.activate()
        time.sleep(2)
        return self

    def __exit__(self, type, value, tb):
        return

    def identify_screen(self):
        print(BombScreen.get_currentScreen(self.image_targets))

    def login_action(self):
        return Login.do_login()
       

    def hero_check_work(self):
        Hero.who_needs_work()
        return True
    
    def hero_refresh_hunt(self):
        return Hero.refresh_hunt()
