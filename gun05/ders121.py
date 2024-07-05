class Ogrenci():
    bolum = "Bilişim"
    kurs = "Btk Akademi"

    def __init__(self, ad, soyad, tc):
        print("Ogrenci oluşturuldu")
        self.ad = ad
        self.soyad = soyad
        self.tcno = tc

    def tamAd(self):
        return self.ad + self.soyad

    def kafHarf(self):
        return len(self.ad)

    def __str__(self):
        return f"{self.ad} - {self.soyad} - adında bir öğrenci"
ogr1 = Ogrenci("kerim","can",123)

print(ogr1)

print(ogr1.bolum)
print(ogr1.kurs)
print(vars(ogr1))
print(ogr1.tamAd())
harf_sayisi = ogr1.kafHarf()
print(harf_sayisi)
# print(Ogrenci.tamAd())

