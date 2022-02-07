import sys
import traceback
from time import sleep

import requests
from packaging import version

from module.bombScreen import BombScreen, BombScreenEnum
from module.config import Config
from module.image import Image
from module.logger import logger, reset_log_file
from module.manager import create_bombcrypto_managers
from module.telegram import TelegramBot

__version__ = "0.0.2"


def main(config_file):
    try:
        # Load configs
        Config.load_config(config_file)
        Image.load_targets()
        TelegramBot.load_config()
        
        if Config.get("generals", "reset_log_file"):
            reset_log_file()

        r = requests.get(
            "https://api.github.com/gists/715eabaa3bca5ca70709a6397b806e86"
        )
        if r.ok:
            data = r.json()

            start_message = data["files"]["start_message"]["content"]
            logger(start_message, color="cyan", datetime=False)

            last_version = data["files"]["version"]["content"].strip()
            version_installed = version.parse(__version__)
            logger(f"-> Current version: {version_installed}", color="cyan", datetime=False)

            if version.parse(last_version) > version.parse(__version__):
                logger("-----------------------------------------------", color="green", datetime=False)
                logger(f"New version available: {last_version}.", color="green", datetime=False)
                update_message = data["files"]["update_message"]["content"]
                logger(update_message, color="green", datetime=False)
                logger("-----------------------------------------------", color="green", datetime=False)
        else:
            logger("Unable to check for updates.")

        bomb_crypto_managers = create_bombcrypto_managers()
        logger(f"{len(bomb_crypto_managers)} Bombcrypto window (s) found")
        bomb_browser_count = 1
        show_initial_screen_message = True
        while True:
            try:
                for manager in bomb_crypto_managers:
                    current_screen = BombScreen.get_current_screen()
                    
                    if show_initial_screen_message:
                        logger(f"💫 Bombcrypto window[{bomb_browser_count}] inicializado em: {BombScreenEnum(current_screen).name}")
                    
                    with manager:
                        manager.do_what_needs_to_be_done(current_screen)
                    
                    if bomb_browser_count == len(bomb_crypto_managers):
                        bomb_browser_count = 1
                        show_initial_screen_message = False
                    else:
                        bomb_browser_count += 1
            except Exception as e:
                logger(
                    traceback.format_exc(),
                    color="red",
                    force_log_file=True,
                    terminal=False,
                )
                logger(
                    f"😬 Ohh no! A error has occurred in the last action.\n{e}\n Check the log  file for more details.",
                    color="yellow",
                )
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
