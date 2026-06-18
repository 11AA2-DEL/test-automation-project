import logging
import os
from config import LOG_LEVEL, LOG_DIR
os.makedirs(LOG_DIR, exist_ok=True)
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    formatter = logging.Formatter('%(asctimes - %(name)s - %(levelname)s -%(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(LOG_LEVEL)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    fh =  logging.FileHandler(os.path.join(LOG_DIR, "test.log"),encoding = "utf-8")
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

