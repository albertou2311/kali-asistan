import nmap
import datetime

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
