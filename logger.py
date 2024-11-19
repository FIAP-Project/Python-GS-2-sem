import logging

# ANSI escape codes for colors
RESET = "\033[0m"
COLORS = {
    'DEBUG': "\033[96m",  # Cyan
    'INFO': "\033[97m",  # White
    'WARNING': "\033[93m",  # Yellow
    'ERROR': "\033[91m",  # Red
    'CRITICAL': "\033[91m",  # Red
}


class ColoredFormatter(logging.Formatter):

    def format(self, record):
        color = COLORS.get(record.levelname, RESET)
        message = super().format(record)
        return f"{color}{message}{RESET}"


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = ColoredFormatter(
    '[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

ch.setFormatter(formatter)
logger.addHandler(ch)
