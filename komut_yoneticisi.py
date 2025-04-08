import pyttsx3
import speech_recognition as sr
import importlib

from komutlar.apache_kapat import apache_kapat
from komutlar.guvenlik import sistemi_guncelle, sistem_temizligi
from komutlar.exploit_taramasi import exploit_ara
from komutlar.loglayici import logla

# Komut modüllerini dinamik olarak yükle (gerekiyorsa)
komut_modulleri = ["komutlar.sistem", "komutlar.ag", "komutlar.tarama"]
for mod in komut_modulleri:
    importlib.import_module(mod)

# Komut sözlüğü - çakışma önlendi
komut_sozlugu = {
    "apache_kapat": apache_kapat,
    "sistem_temizle": sistem_temizligi,
    "guncelle": sistemi_guncelle,
    "exploit_ara": lambda: exploit_ara("192.168.1.1"),  # örnek IP
}

# Komut tanıma fonksiyonu
def komut_tanima(girdi):
    if "komutlar" in girdi:
        komutlari_listele()
        return

    for komut, fonksiyon in komut_sozlugu.items():
        if komut in girdi:
            logla(f"{komut} komutu çalıştırılıyor...", "info")
            fonksiyon()
            return
    logla("Komut tanınamadı.", "warning")

# Komut listesi
def komutlari_listele():
    print("\n📋 Kullanılabilir Komutlar:")
    for komut in komut_sozlugu:
        print(f"→ {komut}")

# Sesli cevap verme
def sesli_cevap(veri):
    engine = pyttsx3.init()
    engine.say(veri)
    engine.runAndWait()

# Sesli komut tanıma
def sesli_komut_tanima():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Komutunuzu bekliyorum...")
        sesli_cevap("Komutunuzu bekliyorum")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        komut = r.recognize_google(audio, language="tr-TR")
        print(f"📥 Alınan Komut: {komut}")
        sesli_cevap(f"Komut alındı: {komut}")
        komut_tanima(komut.lower())

    except sr.UnknownValueError:
        print("❌ Komut anlaşılamadı.")
        sesli_cevap("Komutunuzu anlayamadım.")
    except sr.RequestError:
        print("❌ Google API servisine ulaşılamadı.")
        sesli_cevap("Servise bağlanılamadı, lütfen internet bağlantınızı kontrol edin.")
    except Exception as e:
        print(f"⚠️ Hata: {e}")
        sesli_cevap("Bir hata oluştu.")

# Yazılı komut alma
def komut_al():
    secim = input("🟢 Komut tipi [1: Sesli / 2: Yazılı] > ").strip()
    if secim == "1":
        sesli_komut_tanima()
        return None
    else:
        komut = input("✍️ Komut girin: ")
        komut_tanima(komut.lower())
