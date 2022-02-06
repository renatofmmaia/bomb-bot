import sys
import time
from .config import Config
from enum import Enum

class LoggerEnum(Enum):
    ACTION = 0
    BUTTON_CLICK = 1
    PAGE_FOUND = 2
    TIMER_REFRESH = 3
    ERROR = 4
    

COLOR = {
    "blue": "\033[94m",
    "default": "\033[99m",
    "grey": "\033[90m",
    "yellow": "\033[93m",
    "black": "\033[90m",
    "cyan": "\033[96m",
    "green": "\033[92m",
    "magenta": "\033[95m",
    "white": "\033[97m",
    "red": "\033[91m",
}


def logger(message, color="default", force_log_file=False, terminal=True, datetime=True, end='\n'):
    color_formatted = COLOR.get(color.lower(), COLOR["default"])
    formatted_datetime = time.strftime(Config.get("generals", "time_format"), time.localtime())
    
    if datetime:
        formatted_message = "[{}] => {}".format(formatted_datetime, message)
    else:
        formatted_message = message
        
    formatted_message_colored = color_formatted + formatted_message + "\033[0m"
    
    if terminal:
        sys.stdout.write(color_formatted)
        sys.stdout.flush()
        print(formatted_message_colored, end=end)

    if Config.get('generals','save_log_file') or force_log_file:
        with open("./logs/logger.log", "a+", encoding='utf-8') as logger_file:
            logger_file.write(formatted_message + '\n')

def logger_translated(text: str, loggerEnum: LoggerEnum):
    if loggerEnum.value == LoggerEnum.ACTION.value:
        logger(f"🐧 Performing {text} action")
    elif loggerEnum.value == LoggerEnum.BUTTON_CLICK.value:
        logger(f"❎ Clicking in {text} button...")
    elif loggerEnum.value == LoggerEnum.PAGE_FOUND.value:
        logger(f"🚩 {text} page detected.")
    elif loggerEnum.value == LoggerEnum.TIMER_REFRESH.value:
        logger(f"🍺 Refresh {text}.")
    elif loggerEnum.value == LoggerEnum.ERROR.value:
        logger(f"🆘 {text}.")
    
def reset_log_file():
    file = open("./logs/logger.log","w")
    file.close()
    