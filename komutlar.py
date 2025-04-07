import paramiko
import subprocess
import subprocess

# komutlar.py

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
        rapor_yaz("Sistem Güvenlik Taraması", f"Güvenlik taraması yapılırken hata oluştu: {e}")

def sistemi_guncelle():
    print("Sistem güncelleniyor...")
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
        subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
        subprocess.run(["sudo", "dpkg", "--configure", "-a"], check=True)
        subprocess.run(["sudo", "apt", "clean"], check=True)
        print("Sistem başarıyla güncellendi ve optimize edildi!")
        rapor_yaz("Kali Linux Güncelleme", "Sistem başarıyla güncellendi ve optimize edildi.")
    except subprocess.CalledProcessError as e:
        print(f"Hata oluştu: {e}")
        rapor_yaz("Kali Linux Güncelleme", f"Sistem güncellenirken hata oluştu: {e}")

def sistemi_yeniden_baslat():
    print("Sistem yeniden başlatılıyor...")
    try:
        subprocess.run(["sudo", "reboot"], check=True)
        print("Sistem başarıyla yeniden başlatıldı!")
        rapor_yaz("Kali Linux Yeniden Başlatma", "Sistem başarıyla yeniden başlatıldı.")
    except subprocess.CalledProcessError as e:
        print(f"Hata oluştu: {e}")
        rapor_yaz("Kali Linux Yeniden Başlatma", f"Sistem yeniden başlatılamadı: {e}")

def disk_temizligi():
    print("Disk temizliği yapılıyor...")
    try:
        subprocess.run(["sudo", "bleachbit", "--clean"], check=True)
        print("Disk temizliği tamamlandı!")
        rapor_yaz("Disk Temizliği", "Disk temizliği başarılı.")
    except subprocess.CalledProcessError as e:
        print(f"Hata oluştu: {e}")
        rapor_yaz("Disk Temizliği", f"Disk temizliği yapılırken hata oluştu: {e}")

def sistem_saglik_kontrolu():
    print("Sistem sağlık durumu kontrol ediliyor...")
    try:
        # RAM kullanımı
        ram_kullanimi = subprocess.check_output(["free", "-h"]).decode()
        # Disk kullanımı
        disk_kullanimi = subprocess.check_output(["df", "-h"]).decode()

        print("RAM Kullanımı:")
        print(ram_kullanimi)
        print("Disk Kullanımı:")
        print(disk_kullanimi)

        rapor_yaz("Sistem Sağlık Kontrolü", f"RAM Kullanımı:\n{ram_kullanimi}\nDisk Kullanımı:\n{disk_kullanimi}")
    except subprocess.CalledProcessError as e:
        print(f"Hata oluştu: {e}")
        rapor_yaz("Sistem Sağlık Kontrolü", f"Sistem sağlık durumu kontrol edilirken hata oluştu: {e}")

def gereksiz_servisleri_kapat():
    print("Gereksiz servisler kapatılıyor...")
    try:
        subprocess.run(["sudo", "systemctl", "stop", "servis_adı"], check=True)
        subprocess.run(["sudo", "systemctl", "disable", "servis_adı"], check=True)
        print("Gereksiz servisler kapatıldı!")
        rapor_yaz("Servis Kapatma", "Gereksiz servisler başarıyla kapatıldı.")
    except subprocess.CalledProcessError as e:
        print(f"Hata oluştu: {e}")
        rapor_yaz("Servis Kapatma", f"Servis kapatma işlemi sırasında hata oluştu: {e}")


# ✅ Rapor yazma
def rapor_yaz(komut, detay):
    with open("rapor.txt", "a") as dosya:
        dosya.write(f"Komut: {komut}\n")
        dosya.write(f"Detaylar: {detay}\n")
        dosya.write("=====================================\n")
    print("📄 Rapor başarıyla kaydedildi.")

# ✅ SSH bağlantısı ile sniper tarama
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
        print(f"Hata oluştu: {e}")
    finally:
        client.close()

# ✅ Armtiage kullanma fonksiyonu
def armitage_kullan(ip):
    print(f"Armtiage ile {ip} IP'sine sızılıyor...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect("192.168.142.129", username="albertou", password="2311")
        print("Armtiage başlatılıyor...")
        stdin, stdout, stderr = client.exec_command(f"armitage -t {ip}")
        sonuc = stdout.read().decode()  # Armtiage çıktısı
        print(sonuc)
        rapor_yaz("Armtiage Kullanma", sonuc)  # Rapor kaydediliyor
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        client.close()

# ✅ Diğer fonksiyonlar
def vmware_baslat():
    print("VMware başlatılıyor...")
    rapor_yaz("VMware başlatma", "VMware başarıyla başlatıldı.")

def kali_linux_baslat():
    print("Kali Linux başlatılıyor...")
    rapor_yaz("Kali Linux başlatma", "Kali Linux başarıyla başlatıldı.")

def nmap_tarama(hedef_ip):
    print(f"{hedef_ip} için Nmap taraması yapılıyor...")
    sonuc = subprocess.getoutput(f"nmap {hedef_ip}")
    print(sonuc)
    rapor_yaz("Nmap Taraması", sonuc)

def sistemi_kapat():
    print("Sistem kapatılıyor...")
    rapor_yaz("Sistem kapatma", "Sistem başarıyla kapatıldı.")

# ✅ IP Değiştirme (Proxy veya VPN)
def ip_degistir():
    print("IP değiştiriliyor...")
    subprocess.run(["sudo", "service", "networking", "restart"])  # Örnek olarak, ağ yeniden başlatma
    rapor_yaz("IP Değiştirme", "IP başarıyla değiştirildi.")

# ✅ MAC Adresi Değiştirme
def mac_degistir(interface):
    print(f"{interface} arayüzünün MAC adresi değiştiriliyor...")
    subprocess.run(["sudo", "macchanger", "-r", interface])
    rapor_yaz("MAC Değiştirme", f"{interface} arayüzünün MAC adresi başarıyla değiştirildi.")

# ✅ Sistem Sağlık Kontrolü
def sistem_saglik_kontrol():
    print("Sistem sağlık kontrolü yapılıyor...")
    cpu_kullanimi = subprocess.getoutput("top -bn1 | grep 'Cpu(s)'")
    ram_kullanimi = subprocess.getoutput("free -h")
    disk_kullanimi = subprocess.getoutput("df -h")
    print(f"CPU Kullanımı: {cpu_kullanimi}\nRAM Kullanımı: {ram_kullanimi}\nDisk Kullanımı: {disk_kullanimi}")
    rapor_yaz("Sistem Sağlık Kontrolü", f"CPU Kullanımı: {cpu_kullanimi}\nRAM Kullanımı: {ram_kullanimi}\nDisk Kullanımı: {disk_kullanimi}")

# ✅ Güvenlik Duvarı Kontrolü ve Ayarlama
def guvenlik_duvari_kontrol():
    print("Güvenlik duvarı durumu kontrol ediliyor...")
    firewall_durumu = subprocess.getoutput("sudo ufw status")
    print(f"Firewall Durumu: {firewall_durumu}")
    rapor_yaz("Güvenlik Duvarı Kontrolü", firewall_durumu)

# ✅ Komut tanıma
def komut_tanima(komut):
    komut = komut.lower()
    
    if "sniper" in komut and "tara" in komut:
        hedef_ip = input("Hedef IP: ")
        ssh_baglantisi_ve_sniper_tarama(hedef_ip)

    elif "vmware" in komut:
        vmware_baslat()

    elif "kali linux" in komut:
        kali_linux_baslat()

    elif "nmap tara" in komut:
        hedef_ip = input("Nmap için hedef IP: ")
        nmap_tarama(hedef_ip)

    elif "sistemi kapat" in komut:
        sistemi_kapat()

    elif "rapor oluştur" in komut:
        rapor_yaz("Rapor oluştur", "Kullanıcı manuel olarak rapor istedi.")

    elif "zafiyet tara" in komut:
        from exploit_taramasi import zafiyet_tara
        ip = input("Zafiyet taraması için IP: ")
        zafiyet_tara(ip)

    elif "exploit dene" in komut:
        from exploit_taramasi import main
        main()

    elif "armitage kullan" in komut:
        ip = input("Armtiage ile sızmak için hedef IP girin: ")
        armitage_kullan(ip)

    elif "ip degistir" in komut:
        ip_degistir()

    elif "mac degistir" in komut:
        interface = input("MAC adresi değiştirilecek arayüz (örneğin eth0): ")
        mac_degistir(interface)

    elif "sistem saglik kontrol" in komut:
        sistem_saglik_kontrol()

    elif "guvenlik duvari kontrol" in komut:
        guvenlik_duvari_kontrol()

    else:
        print("❌ Bu komut tanınmadı.")
