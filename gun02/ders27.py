carpim = 1
while True:
    sayi = int(input("bir sayı giriniz"))
    if sayi == 0:
        print("girilen sayıların çarpımı", carpim)
        break
    carpim *= sayi