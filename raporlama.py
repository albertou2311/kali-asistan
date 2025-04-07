import subprocess

def nikto_taramasi():
    subprocess.run(["nikto", "-h", "http://hedefsite.com"])

def dirbuster_baslat():
    subprocess.run(["dirbuster", "-u", "http://hedefsite.com"])

# Taramaları başlat
nikto_taramasi()
dirbuster_baslat()
