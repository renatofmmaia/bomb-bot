from .logger import logger
from .config import Config

class Hero:

    def who_needs_work():
        logger("🏢 Searching heroes to work, using config(hero_work_mod): " + Config.PROPERTIES["hero_work_mod"])
