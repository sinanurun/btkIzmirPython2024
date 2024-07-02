# teşekkür takdir
puan = int(input("Ortalamanızı giriniz : "))
if puan < 70 :
    print("Belge alamazsınız")
else:
    if puan < 85:
        print("Teşekkür alabilirsiniz")
    else:
        if puan <= 100:
            print("Takdir alabilirisiniz")
        else:
            print("Geçerli bir puan girmediniz")