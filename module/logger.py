import sys
import time
from .config import Config

# stream = open("./config.yaml", 'r')
# c = yaml.safe_load(stream)

last_log_is_progress = False

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


def logger(message, color="default", force_log_file=False):
    # global last_log_is_progress
    color_formatted = COLOR.get(color.lower(), COLOR["default"])

    formatted_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    formatted_message = "[{}] => {}".format(formatted_datetime, message)
    formatted_message_colored = color_formatted + formatted_message + "\033[0m"

    sys.stdout.write(color_formatted + ".")
    sys.stdout.flush()

    # if last_log_is_progress:
    #     sys.stdout.write("\n")
    #     sys.stdout.flush()
    #     last_log_is_progress = False

    print(formatted_message_colored)

    if Config.get('generals','save_log_file') or force_log_file:
        logger_file = open("./logs/logger.log", "a+", encoding='utf-8')
        logger_file.write(formatted_message + '\n')
        logger_file.close()

    return True
