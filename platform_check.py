import subprocess
import platform

print("You are running on:", platform.system())

# Eğer Windows'taysak
if platform.system() == "Windows":
    print("Windows ortamında çalıştırılıyor...")
    # Windows'a uygun komutları çalıştırıyoruz
    result = subprocess.run(["ipconfig"], capture_output=True, text=True)
    print(result.stdout)  # Komutun çıktısını yazdırıyoruz

# Eğer Linux'taysak
elif platform.system() == "Linux":
    print("Linux ortamında çalıştırılıyor...")
    # Linux'a uygun komutları çalıştırıyoruz
    result = subprocess.run(["ifconfig"], capture_output=True, text=True)
    print(result.stdout)  # Komutun çıktısını yazdırıyoruz
