import sys
import traceback
from time import sleep

from module.config import Config
from module.image import Image
from module.manager import create_bombcrypto_managers
from module.logger import logger, reset_log_file
from module.telegram import TelegramBot


def main(config_file):
    try:
        # Load configs
        Config.load_config(config_file)
        Image.load_targets()
        TelegramBot.load_config()
        
        if Config.get('generals','reset_log_file'):
            reset_log_file()

        bomb_crypto_managers = create_bombcrypto_managers()
        logger(f"{len(bomb_crypto_managers)} Bombcrypto window (s) found")
        while True:
            try:
                for manager in bomb_crypto_managers:
                    with manager:
                        manager.do_what_needs_to_be_done()
            except Exception as e:
                logger(traceback.format_exc(), color="red", force_log_file=True, terminal=False)
                logger("😬 Ohh no! A error has occurred in the last action. Check the log  file.", color="yellow")
                
            sleep(5)
    except Exception:
        logger(traceback.format_exc(), color="red", force_log_file=True, terminal=False)
        logger("😬 Ohh no! We couldn't start the bot.", color="red")
    
        

if __name__ == "__main__":
    config_path = "config.yaml"

    if len(sys.argv) > 1:
        config_file = sys.argv[1]
        config_path = f"config_profiles/{config_file}.yaml"

             
    main(config_path)
