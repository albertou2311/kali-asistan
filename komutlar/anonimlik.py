import os
import subprocess

def mac_degistir(arayuz="eth0"):
    print(f"🔄 {arayuz} arayüzü için MAC adresi değiştiriliyor...")
    subprocess.run(["sudo", "ifconfig", arayuz, "down"])
    subprocess.run(["sudo", "macchanger", "-r", arayuz])
    subprocess.run(["sudo", "ifconfig", arayuz, "up"])
    print("✅ MAC adresi rastgele olarak değiştirildi.\n")

def tor_baslat():
    print("🌀 Tor servisi başlatılıyor...")
    subprocess.run(["sudo", "systemctl", "start", "tor"])
    print("✅ Tor servisi çalışıyor. ProxyChains aktif olabilir.\n")

def proxychains_kontrol():
    print("🌐 ProxyChains ile IP adresi kontrol ediliyor...")
    try:
        sonuc = subprocess.check_output(["proxychains", "curl", "https://ifconfig.me"], stderr=subprocess.DEVNULL)
        ip = sonuc.decode().strip()
        print(f"🌍 Yeni IP adresin (proxy üzerinden): {ip}\n")
    except Exception as e:
        print(f"❌ ProxyChains hatası: {e}")

def vpn_durumu():
    print("🛡️ VPN bağlantı kontrolü...")
    try:
        sonuc = subprocess.check_output("ifconfig", shell=True).decode()
        if "tun0" in sonuc:
            print("✅ VPN (tun0) bağlantısı aktif.\n")
        else:
            print("⚠️ VPN bağlantısı tespit edilmedi.\n")
    except Exception as e:
        print(f"❌ VPN kontrol hatası: {e}")

if __name__ == "__main__":
    mac_degistir("eth0")         # veya wlan0 kullan
    tor_baslat()
    proxychains_kontrol()
    vpn_durumu()
