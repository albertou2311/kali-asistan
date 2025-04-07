
import paramiko

# SSH bağlantısı için parametreler
hostname = "192.168.142.129"  # Buraya Kali IP adresinizi yazın
username = 'albertou'  # Buraya Kali kullanıcı adınızı yazın
password = '2311'  # Buraya Kali şifrenizi yazın

# SSH istemcisi oluşturma
ssh = paramiko.SSHClient()

# Güvenlik hatalarını yok saymak
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Bağlantıyı açma
ssh.connect(hostname, username=username, password=password)

# Komut çalıştırma
stdin, stdout, stderr = ssh.exec_command("ls")
print(stdout.read().decode())

# Bağlantıyı kapatma
ssh.close()

####
#def ssh_baglantisi():
    #client = paramiko.SSHClient()
    #client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ## Kali IP ve kullanıcı bilgileri
    #kali_ip = "192.168.142.129"
    #username = "albertou"
    #password = "2311"

    #try:
        #client.connect(kali_ip, username=username, password=password)
        #stdin, stdout, stderr = client.exec_command("sniper -t 192.168.1.1")
        #print(stdout.read().decode())
    #except Exception as e:
        #print(f"Hata oluştu: {e}")
    #finally:
        #client.close()

#Fonksiyonu çalıştır
#ssh_baglantisi()
