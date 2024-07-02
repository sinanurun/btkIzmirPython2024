baslangic = int(input("Baslangic: "))
bitis = int(input("Bitis: "))
artis = int(input("Artis: "))
toplam, carpim = 0, 1
for i in range(baslangic,bitis,artis):
    print(i)
    toplam += i
    carpim *= i

metin = "Sayıların Toplamı {}, Çarpımı {}"
print(metin.format(toplam,carpim))