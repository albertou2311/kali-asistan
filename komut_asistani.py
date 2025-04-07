import os
import subprocess
import paramiko
import logging

logging.basicConfig(level=logging.DEBUG)

def ssh_baglantisi():
    host = '192.168.142.129'  # Kali IP adresi
    port = 22
    username = 'albertou'
    password = '2311'  # Kali şifresi
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        logging.info("🔗 SSH bağlantısı kuruluyor...")
        client.connect(host, port=port, username=username, password=password)
        logging.info("✅ SSH bağlantısı kuruldu.")

        komut = "nmap -sV 192.168.142.129"  # hedef IP'yi buraya yerleştirin
        logging.info("📡 Komut çalıştırılıyor: %s", komut)
        
        stdin, stdout, stderr = client.exec_command(komut)
        logging.info("📥 Çıktı:")
        for satir in stdout:
            logging.info(satir.strip())
        
        logging.info("⚠️ Hatalar (varsa):")
        for satir in stderr:
            logging.error(satir.strip())

    except Exception as e:
        logging.error(f"❌ Hata oluştu: {e}")
    finally:
        client.close()
        logging.info("🔒 Bağlantı kapatıldı.")

if __name__ == "__main__":
    ssh_baglantisi()
