# sayilar = set()
sayi = int(input("bir sayi giriniz"))
eb = sayi
ek = sayi
sayilar = {sayi}
while len(sayilar)<10:
    sayilar.add(int(input("Bir sayı giriniz")))
for ksayi in sayilar:
    if eb < ksayi:
        eb = ksayi
    if ek > ksayi:
        ek = ksayi
print("en büyük", eb)
print("en büçük", ek)