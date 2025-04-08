# komutlar.py içinde
# asistan.py içinde
from komutlar import apache_kapat, sistemi_guncelle, disk_temizligi, guvenlik_taramasi

def komut_calistir():
    # Apache'yi kapat
    apache_kapat()

    # Sistemi güncelle
    sistemi_guncelle()

    # Disk temizliği yap
    disk_temizligi()

    # Güvenlik taraması başlat
    guvenlik_taramasi()
