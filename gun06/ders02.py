class Calisan():
    zam_orani = 1.1
    per_say = 0
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        Calisan.per_say += 1
        self.eposta = self.ad+self.soyad+"@sirket.com"

    def tamAd(self):
        return "ad : {}, soyad : {}".format(self.ad, self.soyad)
    # def arttirMaas(self):
    #     self.maas *= Calisan.zam_orani
    def arttirMaas(self, oran = 1.1):
        self.zam_orani = oran
        self.maas *= self.zam_orani

print(Calisan.zam_orani)
print(Calisan.per_say)
personel1 = Calisan("Sakir","can",8000)
print(personel1.tamAd())
print(Calisan.per_say)
personel1.arttirMaas()
print(personel1.maas)