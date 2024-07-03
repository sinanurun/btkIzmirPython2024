#versiyon 1 kullanıcıdan sayı alıp tahmin etme
# sayi = 35
# tahmin = int(input("Bir sayı giriniz"))
# if tahmin == sayi:
#     print("Tahmin başarılı")
# else:
#     print("Tahmin Başarısız")

# versiyon 2 aşağı yukarı
# sayi = 35
# tahmin = int(input("Bir sayı giriniz"))
# if tahmin == sayi:
#     print("Tahmin başarılı")
# elif tahmin > sayi:
#     print("Tahmin Başarısız Keşke küçük bür sayı söyleseydin")
# elif tahmin < sayi:
#     print("Tahmin Başarısız Keşke büyük bir sayı söyleseydin")

# #versiyon 3
# sayi = 35
# taban = 0
# tavan = 100
# print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
# tahmin = int(input("Bir sayı giriniz"))
# while True:
#     if taban <= tahmin <= tavan:
#         print(f"Tahmin geçerli aralıkta")
#         break
#     else:
#         print(f"Tahmin aralığı dışında geçersiz tahmin")
#         print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
#         tahmin = int(input("Bir sayı giriniz"))
# if tahmin == sayi:
#     print("Tahmin başarılı")
# elif tahmin > sayi:
#     print("Tahmin Başarısız Keşke küçük bür sayı söyleseydin")
# elif tahmin < sayi:
#     print("Tahmin Başarısız Keşke büyük bir sayı söyleseydin")

# #versiyon 4 tahmin etmeye devam edebilsin
# sayi = 35
# taban = 0
# tavan = 100
# print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
# tahmin = int(input("Bir sayı giriniz"))
# while True:
#     if taban <= tahmin <= tavan:
#         print(f"Tahmin geçerli aralıkta")
#         break
#     else:
#         print(f"Tahmin aralığı dışında geçersiz tahmin")
#         print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
#         tahmin = int(input("Bir sayı giriniz"))
# while True:
#     if tahmin == sayi:
#         print("Tahmin başarılı")
#         break
#     elif tahmin > sayi:
#         print("Tahmin Başarısız Keşke küçük bir sayı söyleseydin")
#     elif tahmin < sayi:
#         print("Tahmin Başarısız Keşke büyük bir sayı söyleseydin")
#     print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
#     tahmin = int(input("Bir sayı giriniz"))

#versiyon 5 tahmin etmeye devam edebilsin ama aralık daralsın ve
# sadece daralan aralıkta tahminde bulunsun
sayi = 35
taban = 0
tavan = 100
gecerli = []
gecersiz = []
tahminler = {"gecerli":gecerli,"gecersiz":gecersiz}
print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
tahmin = int(input("Bir sayı giriniz"))
while True:
    if taban <= tahmin <= tavan:
        print(f"Tahmin geçerli aralıkta")
        gecerli.append(tahmin)
        break
    else:
        print(f"Tahmin aralığı dışında geçersiz tahmin")
        print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
        gecersiz.append(tahmin)
        tahmin = int(input("Bir sayı giriniz"))
while tahmin != sayi:
    if tahmin > sayi:
        print("Tahmin Başarısız Keşke küçük bir sayı söyleseydin")
        tavan = tahmin
    elif tahmin < sayi:
        print("Tahmin Başarısız Keşke büyük bir sayı söyleseydin")
        taban = tahmin
    while True:
        if taban < tahmin < tavan:
            print(f"Tahmin geçerli aralıkta")
            gecerli.append(tahmin)
            break
        else:
            print(f"Tahmin aralığı dışında geçersiz tahmin")
            print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
            gecersiz.append(tahmin)
            tahmin = int(input("Bir sayı giriniz"))
else:
    print("Tahmin Başarılı tebrikler")
print(tahminler)
print(tahmin.get("geçerli"))
print(tahmin.get("geçersiz"))
print(len(gecerli+gecersiz)," kerede bildiniz")