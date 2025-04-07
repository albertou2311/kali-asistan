
import time
from komut_yoneticisi import komut_al
from islem_yoneticisi import komutu_isle
import komutlar
import zamanlayici
import guvenlik

def sistem_baslangic_islemleri():
    print("[+] Başlangıç işlemleri çalıştırılıyor...")
    komutlar.komut_tanima("kali aç ve ip taraması yap")
    zamanlayici.rapor_olustur()
    guvenlik.guvenlik_uyarisi()
    print("[+] Başlangıç işlemleri tamamlandı.")

def main():
    sistem_baslangic_islemleri()
    try:
        while True:
            komut = komut_al()
            if komut:
                komutu_isle(komut)
            time.sleep(1)  # Sistemi çok yormamak için bekleme
    except KeyboardInterrupt:
        print("\n[-] Asistan manuel olarak durduruldu.")

if __name__ == "__main__":
    main()
