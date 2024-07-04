class Kitap():
    ad = ""
    yazar = ""
    basim = ""

kitap_listesi = []
for i in range(5):
    kitap = Kitap()
    kitap.ad = input(f"{i+1}. Kitap adı giriniz")
    kitap_listesi.append(kitap)

for i in kitap_listesi:
    print(i.ad)
# print(Kitap.count)

