import sys
from time import sleep

from module.config import Config
from module.image import Image
from module.manager import create_bombcrypto_managers
from module.logger import logger


def main(config_file):
    Config.load_config(config_file)
    Image.load_targets()

    bomb_crypto_managers = create_bombcrypto_managers()
    logger(f"{len(bomb_crypto_managers)} Bombcrypto window (s)  found")
    while True:
        for manager in bomb_crypto_managers:
            with manager:
                manager.do_what_needs_to_be_done()

        sleep(5)



if __name__ == "__main__":
    config_file = "config_default"

    if len(sys.argv) > 1:
        config_file = sys.argv[1]

    config_file += ".yaml"
    main(config_file)
