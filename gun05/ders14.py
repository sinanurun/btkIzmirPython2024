class Otomobil():
    teker = 4
    kapi = True

    def __init__(self, marka, model, renk):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.calisma_durumu = False

    def calistir(self):
        if self.calisma_durumu == False:
            self.calisma_durumu = True
            print("araba çalıştırıldı")
            self.hiz = 0
        else:
            print("araba zaten çalışıyor")

    def durdur(self):
        if self.calisma_durumu == True:
            self.calisma_durumu = False
            print("araba durduruldu")
        else:
            print("araba zaten duruyor")

    def hizArttir(self):
        if self.calisma_durumu == True:
            self.hiz += 10
            self.hizGoster()
        else:
            print("arabayı öncelikle çalıştırınız")

    def hizAzalt(self):
        if self.calisma_durumu == True and self.hiz >= 10:
            self.hiz -= 10
            self.hizGoster()
        elif self.calisma_durumu == True and self.hiz == 0:
            print("araç çalşıyor ama zaten duruyor hız azaltılamaz")
        else:
            print("arabayı öncelikle çalıştırınız")

    def hizGoster(self):
        if self.calisma_durumu == False:
            self.hiz = 0
        print("aracın hızı", self.hiz)
        return self.hiz

    def cikis(self):
        print("çıkış yapıldı")
        exit()

    def __str__(self):
        return f"{self.marka} marka {self.model} model {self.renk} renkli araba"


oto1 = Otomobil(marka="Tofaş", model="Kartal", renk="Kırmızı")
# print(oto1)
# oto1.calistir()
# oto1.calistir()
# oto1.durdur()
# oto1.durdur()
# oto1.hizArttir()
# oto1.calistir()
# oto1.hizArttir()

while True:
    cevap = int(input("Çalıştır : 1 \t "
                      "Durdur: 2\n, "
                      "arttır: 3\t, "
                      "Azatl : 4\n "
                      "Hız Göster : 5\t, "
                      "Çıkış 6 \n"))
    if cevap == 1:
        oto1.calistir()
    elif cevap == 2:
        oto1.durdur()
    elif cevap == 3:
        oto1.hizArttir()
    elif cevap == 4:
        oto1.hizAzalt()
    elif cevap == 5:
        oto1.hizGoster()
    elif cevap == 6:
        oto1.cikis()
    else:
        print("hatalı işlem girişi")