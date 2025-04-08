"# kali-asistan" 
# Kali Asistan 🤖🔐

git clone https://github.com/albertou2311/kali-asistan.git
cd kali-asistan
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python ana.py

cd kali-asistan             # Proje klasörüne gir
nano README.md              # README dosyasını düzenle

# değişiklikleri yaptıktan sonra kaydet: Ctrl+O, Enter, Ctrl+X
git add README.md
git commit -m "README güncellendi"
git commit -m

**Kali Asistan**, siber güvenlik uzmanları için geliştirilmiş, sesli/yazılı komutlarla çalışan bir yapay zeka destekli penetrasyon testi asistanıdır.

## 🚀 Özellikler

- 🔍 Otomatik hedef tarama (OS, servis, port, zafiyet)
- 🕵️‍♂️ Anonimlik desteği (IP, MAC gizleme)
- 💥 Exploit ve zafiyet tespiti
- 🔐 SSH üzerinden Kali araçlarına komut gönderme
- 🧠 NLP (Doğal dil) destekli komut işleme
- 🧾 Otomatik loglama, raporlama ve e-posta gönderimi
- 🗓️ Zamanlanmış görevler
- 🎯 OSINT (açık kaynak istihbarat) araçları ile analiz
- ☁️ VMware içinde otomatik başlatma ve tarama

## 📁 Dosya Yapısı

```bash


├── ana.py                 # Ana uygulama dosyası
├── asistan.py            # Asistanın temel işleyişi
├── komut_asistani.py     # Komutları algılama ve yönlendirme
├── komutlar.py           # Tüm kullanılabilir komutlar
├── anonimlik.py          # IP, MAC gizleme işlemleri
├── port_tarama.py        # Port tarama modülü
├── exploit_taramasi.py   # Exploit tespit modülü
├── osint_aracı.py        # OSINT araçları
├── loglayici.py          # Log kayıt sistemi
├── zamanlayici.py        # Zamanlanmış görevler
├── eposta_gonderici.py   # Raporları mail olarak gönderir
├── README.md             # Bu dosya
└── ...
💬 Örnek Komutlar
"VMware'yi başlat" → VMware başlatılır

"Kali Linux'a giriş yap" → SSH ile bağlanır

"192.168.1.1 adresini tara" → Nmap, whois, nslookup gibi araçlarla bilgi toplar

"Exploit bul" → CVE veritabanında açık arar

"Portları kaydet" → Tarama sonuçlarını portlar.txt içine yazar

📩 İletişim
Geliştirici: Albertou
Firma: Yıldırım Bilişim Elektrik
