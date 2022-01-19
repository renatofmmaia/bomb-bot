import sys

import yaml

from module.bombScreen import BombScreen
from module.config import Config
from module.hero import Hero
from module.image import Image
from module.manager import create_bombcrypto_managers
from module.platform import Platform, PlatformEnum


def main(config_file):
    Config.load_config(config_file)
    Image.load_targets()

    bomb_crypto_managers = create_bombcrypto_managers()
    # while True:
    for manager in bomb_crypto_managers:
        with manager:
            print(manager.login_action())
        
        # with manager:
        #     print(manager.hero_check_work())


if __name__ == "__main__":
    config_file = "config_default"

    if len(sys.argv) > 1:
        config_file = sys.argv[1]

    config_file += ".yaml"
    main(config_file)
