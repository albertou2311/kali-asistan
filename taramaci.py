import nmap
import datetime

# taramaci.py içine ekle
import subprocess

def hedef_bilgi_topla(ip_adresi):
    print(f"[+] {ip_adresi} hedefi hakkında bilgi toplanıyor...")
    try:
        # OS ve servis bilgisi toplama (Nmap servis taraması)
        sonuc = subprocess.check_output(f"nmap -sS -sV -O {ip_adresi}", shell=True, text=True)
        
        with open("raporlar/bilgi_raporu.txt", "w") as f:
            f.write(sonuc)
        
        print("[+] Bilgi raporu oluşturuldu: raporlar/bilgi_raporu.txt")
        return sonuc
    except subprocess.CalledProcessError as e:
        print("[-] Bilgi toplama sırasında hata oluştu:", e)
        return None



def hedef_tara(ip_adresi):
    scanner = nmap.PortScanner()
    print(f"[+] {ip_adresi} IP adresi taranıyor...")
    scanner.scan(ip_adresi, arguments="-p-")
    sonuc = scanner[ip_adresi]

    acik_portlar = []
    for port in sonuc['tcp']:
        if sonuc['tcp'][port]['state'] == 'open':
            acik_portlar.append(port)

    # Rapor yaz
    zaman = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    rapor_adi = f"rapor_{ip_adresi.replace('.', '_')}_{zaman}.txt"

    with open(rapor_adi, 'w') as dosya:
        dosya.write(f"IP: {ip_adresi}\n")
        dosya.write("Açık Portlar:\n")
        for port in acik_portlar:
            dosya.write(f"  - {port}\n")

    print(f"[✓] Taraması bitti. Açık portlar: {acik_portlar}")
    print(f"[✓] Rapor kaydedildi: {rapor_adi}")
    return acik_portlar
