# loglayici.py
import logging

def logla(mesaj, seviye="info"):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    if seviye == "info":
        logger.info(mesaj)
    elif seviye == "warning":
        logger.warning(mesaj)
    elif seviye == "error":
        logger.error(mesaj)
