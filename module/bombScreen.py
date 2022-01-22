from enum import Enum


from cv2 import cv2

from .config import Config
from .image import Image
from .logger import LoggerEnum, logger, logger_translated
from .mouse import *
from .utils import *
from .telegram import TelegramBot


class BombScreenEnum(Enum):
    NOT_FOUND = -1
    LOGIN = 0
    HOME = 1
    HEROES = 2
    TREASURE_HUNT = 3
    TREASURE_HUNT_CHEST = 4


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
            BombScreenEnum.TREASURE_HUNT_CHEST.value: Image.TARGETS["identify_hunt_chest"],
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
            
    def do_print_chest(manager):
        logger_translated("print chest", LoggerEnum.ACTION)
        
        if BombScreen.get_current_screen() != BombScreenEnum.TREASURE_HUNT.value:
            BombScreen.go_to_treasure_hunt(manager)
        
        click_when_target_appears("button_hunt_chest")
        BombScreen.wait_for_screen(BombScreenEnum.TREASURE_HUNT_CHEST.value)
        image = None

        if Config.get("screen", "print_full_screen"):
            image = Image.print_full_screen("chest")
        else:
            image = Image.print_partial_screen("chest", "chest_screen_for_geometry")

        TelegramBot.send_message_with_image(image, "Se liga no farm desse bot, é muito BCOIN! :D")
        click_when_target_appears("buttun_x_close")
            
        manager.set_print_chest_refreshed()


class Login:
    def do_login(manager):
        logger_translated("login", LoggerEnum.ACTION)

        login_attepmts = Config.PROPERTIES["screen"]["number_login_attempts"]

        logged = False
        for i in range(login_attepmts):
            current_screen = BombScreen.get_current_screen()
            logger(f"💫 Bot inicializado em: {BombScreenEnum(current_screen).name}")
            
            if BombScreen.get_current_screen() != BombScreenEnum.LOGIN.value:
                refresh_page()
                BombScreen.wait_for_screen(BombScreenEnum.LOGIN.value)

            logger_translated("Login", LoggerEnum.PAGE_FOUND)

            logger_translated("wallet", LoggerEnum.BUTTON_CLICK)
            if not click_when_target_appears("button_connect_wallet"):
                refresh_page()
                continue

            logger_translated("sigin wallet", LoggerEnum.BUTTON_CLICK)
            if not click_when_target_appears("button_connect_wallet_sign"):
                refresh_page()
                continue

            if (BombScreen.wait_for_screen(BombScreenEnum.HOME.value)!= BombScreenEnum.HOME.value):
                logger("🚫 Failed to login, restart proccess...")
                continue
            else:
                logger("🎉 Login successfully!")
                logged = True
                break

        manager.set_logged(logged)
        return logged


class Hero:
    def who_needs_work(manager):
        logger_translated(f"heroes to work(config: {Config.get('hero','work_mod')})", LoggerEnum.ACTION)

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
            repeat=Config.get('screen','scroll_how_mutch_try_move_down'),
            function_between=click_betwenn_scrolls
        )
        logger(f"🏃 {sum(n_clicks_per_scrool)} new heros sent to explode everything 💣💣💣.")
        Hero.refresh_hunt(manager)
        manager.set_heroes_refreshed()
        return True

    def refresh_hunt(manager):
        logger_translated("huting positions", LoggerEnum.TIMER_REFRESH)

        BombScreen.go_to_home(manager)
        BombScreen.go_to_treasure_hunt(manager)

        manager.set_positions_refreshed()
        return True
