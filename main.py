import sys

import yaml

from module.bombScreen import BombScreen
from module.hero import Hero
from module.image import Image
from module.manager import create_bombcrypto_managers
from module.platform import Platform, PlatformEnum
from module.config import Config


def main(config_file):
    Config.load_config(config_file)
    Image.load_targets()
   
    # print(Image.TARGETS, '<<')

    # print(bomb_crypto_managers)
    # BombScreen.get_current_screen(Image.TARGETS)

    bomb_crypto_managers = create_bombcrypto_managers()
    # while True:
    for manager in bomb_crypto_managers:
        with manager:
            manager.login_action()


if __name__ == "__main__":
    config_file = "config_default"

    if len(sys.argv) > 1:
        config_file = sys.argv[1]

    config_file += ".yaml"
    main(config_file)
