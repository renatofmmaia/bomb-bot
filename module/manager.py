import time
from enum import Enum

from .bombScreen import BombScreen
from .hero import Hero
from .image import Image
from .logger import logger
from .window import get_windows


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
        login_attempts = 3
        logger("😿 Performing login action")

        # if login_attempts > 3:
        #     logger('🔃 Too many login attempts, refreshing')
        #     login_attempts = 0
        #     pyautogui.hotkey('ctrl','f5')
        #     return

        if BombScreen.click_if_image_found(
            Image.TARGETS["button_connect_wallet"],
            name="connectWalletBtn",
            timeout=10,
        ):
            logger("🎉 Connect wallet button detected.")
            login_attempts = login_attempts + 1

        if BombScreen.click_if_image_found(
            Image.TARGETS["button_connect_wallet_sign"],
            name="sign button",
            timeout=8,
        ):
            logger("🎉 Signin wallet button detected.")
            login_attempts = login_attempts + 1

        logger("🎉 Login successfully!")

    def hero_check_work():
        Hero.who_needs_work()
