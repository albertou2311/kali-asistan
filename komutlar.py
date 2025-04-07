# komutlar.py
import paramiko
import subprocess

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

    else:
        print("❌ Bu komut tanınmadı.")
