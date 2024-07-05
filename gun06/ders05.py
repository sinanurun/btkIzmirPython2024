# HATA AYIKLAMA
try:
    a = int(input("Enter a number: "))
except:
    print("hata var")
else:
    print("değer atama işlemi başarıyla gerçekleşti")
finally:
    print("bende çalıştım")