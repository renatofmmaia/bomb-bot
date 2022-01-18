import yaml
import sys
from module.platform import Platform, PlatformEnum
from module.manager import create_bombcrypto_managers
from module.hero import Hero
from module.image import Image

def main(config_file):
    with open(config_file, 'r') as stream:  
        config = yaml.safe_load(stream)
    
    Image.load_targets()
    print(Image.TARGETS, '<<')
    bomb_crypto_managers = create_bombcrypto_managers()
    print(bomb_crypto_managers)
    
    # while True:
    #     for manager in bomb_crypto_managers:
    #          with manager:
                 
                 
    
if __name__ == "__main__":
    config_file = "config_default"
    
    if len(sys.argv) > 1:
        config_file = sys.argv[1]

    config_file += ".yaml"
    main(config_file)