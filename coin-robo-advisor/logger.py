import os
import logging
from logging.handlers import TimedRotatingFileHandler

LOG_DIR = './logs'
LOG_FILE_NAME = 'coin_robo_advisor.log'

if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] %(message)s")

fileHandler = TimedRotatingFileHandler(filename=f'{LOG_DIR}/{LOG_FILE_NAME}',
                                       when='midnight', interval=1, encoding='utf-8')
fileHandler.suffix = '%Y%m%d'
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
