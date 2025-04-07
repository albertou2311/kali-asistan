import pyttsx3
import speech_recognition as sr
import komutlar
from komutlar import *
from taramaci import hedef_tara, hedef_bilgi_topla
from exploit_taramasi import zafiyet_tara
import os

def komutu_isle(komut):
    if "bilgi topla" in komut:
        bilgi_toplama_baslat()
    elif "port tara" in komut or "ip tara" in komut:
        tarama_baslat()
    elif "zafiyet tara" in komut:
        zafiyet_taramasi_baslat()
    elif "çık" in komut or "kapat" in komut:
        print("[!] Sistem kapatılıyor...")
        exit()
    elif "başlangıç" in komut:
        sistem_baslangic_islemleri()
    else:
        print("[-] Tanınmayan komut:", komut)

def bilgi_toplama_baslat():
    ip = input("Bilgi toplanacak IP adresini girin: ")
    rapor = hedef_bilgi_topla(ip)
    if rapor:
        print("[+] Bilgi toplama tamamlandı. Rapor hazır.")
    else:
        print("[-] Bilgi toplanamadı.")

def tarama_baslat():
    ip = input("Lütfen taranacak IP adresini girin: ")
    acik_portlar = hedef_tara(ip)
    print(f"[!] {ip} adresindeki açık portlar: {acik_portlar}")

def zafiyet_taramasi_baslat():
    ip = input("Zafiyet taraması yapılacak IP adresini girin: ")
    sonuc = zafiyet_tara(ip)
    if sonuc:
        print("[✓] Zafiyet taraması tamamlandı.")
    else:
        print("[-] Zafiyet taraması yapılamadı.")

def sistem_baslangic_islemleri():
    print("[+] Başlangıç işlemleri çalıştırılıyor...")
    komutlar.komut_tanima("kali aç ve ip taraması yap")
    zamanlayici.rapor_olustur()
    guvenlik.guvenlik_uyarisi()
    print("[+] Başlangıç işlemleri tamamlandı.")


# Sesli yanıt verme fonksiyonu
def sesli_cevap(veri):
    engine = pyttsx3.init()
    engine.say(veri)
    engine.runAndWait()

# Sesli komut tanıma fonksiyonu
def sesli_komut_tanima():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Komutunuzu bekliyorum...")
        sesli_cevap("Komutunuzu bekliyorum")
        audio = r.listen(source)

    try:
        komut = r.recognize_google(audio, language="tr-TR")
        print(f"📥 Alınan Komut: {komut}")
        sesli_cevap(f"Komut alındı: {komut}")
        komutlar.komut_tanima(komut.lower())  # Küçük harfe çevir, daha iyi eşleşir

    except sr.UnknownValueError:
        print("❌ Komut anlaşılamadı.")
        sesli_cevap("Komutunuzu anlayamadım.")
    except sr.RequestError:
        print("❌ Google API servisine ulaşılamadı.")
        sesli_cevap("Servise bağlanılamadı, lütfen internet bağlantınızı kontrol edin.")

# Yazılı komut alma fonksiyonu
def komut_al():
    secim = input("🟢 Komut tipi [1: Sesli / 2: Yazılı] > ").strip()
    if secim == "1":
        sesli_komut_tanima()
        return None
    else:
        komut = input("✍️ Komut girin: ")
        return komut.lower()
