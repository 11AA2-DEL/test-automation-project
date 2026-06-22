#
import logging
import os
from config import LOG_LEVEL, LOG_DIR
os.makedirs(LOG_DIR, exist_ok=True)
def get_logger(name): #创建一个日志器
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    #配置日志格式：时间、模块名、级别、消息
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler() #输出到终端
    ch.setLevel(LOG_LEVEL)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    fh =  logging.FileHandler(os.path.join(LOG_DIR, "test.log"),encoding = "utf-8")  #输出到文件
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

