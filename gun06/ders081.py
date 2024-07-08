import json
kitap_listesi = []

class Kitap():
    def __init__(self, ad, yazar, sayfa, basim):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa
        self.basim = basim
    def __str__(self):
        return self.ad

def kitapTanimla():
    try:
        kitap_adi = input("Kitap adı")
        kitap_yazar = input("yazar")
        kitap_sayfa = int(input("sayfa"))
        kitap_yili = int(input("yili"))
        kitap = Kitap(kitap_adi, kitap_yazar, kitap_sayfa, kitap_yili)
        kitap_listesi.append(kitap)
        return True
    except:
        return False

def kitapListele():
    if len(kitap_listesi) == 0:
        return "Listelenecek Kitap Yok"
    else:
        for x, kitap in enumerate(kitap_listesi):
            print(x+1,kitap)

def kitapListesiKaydet():
    try:
        with open("kitaplistesi.json", "w") as kitap_listesi_dosyasi:
            kitap_bilgileri = json.dumps(kitap_listesi)
            kitap_listesi_dosyasi.write(kitap_bilgileri)
            print("Kayıt işlemi Başarılı")
            return True
    except:
        print("Kayıt işlemi Başarısız")
        return True


def menu():
    while True:
        k_giris = input("Yeni Kitap Tanımla:1, Listele:2, Kaydet:3, Çıkış:Q")
        if k_giris == "1":
            kitapTanimla()
        elif k_giris == "2":
            kitapListele()
        elif k_giris == "3":
            kitapListesiKaydet()
        else:
            exit()

if __name__ == "__main__":
    menu()
