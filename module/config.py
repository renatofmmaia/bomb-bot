import yaml


class Config:
    PROPERTIES = {}

    @staticmethod
    def load_config(config_file):
        with open(config_file, "r") as stream:
            Config.PROPERTIES = yaml.safe_load(stream)
