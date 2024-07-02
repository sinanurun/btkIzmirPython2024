# while döngüsü koşul geçerli olduğu sürece tekrar eder
adet = int(input("kaç dilim pizza istersiniz"))
dilim = adet
#yontem 1
while adet > 0:
    print("pizzanız geldi afiyet olsun")
    adet -= 1
 #yontem2
i = 1
while dilim >= i:
    print(i,".pizzanız geldi afiyet olsun")
    i += 1
