#versiyon 1 pazar listesi
"""
adet = int(input("kaç farklı zerzevat alacaksınız"))
zerzevat = []
for i in range(1,adet+1):
    urun = input(f"{i}. urun bilgisini giriniz : ")
    zerzevat.append(urun)

for urun in zerzevat:
    print(urun, end= "\t")
"""
#versiyon 2 pazar listesi
mesaj = """Pazar Listesi Oluşturma Programına Hoşgeldiniz
Programdan Çıkmak için X'e basınız"""
print(mesaj)
zerzevat = []
while True:
    urun = input("Ürün girişi yapınız")
    if urun.lower() == "x":
        print("pazar listeniz", zerzevat)
        break
    elif urun == "":
        continue
    else:
        zerzevat.append(urun)