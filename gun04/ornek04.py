kitaplik = {}
while True:
    kategori_adi = input("Kategori - h?: ")
    if kategori_adi == "h":
        print("Kategori Giriş İşlemi Tamamlandı")
        break
    else:
        kitaplik[kategori_adi] ={}
        while True:
            yazar_adi = input("Yazar Adı - h?: ")
            if yazar_adi == "h":
                print("Yazar Girişi Tamamlandı")
                break
            else:
                kitap = []
                # kitaplik[kategori_adi][yazar_adi] = []
                while True:
                    kitap_adi = input("Kitap Adı - h?: ")
                    if kitap_adi == "h":
                        print("Kitap Girişi Tamamlandı")
                        kitaplik[kategori_adi][yazar_adi] = kitap
                        break
                    else:
                        kitap.append(kitap_adi)
                        # kitaplik[kategori_adi][yazar_adi].append(kitap_adi)

print(kitaplik)
