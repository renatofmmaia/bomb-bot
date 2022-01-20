from .logger import logger
from .login import Login
from .config import Config
from .bombScreen import BombScreen, BombScreenEnum
from .mouse import *
from .image import Image
import pyautogui

class Hero:

    def who_needs_work():
        logger(f"😿 Performing heroes to work action, using config(hero_work_mod): {Config.get('hero_work_mod')}.")
        
        for i in range(5):
            move_to("hero_bar_vertical")
            click_on_multiple_targets("button_work_unchecked", not_click="button_work_checked", filter_func=Image.filter_by_green_bar)            
            pyautogui.dragRel(0,-200,duration=2, button='left',tween=pyautogui.easeOutQuad)
            time.sleep(1)
            logger(i)
            
            if i == 4:
                click_on_multiple_targets("button_work_unchecked", not_click="button_work_checked", filter_func=Image.filter_by_green_bar)
    
    
        
    def refresh_hunt():
        logger("😿 Performing Refresh huting positions action")
        
        current_screen = BombScreen.get_current_screen()
        logger(f"🎉 {BombScreenEnum(current_screen).name} page detected.")
        
        if current_screen == BombScreenEnum.TREASURE_HUNT.value:
            click_when_target_appears("button_back")
            BombScreen.wait_for_screen(BombScreenEnum.HOME.value)
            click_when_target_appears("identify_home")
            
        elif current_screen == BombScreenEnum.HOME.value:
            click_when_target_appears("identify_home")
            
        elif current_screen == BombScreenEnum.HEROES.value:
            click_when_target_appears("buttun_x_close")
            BombScreen.wait_for_screen(BombScreenEnum.HOME.value)
            click_when_target_appears("identify_home")
            
        elif current_screen == BombScreenEnum.LOGIN.value:
            Login.do_login()
            click_when_target_appears("identify_home")
            
        else:
            Login.do_login()
            click_when_target_appears("identify_home")
        
        logger("🎉 Refresh huting positions success!")
        return True
            
