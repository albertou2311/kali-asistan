import platform
import subprocess

# Eğer Windows'taysak
if platform.system() == "Windows":
    print("Windows ortamında çalıştırılıyor...")
    # Windows'a uygun komutları çalıştırabiliriz
    subprocess.run(["ipconfig"])  # Windows'da IP bilgisi almak için ipconfig kullanılır.

# Eğer Linux'taysak
elif platform.system() == "Linux":
    print("Linux ortamında çalıştırılıyor...")
    # Linux'a uygun komutları çalıştırabiliriz
    subprocess.run(["ifconfig"])  # Linux'ta ifconfig çalışır
