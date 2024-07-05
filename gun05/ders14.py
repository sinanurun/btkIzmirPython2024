class Otomobil():
    teker = 4
    kapi = True
    def __init__(self, marka, model, renk):
        self.marka = marka
        self.model = model
        self.renk = renk
        self. calisma_durumu = False

    def calistir(self):
        if self.calisma_durumu == False:
            self.calisma_durumu = True
            print("araba çalıştırıldı")
        else:
            print("araba zaten çalışıyor")

    def durdur(self):
        if self.calisma_durumu == True:
            self.calisma_durumu = False
            print("araba durduruldu")
        else:
            print("araba zaten duruyor")



    def __str__(self):
        return f"{self.marka} marka {self.model} model {self.renk} renkli araba"


oto1 = Otomobil(marka="Tofaş", model="Kartal", renk="Kırmızı")
print(oto1)
oto1.calistir()
oto1.calistir()
oto1.durdur()
oto1.durdur()