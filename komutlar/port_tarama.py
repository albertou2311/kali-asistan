import nmap

def port_tara(ip_adresi):
    nm = nmap.PortScanner()
    nm.scan(ip_adresi, '1-65535')  # Tüm portları tarama
    
    for host in nm.all_hosts():
        print(f"Tarama yapılan host: {host}")
        for proto in nm[host].all_protocols():
            print(f"Protokol: {proto}")
            lport = nm[host][proto].keys()
            for port in lport:
                print(f"Port {port} durumu: {nm[host][proto][port]['state']}")

if __name__ == "__main__":
    ip_adresi = input("Hedef IP adresini girin: ")
    port_tara(ip_adresi)
