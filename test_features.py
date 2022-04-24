import sys
from module.manager import create_bombcrypto_managers
from module.config import Config

def main(config_file):

	Config.load_config(config_file)
	bomb_crypto_managers = create_bombcrypto_managers()
	for manager in bomb_crypto_managers:
		if manager.window.account:
			print(manager.window.account)
		else:
			print("sem account")


if __name__ == "__main__":
    config_path = "config.yaml"

    if len(sys.argv) > 1:
        config_file = sys.argv[1]
        config_path = f"config_profiles/{config_file}.yaml"

    main(config_path)