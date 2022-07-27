import pandas as pd
import keyboard

class control():

    def __init__(self):
        print("Ders Notu Hesaplama Sistemi")

    def numaraKontrol(self):
        while (True):
            try:
                okulNo = int(input("Numara:"))
                return okulNo
                break
            except:
                print("Lütfen sayısal bir değer giriniz")

    def notKontrol(self):
        while (True):
            try:
                notu = int(input("notunu giriniz:"))
                if (notu >= 0 and notu <= 100):
                    return notu
                    break
                else:
                    print("lütfen [0-100] arası not giriniz")
                    continue
            except:
                print("hatalı not girişi tekrar giriniz")

    def harf_Durum_Belirleme(self, notu):
        if notu > 80:
            harfNotu = "A"
            durum = "GEÇTİ"
        elif notu > 70:
            harfNotu = "B"
            durum = "GEÇTİ"
        elif notu > 55:
            harfNotu = "C"
            durum = "GEÇTİ"
        elif notu > 45:
            harfNotu = "D"
            durum = "GEÇTİ"
        elif notu > 25:
            harfNotu = "E"
            durum = "KALDI"
        else:
            harfNotu = "F"
            durum = "KALDI"

        return harfNotu, durum

    def tusKontrol(self):
        while True:
            try:
                if keyboard.is_pressed('q'):
                    print("çıkılıyor!!!")
                    cikis = True
                    return cikis
                    break
                elif keyboard.is_pressed('d'):
                    print("devam ediliyor")
                    break
            except:
                print("istenmeyen bir hata oluştu")
                break

                # print("boş dönüyor")
                
                
                
sinif = control()
veri = []
while True:
    desAdi = input("ders adını giriniz:")
    ad = input("Ad:")
    soyAd = input("Soyad:")

    okulNo = sinif.numaraKontrol()

    notu = sinif.notKontrol()

    harfNotu, durum = sinif.harf_Durum_Belirleme(notu)

    veri.append([ad, soyAd, desAdi, okulNo, notu, harfNotu, durum])
    print("Veri kaydedildi çıkmak için 'q' tuşuna devam etmek için 'd' tuşuna basınız:")

    cikis = sinif.tusKontrol()

    if cikis == True:
        break

sutun_isimleri = ['Ad', 'Soyad', 'Ders_Adı', 'Numara', 'Not', 'Harf', 'Durum']
df = pd.DataFrame(data=veri, columns=sutun_isimleri)
df.to_excel("ogr_bilgiler.xlsx")
