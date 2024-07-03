import random
rastgele = random.randrange(1,1000)
# print("tutulan sayı",rastgele)
tahminSayisi = 10
taban = 0
tavan = 1001
while tahminSayisi >= 1:
    tahmin =random.randrange(taban,tavan)
    # tahmin =int(input("sayı giriniz"))
    print(tahmin , end=" ")
    cevap = input("+,-,=")
    if cevap == "=":
        print("Tebrikler")
        break
    elif cevap == "+" :
        print("daha küçük")
        tavan = tahmin
    elif cevap == "-":
        print("daha büyük")
        taban = tahmin
    tahminSayisi -= 1
    print("kalan hakkınız", tahminSayisi)