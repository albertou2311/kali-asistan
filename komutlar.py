import paramiko
import subprocess
import komutlar.komut_tanima
# import komutlar.komut_tanima  # Bu satırı kaldırabiliriz
from komutlar import komut_tanima
from .komutlar import apache_kapat, sistemi_guncelle, sistem_temizligi
import os

# komutlar/__init__.py dosyasını Python ile oluşturma
os.makedirs('komutlar', exist_ok=True)
with open('komutlar/__init__.py', 'w') as f:
    pass


def komut_tanima(komut):
    from islem_yoneticisi import komutu_isle
    komutu_isle(komut)
    
# ✅ Rapor yazma
def rapor_yaz(komut, detay):
    with open("rapor.txt", "a") as dosya:
        dosya.write(f"Komut: {komut}\n")
        dosya.write(f"Detaylar: {detay}\n")
        dosya.write("=====================================\n")
    print("📄 Rapor başarıyla kaydedildi.")


# ✅ Sistem Komutları
def apache_kapat():
    print("[!] Apache servisleri kapatılıyor...")
    os.system("sudo systemctl stop apache2")
    print("[✓] Apache kapatıldı.")

def sistem_temizligi():
    print("[!] Sistem temizliği başlatılıyor...")
    os.system("sudo apt-get clean")
    print("[✓] Sistem temizliği tamamlandı.")

def guvenlik_taramasi():
    print("Sistem güvenlik taraması başlatılıyor...")
    try:
        subprocess.run(["sudo", "lynis", "audit", "system"], check=True)
        print("Güvenlik taraması tamamlandı!")
        rapor_yaz("Sistem Güvenlik Taraması", "Sistem güvenlik taraması başarılı.")
    except subprocess.CalledProcessError as e:
        print(f"Hata oluştu: {e}")
        rapor_yaz("Sistem Güvenlik Taraması", str(e))

def sistemi_guncelle():
    print("Sistem güncelleniyor...")
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
        subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
        subprocess.run(["sudo", "dpkg", "--configure", "-a"], check=True)
        subprocess.run(["sudo", "apt", "clean"], check=True)
        print("Sistem başarıyla güncellendi!")
        rapor_yaz("Kali Linux Güncelleme", "Sistem başarıyla güncellendi.")
    except subprocess.CalledProcessError as e:
        print(f"Hata oluştu: {e}")
        rapor_yaz("Kali Linux Güncelleme", str(e))

def sistemi_yeniden_baslat():
    print("Sistem yeniden başlatılıyor...")
    try:
        subprocess.run(["sudo", "reboot"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Hata oluştu: {e}")
        rapor_yaz("Yeniden Başlatma", str(e))

def disk_temizligi():
    print("Disk temizliği yapılıyor...")
    try:
        subprocess.run(["sudo", "bleachbit", "--clean"], check=True)
        print("Disk temizliği tamamlandı!")
        rapor_yaz("Disk Temizliği", "Disk temizliği başarılı.")
    except subprocess.CalledProcessError as e:
        print(f"Hata oluştu: {e}")
        rapor_yaz("Disk Temizliği", str(e))

def sistem_saglik_kontrol():
    print("Sistem sağlık durumu kontrol ediliyor...")
    cpu = subprocess.getoutput("top -bn1 | grep 'Cpu(s)'")
    ram = subprocess.getoutput("free -h")
    disk = subprocess.getoutput("df -h")
    print(f"CPU: {cpu}\nRAM:\n{ram}\nDisk:\n{disk}")
    rapor_yaz("Sistem Sağlık Kontrolü", f"{cpu}\n{ram}\n{disk}")

def gereksiz_servisleri_kapat():
    print("Gereksiz servisler kapatılıyor...")
    try:
        subprocess.run(["sudo", "systemctl", "stop", "servis_adı"], check=True)
        subprocess.run(["sudo", "systemctl", "disable", "servis_adı"], check=True)
        print("Servisler kapatıldı.")
        rapor_yaz("Servis Kapatma", "Gereksiz servisler kapatıldı.")
    except subprocess.CalledProcessError as e:
        print(f"Hata oluştu: {e}")
        rapor_yaz("Servis Kapatma", str(e))


# ✅ Ağ Araçları ve Penetrasyon
def nmap_tarama(hedef_ip):
    print(f"{hedef_ip} için Nmap taraması yapılıyor...")
    sonuc = subprocess.getoutput(f"nmap {hedef_ip}")
    print(sonuc)
    rapor_yaz("Nmap Taraması", sonuc)

def ssh_baglantisi_ve_sniper_tarama(hedef_ip):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect("192.168.142.129", username="albertou", password="2311")
        print(f"Sniper taraması başlatılıyor: {hedef_ip}")
        stdin, stdout, stderr = client.exec_command(f"sniper -t {hedef_ip}")
        sonuc = stdout.read().decode()
        print(sonuc)
        rapor_yaz("Sniper Taraması", sonuc)
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        client.close()

def armitage_kullan(ip):
    print(f"Armtiage ile {ip} IP'sine sızılıyor...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect("192.168.142.129", username="albertou", password="2311")
        stdin, stdout, stderr = client.exec_command(f"armitage -t {ip}")
        sonuc = stdout.read().decode()
        print(sonuc)
        rapor_yaz("Armtiage", sonuc)
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        client.close()


# ✅ Sistem ve Ağ Ayarları
def ip_degistir():
    print("IP değiştiriliyor...")
    subprocess.run(["sudo", "service", "networking", "restart"])
    rapor_yaz("IP Değiştirme", "IP değiştirildi.")

def mac_degistir(interface):
    print(f"{interface} arayüzünün MAC adresi değiştiriliyor...")
    subprocess.run(["sudo", "macchanger", "-r", interface])
    rapor_yaz("MAC Değiştirme", f"{interface} MAC adresi değiştirildi.")

def guvenlik_duvari_kontrol():
    print("Güvenlik duvarı kontrol ediliyor...")
    durum = subprocess.getoutput("sudo ufw status")
    print(durum)
    rapor_yaz("Firewall Durumu", durum)


# ✅ Diğer
def vmware_baslat():
    print("VMware başlatılıyor...")
    rapor_yaz("VMware", "VMware başlatıldı.")

def kali_linux_baslat():
    print("Kali Linux başlatılıyor...")
    rapor_yaz("Kali Linux", "Kali Linux başlatıldı.")

def sistemi_kapat():
    print("Sistem kapatılıyor...")
    rapor_yaz("Sistem Kapatma", "Sistem başarıyla kapatıldı.")


# ✅ Ana Komut Tanıma
def komut_tanima(komut):
    komut = komut.lower()

    if "sniper" in komut:
        hedef_ip = input("Hedef IP: ")
        ssh_baglantisi_ve_sniper_tarama(hedef_ip)

    elif "armitage" in komut:
        ip = input("Hedef IP: ")
        armitage_kullan(ip)

    elif "nmap" in komut:
        hedef_ip = input("Hedef IP: ")
        nmap_tarama(hedef_ip)

    elif "apache kapat" in komut:
        apache_kapat()

    elif "sistem temizle" in komut:
        sistem_temizligi()

    elif "sistem güncelle" in komut:
        sistemi_guncelle()

    elif "disk temizle" in komut:
        disk_temizligi()

    elif "sistem saglik" in komut:
        sistem_saglik_kontrol()

    elif "servis kapat" in komut:
        gereksiz_servisleri_kapat()

    elif "ip degistir" in komut:
        ip_degistir()

    elif "mac degistir" in komut:
        arayuz = input("Arayüz: ")
        mac_degistir(arayuz)

    elif "firewall kontrol" in komut:
        guvenlik_duvari_kontrol()

    elif "sistem kapat" in komut:
        sistemi_kapat()

    elif "yeniden baslat" in komut:
        sistemi_yeniden_baslat()

    elif "kali linux" in komut:
        kali_linux_baslat()

    elif "vmware" in komut:
        vmware_baslat()
    
    else:
        print("❌ Komut tanınmadı.")


touch komutlar/__init__.py

