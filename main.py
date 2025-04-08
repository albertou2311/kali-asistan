import time
from komut_yoneticisi import komut_al
from islem_yoneticisi import komutu_isle
import komutlar
import zamanlayici
import guvenlik
from loglayici import logla
from zamanlayici import zamanla_gorev
from exploit_taramasi import exploit_ara
from taramaci import hedef_tara, hedef_bilgi_topla
from komutlar import komut_tanima, sistem_temizligi

def sistem_baslangic_islemleri():
    print("[+] Başlangıç işlemleri çalıştırılıyor...")
    komut = komutlar.komut_tanima("kali aç ve ip taraması yap")
    if komut:
        print("[✓] Komut doğru şekilde alındı.")
    else:
        print("[!] Komut alınamadı.")
    zamanlayici.rapor_olustur()
    guvenlik.guvenlik_uyarisi()
    print("[+] Başlangıç işlemleri tamamlandı.")

def zafiyet_taramasi_baslat():
    ip = input("Zafiyet taraması yapılacak IP adresini girin: ")
    sonuc = zafiyet_tara(ip)
    if sonuc:
        print("[✓] Zafiyet taraması tamamlandı.")
    else:
        print("[-] Zafiyet taraması yapılamadı.")

def tarama_baslat():
    ip = input("Lütfen taranacak IP adresini girin: ")
    acik_portlar = hedef_tara(ip)
    print(f"[!] {ip} adresindeki açık portlar: {acik_portlar}")

def bilgi_toplama_baslat():
    ip = input("Bilgi toplanacak IP adresini girin: ")
    rapor = hedef_bilgi_topla(ip)
    if rapor:
        print("[+] Bilgi toplama tamamlandı. Rapor hazır.")
    else:
        print("[-] Bilgi toplanamadı.")

def main():
    sistem_baslangic_islemleri()  # Başlangıç işlemlerini çalıştır.
    try:
        while True:
            komut = komut_al()  # Kullanıcıdan komut al.
            if komut:
                komutu_isle(komut)  # Komutu çalıştır.
            time.sleep(1)  # Sistemi çok yormamak için bekleme
    except KeyboardInterrupt:
        print("\n[-] Asistan manuel olarak durduruldu.")

if __name__ == "__main__":
    main()  # Programı başlat
