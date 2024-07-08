import json
class Kitap():
    def __init__(self, ad, yazar, sayfa, basim):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa
        self.basim = basim

    @classmethod
    def kitapOlustur(cls,kwargs):
        ad,yazar,sayfa,basim = kwargs.values()
        return cls(ad, yazar, sayfa, basim)


def kitapTanimla():
    try:
        kitap_adi = input("Kitap adı")
        kitap_yazar = input("yazar")
        kitap_sayfa = int(input("sayfa"))
        kitap_yili = int(input("yili"))
        kitap = Kitap(kitap_adi, kitap_yazar, kitap_sayfa, kitap_yili)
        kitap_bilgisi = vars(kitap)
        kitap_listesi.append(kitap_bilgisi)
        return True
    except:
        return False

def kitapGuncelle(gkitap):
    kitap = Kitap.kitapOlustur(kitap_listesi[gkitap])
    kitap.ad = "deli"
    kitap_listesi[gkitap] = vars(kitap)

def kitapListele():
    if len(kitap_listesi) == 0:
        return "Listelenecek Kitap Yok"
    else:
        for x, kitap in enumerate(kitap_listesi):
            print(x+1,kitap["ad"])

def kayitliKitapListele():
    try:
        with open("kitaplistesi.json", "r") as dosya:
            kayitli_kitap_listesi = list(json.load(dosya))
            if len(kayitli_kitap_listesi ) == 0:
                print("Kayitli kitap bulunama")
            else:
                for x, kitap in enumerate(kayitli_kitap_listesi ):
                    print(x+1,kitap["ad"])
            return kayitli_kitap_listesi
    except:
        return []

def kitapListesiKaydet():
    try:
        with open("kitaplistesi.json", "w") as kitap_listesi_dosyasi:
            kitap_bilgileri = json.dumps(kitap_listesi)
            kitap_listesi_dosyasi.write(kitap_bilgileri)
            print("Kayıt işlemi Başarılı")
            return True
    except Exception as e:
        print("Kayıt işlemi Başarısız", e)
        return True


def menu():
    while True:
        k_giris = input("Yeni Kitap Tanımla:1, Listele:2, Kaydet:3,Kayitli Kitaplar:4, Çıkış:Q")
        if k_giris == "1":
            kitapTanimla()
        elif k_giris == "2":
            kitapListele()
        elif k_giris == "3":
            kitapListesiKaydet()
        elif k_giris == "4":
            kayitliKitapListele()
        else:
            exit()

if __name__ == "__main__":
    kitap_listesi = kayitliKitapListele()
    menu()
