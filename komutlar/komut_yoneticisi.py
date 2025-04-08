# komut_yoneticisi.py
import pyttsx3
import speech_recognition as sr
from loglayici import logla
from komutlar import apache_kapat, sistemi_guncelle, sistem_temizligi, fonksiyon
from exploit_taramasi import exploit_ara

import importlib
komut_modulleri = ["komutlar.sistem", "komutlar.ag", "komutlar.tarama"]
for mod in komut_modulleri:
    importlib.import_module(mod)

komutlar = {
    "apache_kapat": apache_kapat,
    "sistem_temizle": sistem_temizligi,
    "guncelle": sistemi_guncelle,
    "exploit_ara": lambda: exploit_ara("192.168.1.1"),  # örnek kullanım
}

def komut_tanima(girdi):
    if "komutlar" in girdi:
        komutlari_listele()
        return
    
    for komut, fonksiyon in komutlar.items():
        if komut in girdi:
            logla(f"{komut} komutu çalıştırılıyor...", "info")
            fonksiyon()
            return
    logla("Komut tanınamadı.", "warning")

def komutlari_listele():
    print("\n📋 Kullanılabilir Komutlar:")
    for komut in komutlar:
        print(f"→ {komut}")

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

        komut_tanima(komut.lower())  # Küçük harfe çevir, daha iyi eşleşir

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
