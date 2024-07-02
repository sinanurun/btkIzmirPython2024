baslangic = int(input("Baslangic: "))
bitis = int(input("Bitis: "))
artis = int(input("Artis: "))

if baslangic > bitis:
    baslangic ,bitis = bitis, baslangic

toplam, carpim = 0, 1
while baslangic <= bitis:
    toplam += baslangic
    carpim *= baslangic
    baslangic += artis

metin = "Sayıların Toplamı {}, Çarpımı {}"
print(metin.format(toplam,carpim))