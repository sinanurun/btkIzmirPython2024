class Ogrenci():
    bolum = "Bilişim"
    kurs = "Btk Akademi"

    def __init__(self, ad, soyad, tc):
        print("Ogrenci oluşturuldu")
        self.ad = ad
        self.soyad = soyad
        self.tcno = tc

ogr1 = Ogrenci("kerim","can",123)
print(ogr1.bolum)
print(ogr1.kurs)
print(vars(ogr1))

