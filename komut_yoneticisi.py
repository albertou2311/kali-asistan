import pyttsx3
import speech_recognition as sr
import komutlar


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
