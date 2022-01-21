import time

from .bombScreen import BombScreen, Hero, Login
from .logger import logger
from .mouse import *
from .utils import *
from .window import get_windows
from .config import Config


def create_bombcrypto_managers():
    return [BombcryptoManager(w) for w in get_windows()]


class BombcryptoManager:
    def __init__(self, window) -> None:
        self.window = window
        self.refresh_login = Config.get('refresh_login')*60
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
        check_heroes=Config.get('check_heroes')*60
        if check_heroes and now() - self.heroes_check > check_heroes:
            Hero.who_needs_work(self)

        refresh_hunt = Config.get('refresh_hunt')*60
        if refresh_hunt and now() - self.refresh_hunt > refresh_hunt:
            Hero.refresh_hunt(self)

        refresh_login = Config.get('refresh_login')*60
        if refresh_login and now() - self.refresh_login > refresh_login:
            Login.do_login(self)
        
        return True
    
    def needs_to_send_heroes_to_work(self):
        value = Config.get('check_heroes')
        time_passed = time.time() - self.heroes_check >  value*60
        return value and time_passed

    def heros_needs_to_be_refreshed(self):
        value = Config.get('check_heroes')
        time_passed = time.time() - self.heroes_check >  value*60
        return value and time_passed
    
    def heros_needs_to_be_refreshed(self):
        value = Config.get('check_heroes')
        time_passed = time.time() - self.heroes_check >  value*60
        return value and time_passed

    def set_logged(self, logged):
        self.logged = logged
        if logged:
            self.refresh_login = time.time()

    def set_treasure_hunt_refreshed(self):
        self.refresh_hunt = time.time()
    
    def set_positions_refreshed(self):
        self.heroes_check = time.time()

