# coding=utf-8
import os
from loguru import logger

class OceanLogger(object):
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path_info = os.path.join(BASE_DIR, 'log/websocket_info.log')
        file_path_error = os.path.join(BASE_DIR, 'log/websocket_error.log')
        file_path_debug = os.path.join(BASE_DIR, 'log/websocket_debug.log')
        # log_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <4}</level> | <level>{extra[request_id]}</level> |<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
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



# if __name__ == "__main__":
#     OceanLogger()
#     context_logger.error("error_messsage")
#     context_logger = context_logger.bind(request_id="request_id_2")
#     context_logger.info("info_messsage")
#     context_logger.debug("debug_messsage")
