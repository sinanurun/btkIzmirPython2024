#yeme sipariş uygulaması
yemek = input("Yemek bilgisi giriniz:")
if yemek=="pide":
    icecek = input("Icecek bilgisi giriniz:")
    if icecek == "ayran":
        print("sipariş doğru")
    else:
        print("yemek doğru içecek yanlış")
else:
    print("sipariş yanlış")


