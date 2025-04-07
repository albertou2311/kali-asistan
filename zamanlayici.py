import schedule
import time

def rapor_olustur():
    print("[+] Rapor oluşturuluyor...")
    time.sleep(2)
    print("[+] Rapor başarıyla oluşturuldu.")

def zamanla_gorev(func, delay):
    print(f"[+] Görev {delay} saniye sonra çalışacak...")
    time.sleep(delay)
    func()

