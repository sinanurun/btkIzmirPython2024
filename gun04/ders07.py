dosya_adi = "deneme.txt"
with open(dosya_adi) as dosya:
    print(dosya.readline())
    print(dosya.readline())

with open(dosya_adi) as dosya:
    metin = dosya.read()
    satirlar = metin.split("\n")
    for i in satirlar:print(i)
