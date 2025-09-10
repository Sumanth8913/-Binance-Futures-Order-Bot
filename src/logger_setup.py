import logging, logging.handlers, os

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'bot.log')

def get_logger(name='binance_bot'):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    fmt = '%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(message)s'
    formatter = logging.Formatter(fmt)

    fh = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=3)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
