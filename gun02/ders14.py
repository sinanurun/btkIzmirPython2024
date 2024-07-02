ad1 = "Mehmet"
ad2 = "Irmak"
ad3 = "Umut"
print(ad1 + ad2 + ad3)
print(f"{ad1} {ad2} {ad3}")

metin = "Merhaba sayın {} Kursumuza Hoşgeldiniz"
print(metin.format(ad1))
print(metin.format(ad2))
print(metin.format(ad3))

metin2 = "yarışmamızın başarı listesi {} {} {}"
print(metin2.format(ad1,ad2,ad3))
print(metin2.format(ad2,ad3,ad1))

metin3 = "{k1}, {k2} {k3} {k1},".format(k1=ad1,k2=ad2,k3=ad3)
print(metin3)