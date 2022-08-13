# coding=utf-8
import os
from loguru import logger

class OceanLogger(object):
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path_info = os.path.join(BASE_DIR, 'log/monitor_info.log')
        file_path_error = os.path.join(BASE_DIR, 'log/monitor_error.log')
        file_path_debug = os.path.join(BASE_DIR, 'log/monitor_debug.log')

        logger.add(
            file_path_debug,
            encoding='utf-8',
            level="DEBUG",
            rotation="00:00",
            backtrace=True,
            diagnose=True)

        logger.add(
            file_path_info,
            encoding='utf-8',
            level="INFO",
            rotation="00:00",
            backtrace=True,
            diagnose=True)

        logger.add(
            file_path_error,
            encoding='utf-8',
            level='ERROR',
            rotation="00:00",
            backtrace=True,
            diagnose=True)
