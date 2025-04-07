import winsound

def guvenlik_uyarisi():
    print("Kritik güvenlik açığı tespit edildi!")
    winsound.Beep(1000, 1000)  # Sesli uyarı

guvenlik_uyarisi()
