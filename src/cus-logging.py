import logging

LOG_LEVEL = logging.DEBUG

logging.basicConfig(level=LOG_LEVEL, format='%(asctime)-15s %(filename)s/%(funcName)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
