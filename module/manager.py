import time
from enum import Enum

from .bombScreen import BombScreen, BombScreenEnum
from .hero import Hero
from .image import Image
from .logger import logger
from .window import get_windows
from .config import Config
from .utils import *


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
        logger("😿 Performing login action")
        
        login_attepmts = Config.PROPERTIES["screen"]["number_login_attempts"]
        
        logged = False
        for i in range(login_attepmts):
            
            if BombScreen.get_current_screen() != BombScreenEnum.LOGIN.value:
                refresh_page()
                
            logger("🎉 Login page detected.")

            logger("🎉 Clicking in wallet button...")
            if not BombScreen.click_if_image_found("button_connect_wallet"):
                refresh_page()
                continue
            
            logger("🎉 Clicking in sigin wallet button...")
            if not BombScreen.click_if_image_found("button_connect_wallet_sign", 10):
                refresh_page()
                continue
            
            if BombScreen.get_current_screen() != BombScreenEnum.HOME.value:
                logger("🎉 Failed to login, restart proccess...")
                continue
            else:    
                logger("🎉 Login successfully!")
                logged = True
                break
            
        return logged
       

    def hero_check_work():
        Hero.who_needs_work()
        return True
