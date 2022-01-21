import time

from .bombScreen import BombScreen, Hero, Login
from .logger import logger
from .mouse import *
from .utils import *
from .window import get_windows


def create_bombcrypto_managers():
    return [BombcryptoManager(w) for w in get_windows()]


class BombcryptoManager:
    def __init__(self, window) -> None:
        self.window = window
        self.refresh_login = 0
        self.heroes_check = 0
        self.refresh_hunt = 0
        self.print_coins = 0

    def __enter__(self):
        self.window.activate()
        time.sleep(2)
        return self

    def __exit__(self, type, value, tb):
        return

    def identify_screen(self):
        print(BombScreen.get_currentScreen(self.image_targets))

    def do_what_needs_to_be_done(self):       
        if time.time() - self.heroes_check >  30*60:
            Hero.who_needs_work()
            self.heroes_check = time.time()
            self.refresh_heroes = time.time()

        if time.time() - self.refresh_hunt > 5*60:
            Hero.refresh_hunt()
            self.refresh_hunt = time.time()

        if time.time() - self.refresh_login > 30*60:
            Login.do_login()
            self.refresh_login = time.time()
        
        return True
    
    def hero_refresh_hunt(self):
        return Hero.refresh_hunt()
