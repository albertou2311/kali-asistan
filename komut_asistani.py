
import os
import subprocess
import subprocess
import paramiko

def ssh_baglantisi():
    host = '192.168.142.129'  # Kali IP adresi (örnek, senin Kali IP'ni gir)
    port = 22
    username = 'Albertou'
    password = '2311' # Kali şifresi ( örnek şifre senin şifreni gir )
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print("🔗 SSH bağlantısı kuruluyor...")
        client.connect(host, port=port, username=username, password=password)
        print("✅ SSH bağlantısı kuruldu.")

        komut = "nmap -sV 192.168.1.1"  # örnek komut
        stdin, stdout, stderr = client.exec_command(komut)

        print("📡 Komut çalıştırılıyor: ", komut)
        print("📥 Çıktı:")
        for satir in stdout:
            print(satir.strip())
        
        print("⚠️ Hatalar (varsa):")
        for satir in stderr:
            print(satir.strip())

    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
    finally:
        client.close()
        print("🔒 Bağlantı kapatıldı.")

if __name__ == "__main__":
    ssh_baglantisi()
