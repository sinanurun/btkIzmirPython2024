# teşekkür takdir
puan = int(input("Ortalamanızı giriniz : "))
if puan < 70 :
    print("Belge alamazsınız")
elif puan < 85: # else + if => elif
    print("Teşekkür alabilirsiniz")
elif puan <= 100:
    print("Takdir alabilirisiniz")
else:
    print("Geçerli bir puan girmediniz")