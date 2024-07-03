import random
rastgele = random.randrange(1,1000)
print("tutulan sayı",rastgele)
tahminSayisi = 10
taban = 0
tavan = 1001
while tahminSayisi >= 1:
    # tahmin =random.randrange(taban,tavan)
    tahmin =int(input("sayı giriniz"))
    print(tahmin , end=" ")
    if tahmin == rastgele:
        print("Tebrikler")
        break
    elif tahmin > rastgele:
        print("daha küçük")
        tavan = tahmin
    elif tahmin < rastgele:
        print("daha büyük")
        taban = tahmin
    tahminSayisi -= 1
    print("kalan hakkınız", tahminSayisi)