from .bombScreen import BombScreen, BombScreenEnum
from .config import Config
from .logger import logger
from .mouse import *

class Login:
    
    def do_login():
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
            
            if BombScreen.wait_for_screen(BombScreenEnum.HOME.value) != BombScreenEnum.HOME.value:
                logger("🎉 Failed to login, restart proccess...")
                continue
            else:    
                logger("🎉 Login successfully!")
                logged = True
                break
            
        return logged