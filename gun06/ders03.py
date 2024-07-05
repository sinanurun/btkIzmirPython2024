class Ogrenci():
    def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad

class FOgrenci(Ogrenci):
    def __init__(self,ad, soyad, fakulte):
        # Ogrenci.__init__(self,ad,soyad)
        super().__init__(self,ad,soyad)
        self.fakulte=fakulte

class BOgrenci(FOgrenci):
    def __init__(self,ad,soyad,fakulte,bolum):
        FOgrenci.__init__(self,ad, soyad, fakulte)
        self.bolum=bolum


