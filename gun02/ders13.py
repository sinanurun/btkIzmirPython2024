# temel string yani karakter dizisi işlemleri
ad = "besteakıllılar"
print(len(ad)) # stringin boyutunu verir
print(ad[0]) # ad[x] x index değerini döndürür
print(ad[-1]) # soldan sağa 0,1,2,3, sağdan sola -1,-2,-3,,,,
print(ad[4],ad[-2])
print(ad[0:5]) # ad[bas,bitis]
print(ad[:5])
print(ad[-9:])
print(ad[::2]) # ad[bas,bitis,artis] baştan sona atlayarak
print(ad[::-1])
print(ad[3:8:2])
print(ad[-8:-3:2])
print("b" in ad)
print("bes" in ad)
print("besk" in ad)
print(ad[-1:-10:-1])


