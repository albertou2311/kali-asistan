import logging
from komut_yoneticisi import sesli_cevap, sesli_komut_tanima, komut_al

# Loglama yapılandırması
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        komut = komut_al()
        if komut:
            from komut_yoneticisi import komut_tanima
            logging.info(f"Tanımlanan komut: {komut}")
            komut_tanima(komut)
        else:
            logging.warning("Hiçbir komut tanımlanamadı")
    except Exception as e:
        logging.error(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
