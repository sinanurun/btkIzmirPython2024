ogrenci_adi = "hatice"
ogrenci_soyadi = "akıncı"
ogrenci_yas = 21
ogrenci_boy = 1.63
ogrenci_cinsiyet = True

ogrenci_bilgisi = [ogrenci_adi,ogrenci_soyadi,
                   ogrenci_boy,ogrenci_yas,ogrenci_cinsiyet]
print(ogrenci_bilgisi)
print(ogrenci_bilgisi[0])
print(ogrenci_bilgisi[-1])
print(ogrenci_bilgisi[:2])
print(ogrenci_bilgisi[-2:])
print(len(ogrenci_bilgisi))
print(type(ogrenci_bilgisi))
for bilgi in ogrenci_bilgisi:
    print(bilgi)