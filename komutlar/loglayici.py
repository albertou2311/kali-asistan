# loglayici.py
import logging
from datetime import datetime
import os

def log_konfiguru_et():
    tarih = datetime.now().strftime("%d-%m-%Y")
    log_dosyasi = f"logs/log_{tarih}.txt"
    os.makedirs("logs", exist_ok=True)
    
    logging.basicConfig(
        filename=log_dosyasi,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def logla(mesaj, seviye="info"):
    log_konfiguru_et()
    if seviye == "info":
        logging.info(mesaj)
    elif seviye == "warning":
        logging.warning(mesaj)
    elif seviye == "error":
        logging.error(mesaj)
