def kisiel_bilgi_karti(**kwargs):
    print(kwargs["ad"], kwargs["soyad"])
    if "bolum" in kwargs.keys():
        print(kwargs["bolum"])

kisiel_bilgi_karti(ad="ali",soyad="can",bolum = "YBS")
kisiel_bilgi_karti(soyad="velican",ad="veli")