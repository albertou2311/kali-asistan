
import subprocess
import os
from komut_yoneticisi import sesli_cevap, sesli_komut_tanima, komut_al
from goruntu_yuztanima import yuz_tanima_baslat
from rapor_olusturucu import rapor_olustur
from osint_tool import osint_aramasi
from email_gonderici import mail_gonder

def ekran_temizle():
    os.system('cls')  # Windows için
    # os.system('clear')  # Linux/MacOS için

def kali_linux_ac():
    konus("Kali Linux başlatılıyor.")
    subprocess.Popen(["vmrun", "-T", "ws", "start", "C:\\Kali\\Kali.vmx"])

def nmap_taramasi(ip_adresi):
    konus(f"{ip_adresi} adresine nmap taraması başlatılıyor.")
    os.system(f"gnome-terminal -- nmap -sV {ip_adresi}")

def osint_arama(kelime):
    konus(f"{kelime} için açık kaynak araması başlatılıyor.")
    os.system(f"gnome-terminal -- python3 osint_tool.py {kelime}")

def komutu_isle(komut):
    komut_islem = komut_tespit_et(komut)  # Komutu analiz et

    if "vmware" in komut:
        konus("VMware açılıyor.")
        subprocess.Popen(["C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe"])

    if komut_islem == "kali_linux_baslat":
        kali_linux_ac()
    elif komut_islem == "yuz_tanima_baslat":
        yuz_tanima_baslat()
    elif komut_islem == "rapor_olustur":
        rapor_olustur()
    elif komut_islem == "osint_aramasi":
        osint_aramasi()
    elif komut_islem == "mail_gonder":
        mail_gonder()
    elif komut_islem == "komut_anlasilmadi":
        konus("Komut anlaşılamadı. Lütfen tekrar deneyin.")
    elif "nmap tara" in komut:
        konus("Lütfen IP adresini söyleyin.")
        ip = sesli_komut_al()
        if ip:
            nmap_taramasi(ip)
            ekran_temizle()  # clear() yerine ekran_temizle() kullanılmalı
    elif "osint ara" in komut:
        konus("Lütfen aramak istediğiniz terimi söyleyin.")
        kelime = sesli_komut_al()
        if kelime:
            osint_arama(kelime)
    elif "çıkış yap" in komut:
        konus("Asistan kapatılıyor. Görüşmek üzere.")
        exit()
    else:
        konus("Bu komutu anlayamadım.")
