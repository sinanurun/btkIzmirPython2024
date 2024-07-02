# if True:
#     pass
# print("he")
#break döngünün bitirilmesini sağlayan komuttur
# for dd in range(20):
#     ad = input("adınızı giriniz")
#     if ad == "hatice":
#         print("hatice bulundu")
#         break
#     print(dd)

for dd in range(20):
    ad = input("adınızı giriniz")
    if ad == "can":
        print("can kayıt yapılamaz")
        continue
    soyad = input("soyad giriniz")
    print(ad,soyad,"kayıt tamamlandı")