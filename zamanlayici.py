import schedule
import time

def rapor_olustur():
    print("Port taraması raporu oluşturuluyor...")

# Her gün saat 10'da rapor oluştur
schedule.every().day.at("10:00").do(rapor_olustur)

while True:
    schedule.run_pending()
    time.sleep(1)
