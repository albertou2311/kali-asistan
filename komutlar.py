
import paramiko
import subprocess

#Rapor yazma fonksiyonu
# komutlar.py içinde
def komut_tanima(komut):
    if "kali linux başlat" in komut:
        return "kali_linux_baslat"
    elif "yüz tanıma başlat" in komut:
        return "yuz_tanima_baslat"
    elif "rapor oluştur" in komut:
        return "rapor_olustur"
    elif "osint araması" in komut:
        return "osint_aramasi"
    elif "mail gönder" in komut:
        return "mail_gonder"
    else:
        return "komut_anlasilmadi"


def rapor_yaz(komut, detay):
    with open("rapor.txt", "a") as dosya:
        dosya.write(f"Komut: {komut}\n")
        dosya.write(f"Detaylar: {detay}\n")
        dosya.write("=====================================\n")
    print("Rapor başarıyla kaydedildi.")

# SSH bağlantısı ve sniper taraması yapan fonksiyon
def ssh_baglantisi_ve_sniper_tarama(hedef_ip="192.168.1.1"):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Anahtar doğrulamasını atla

    try:
        client.connect("192.168.142.129", username="albertou", password="2311")
        print(f"Sniper taraması başlatılıyor: {hedef_ip}")    
        stdin, stdout, stderr = client.exec_command(f"sniper -t {hedef_ip}")
        print(stdout.read().decode())  # Tarama sonucu çıktı
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        client.close()

# VMware başlatma fonksiyonu
def vmware_baslat():
    print("VMware başlatılıyor...")
    # VMware'i başlatacak komutları buraya ekleyebilirsin
    rapor_yaz("VMware başlatma", "VMware başarıyla başlatıldı.")

# Kali Linux başlatma fonksiyonu
def kali_linux_baslat():
    print("Kali Linux giriş başlatılıyor...")
    # Kali Linux başlatma işlemleri burada yapılabilir
    rapor_yaz("Kali Linux başlatma", "Kali Linux başarıyla başlatıldı.")

# Nmap taraması fonksiyonu
def nmap_tarama(hedef_ip):
    print(f"{hedef_ip} adresine Nmap taraması yapılıyor...")
    # Nmap komutunu çalıştıran fonksiyon
    # subprocess.run(["nmap", "192.168.1.1"]) gibi

# Sistemi kapatma fonksiyonu
def sistemi_kapat():
    print("Sistem kapatılıyor...")
    # Burada sistem kapama komutu yer alabilir
    # subprocess.run(["shutdown", "-h", "now"]) gibi bir komut kullanılabilir
    rapor_yaz("Sistemi kapatma", "Sistem başarıyla kapatıldı.")

# Komutları tanımlama fonksiyonu
def komut_tanima(komut):
    komut = komut.lower()  # Küçük harfe çevir, daha kolay karşılaştırma için

    # Komutlara göre uygun işlemleri çağır
    if "sniper" in komut and "tara" in komut:
        hedef_ip = "192.168.1.1"  # Bu hedef ipyi komutla değiştirebilirsin
        ssh_baglantisi_ve_sniper_tarama(hedef_ip)
    
    elif "vmware" in komut:
        vmware_baslat()

    elif "kali linux" in komut:
        kali_linux_baslat()

    elif "nmap tara" in komut:
        hedef_ip = "192.168.1.1"  # Hedef IP buradan alınabilir veya kullanıcıdan alınabilir
        nmap_tarama(hedef_ip)

    elif "sistemi kapat" in komut:
        sistemi_kapat()

    else:
        print("❌ Bu komut tanımlanamadı.")
