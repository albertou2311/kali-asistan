# komutlar/komutlar.py
import paramiko
import subprocess
from .komut_tanima import fonksiyon

def apache_kapat():
    subprocess.run(["systemctl", "stop", "apache2"], check=True)

def sistemi_guncelle():
    subprocess.run(["apt-get", "update"], check=True)
    subprocess.run(["apt-get", "upgrade", "-y"], check=True)

def sistem_temizligi():
    subprocess.run(["apt-get", "autoremove", "-y"], check=True)
    subprocess.run(["apt-get", "clean"], check=True)
