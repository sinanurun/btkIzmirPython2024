class Ogrenci():
    bolum = "Bilişim"
    kurs = "Btk Akademi"
    ogrenci_sayisi = 0
    ogrenci_listesi = []
    def __init__(self, ad, soyad, tc):
        self.ad = ad
        self.soyad = soyad
        self.tcno = tc
        Ogrenci.ogrenci_sayisi += 1
        print(self.ogrenci_sayisi,"Ogrenci oluşturuldu")

    def tamAd(self):
        return self.ad + self.soyad

    def kafHarf(self):
        return len(self.ad)

    def __str__(self):
        return f"{self.ad} - {self.soyad} - adında bir öğrenci"
ogr1 = Ogrenci("kerim","can",123)
ogr2 = Ogrenci("ege","canan",456)

print(ogr1)
print(ogr2)
print("tanımlanan öğrenci sayısı :", Ogrenci.ogrenci_sayisi)
print("tanımlanan öğrenci sayısı :", ogr1.ogrenci_sayisi)
print("tanımlanan öğrenci sayısı :", ogr2.ogrenci_sayisi)


