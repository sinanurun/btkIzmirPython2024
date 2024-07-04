class Ogrenci():
    bolum = "Bilişim"
    kurs = "Btk Akademi"

    def __init__(self):
        print("Ogrenci oluşturuldu")
        self.ad = input("ad gir")
        self.soyad = input("soyadad gir")
        self.tcno = input("tc gir")

ogr1 = Ogrenci()
print(ogr1.bolum)
print(ogr1.kurs)
ogr1.ad = "Kerim"
print(ogr1.ad)
print(vars(ogr1))
ogr2 = Ogrenci()
print(ogr2.bolum)
print(ogr2.kurs)
ogr2.ad = "Ege"
print(ogr2.ad)
print(vars(ogr2))
