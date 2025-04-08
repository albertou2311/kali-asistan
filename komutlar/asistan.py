# asistan.py
from komut_yoneticisi import sesli_cevap, sesli_komut_tanima, komut_al

def main():
    komut = komut_al()
    if komut:
        from komut_yoneticisi import komut_tanima
        komut_tanima(komut)

if __name__ == "__main__":
    main()
