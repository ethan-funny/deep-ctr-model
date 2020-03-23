import sys
import logging
from colorlog import ColoredFormatter


def _getlogger():
    LOGFORMAT = "%(log_color)s[%(levelname)s %(asctime)s @%(filename)s:%(lineno)d]%(reset)s %(message)s"
    formatter = ColoredFormatter(LOGFORMAT)

    logger = logging.getLogger('deep-ctr-model')

    logger.propagate = False
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = _getlogger()
