import subprocess
import os
from komut_yoneticisi import sesli_cevap, sesli_komut_tanima, komut_al
from komutlar import komut_tanima, rapor_yaz, ssh_baglantisi_ve_sniper_tarama
from goruntu_yuztanima import yuz_tanima_baslat
from rapor_olusturucu import rapor_olustur
from osint_tool import osint_aramasi
from email_gonderici import mail_gonder

def ekran_temizle():
    os.system('cls')  # Windows için
    # os.system('clear')  # Linux/MacOS için

def kali_linux_ac():
    sesli_cevap("Kali Linux başlatılıyor.")
    subprocess.Popen(["vmrun", "-T", "ws", "start", "C:\\Kali\\Kali.vmx"])

def nmap_taramasi(ip_adresi):
    sesli_cevap(f"{ip_adresi} adresine nmap taraması başlatılıyor.")
    os.system(f"gnome-terminal -- nmap -sV {ip_adresi}")

def osint_arama(kelime):
    sesli_cevap(f"{kelime} için açık kaynak araması başlatılıyor.")
    os.system(f"gnome-terminal -- python3 osint_tool.py {kelime}")

def komutu_isle(komut):
    komut_islem = komut_tanima(komut)  # Komutu analiz et

    if "vmware" in komut:
        sesli_cevap("VMware açılıyor.")
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
        sesli_cevap("Komut anlaşılamadı. Lütfen tekrar deneyin.")
    elif "nmap tara" in komut:
        sesli_cevap("Lütfen IP adresini söyleyin.")
        ip = sesli_komut_tanima()  # Sesli komut al
        if ip:
            nmap_taramasi(ip)
            ekran_temizle()  # clear() yerine ekran_temizle() kullanılmalı
    elif "osint ara" in komut:
        sesli_cevap("Lütfen aramak istediğiniz terimi söyleyin.")
        kelime = sesli_komut_tanima()  # Sesli komut al
        if kelime:
            osint_arama(kelime)
    elif "çıkış yap" in komut:
        sesli_cevap("Asistan kapatılıyor. Görüşmek üzere.")
        exit()
    else:
        sesli_cevap("Bu komutu anlayamadım.")

def komut_sec():
    komut = komut_al()  # Sesli veya yazılı komut seçimi
    if komut:
        komutu_isle(komut)
