# ehliyet alma programı
d_yili = int(input("Doğum yılınızı giriniz: "))
yas = 2024 - d_yili
if yas >= 18 :
    print("Ehliyet alabilirsiniz")
else:
    print("Ehliyet Alamazsınız Yaşınız Tutmuyor")
    print(f"Ehliyet Alamazsınız {yas} yaşındasınız")
    print(f"{18-yas} kadar daha beklemeniz gerekmektedir")