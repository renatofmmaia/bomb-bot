from enum import Enum


from cv2 import cv2

from .config import Config
from .image import Image
from .logger import logger
from .mouse import *
from .utils import *


class BombScreenEnum(Enum):
    NOT_FOUND = -1
    LOGIN = 0
    HOME = 1
    HEROES = 2
    TREASURE_HUNT = 3


class BombScreen:

    def wait_for_screen(
        bombScreenEnum, time_beteween: float = 0.5, timeout: float = 60
    ):
        def check_screen():
            screen = BombScreen.get_current_screen()
            if screen == bombScreenEnum:
                return True
            else:
                return None

        return do_with_timeout(
            check_screen, time_beteween=time_beteween, timeout=timeout
        )

    def get_current_screen(time_beteween: float = 0.5, timeout: float = 20):
        targets = {
            BombScreenEnum.HOME.value: Image.TARGETS["identify_home"],
            BombScreenEnum.HEROES.value: Image.TARGETS["identify_heroes"],
            BombScreenEnum.LOGIN.value: Image.TARGETS["identify_login"],
            BombScreenEnum.TREASURE_HUNT.value: Image.TARGETS["identify_treasure_hunt"],
        }
        max_value = 0
        img = Image.screen()
        screen_name = -1

        for name, target_img in targets.items():
            result = cv2.matchTemplate(img, target_img, cv2.TM_CCOEFF_NORMED)
            max_value_local = result.max()
            if max_value_local > max_value:
                max_value = max_value_local
                screen_name = name

        return screen_name if max_value > Config.get("threshold", "default") else -1

    def go_to_home(manager):
        current_screen = BombScreen.get_current_screen()
        if current_screen == BombScreenEnum.HOME.value:
            return
        elif current_screen == BombScreenEnum.TREASURE_HUNT.value:
            click_when_target_appears("button_back")
        elif current_screen == BombScreenEnum.HEROES.value:
            click_when_target_appears("buttun_x_close")
        else:
            Login.do_login(manager)
            return

        BombScreen.wait_for_screen(BombScreenEnum.HOME.value)

    def go_to_heroes(manager):
        if BombScreen.get_current_screen() == BombScreenEnum.HEROES.value:
            return
        else:
            BombScreen.go_to_home(manager)
            click_when_target_appears("button_heroes")
            BombScreen.wait_for_screen(BombScreenEnum.HOME.value)

    def go_to_treasure_hunt(manager):
        if BombScreen.get_current_screen() == BombScreenEnum.TREASURE_HUNT.value:
            return
        else:
            BombScreen.go_to_home(manager)
            click_when_target_appears("identify_home")
            BombScreen.wait_for_screen(BombScreenEnum.HOME.value)


class Login:
    def do_login(manager):
        logger("😿 Performing login action")

        login_attepmts = Config.PROPERTIES["screen"]["number_login_attempts"]

        logged = False
        for i in range(login_attepmts):

            if BombScreen.get_current_screen() != BombScreenEnum.LOGIN.value:
                refresh_page()
                BombScreen.wait_for_screen(BombScreenEnum.LOGIN.value)

            logger("🎉 Login page detected.")

            logger("🎉 Clicking in wallet button...")
            if not click_when_target_appears("button_connect_wallet"):
                refresh_page()
                continue

            logger("🎉 Clicking in sigin wallet button...")
            if not click_when_target_appears("button_connect_wallet_sign"):
                refresh_page()
                continue

            if (BombScreen.wait_for_screen(BombScreenEnum.HOME.value)!= BombScreenEnum.HOME.value):
                logger("🎉 Failed to login, restart proccess...")
                continue
            else:
                logger("🎉 Login successfully!")
                logged = True
                break

        manager.set_logged(logged)
        return logged


class Hero:
    def who_needs_work(manager):
        logger(
            f"😿 Performing heroes to work action, using config: {Config.get('hero_work_mod')}."
        )
        BombScreen.go_to_home(manager)
        BombScreen.go_to_heroes(manager)
        def click_betwenn_scrolls():
            return click_on_multiple_targets(
                            "button_work_unchecked",
                            not_click="button_work_checked",
                            filter_func=Image.filter_by_green_bar,
                        )
        n_clicks_per_scrool = scroll_and_click_on_targets(
            safe_scroll_target="hero_bar_vertical",
            repeat=5,
            function_between=click_betwenn_scrolls
        )
        logger(f"🏃 {sum(n_clicks_per_scrool)} heros sent to explode everything 💣💣💣.")
        Hero.refresh_hunt(manager)
        manager.set_heroes_refreshed()
        return True

    def refresh_hunt(manager):
        logger("😿 Performing Refresh huting positions action")

        BombScreen.go_to_home(manager)
        BombScreen.go_to_treasure_hunt(manager)

        manager.set_positions_refreshed()
        logger("🎉 Refresh huting positions success!")
        return True
