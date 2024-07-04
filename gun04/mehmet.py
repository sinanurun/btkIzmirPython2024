import random
import time

jeton = int(input("Şanslı 7li oyununa hoşgeldiniz. Kaç adet jeton almak istersiniz? "))

while jeton > 0:
    jeton -= 1
    rakam1 = random.randrange(0,9)
    rakam2 = random.randrange(0,9)
    rakam3 = random.randrange(0,9)

    print(rakam1, rakam2,rakam3, sep="\t")

    if (rakam1 == rakam2) and (rakam2 == rakam3):
        print("Şanslı 7li Oyununu kazandınız. Kalan jeton: {}".format(jeton))
        break
    else:
        if jeton == 0:
            print("Jetonunuz bitti, oyunu kaybettiniz.")
        else:
            print("Rakamlar aynı gelmedi, tekrar deneniyor..")
            # time.sleep(0.5)