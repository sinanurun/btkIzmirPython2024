def ogrencKarti(**kwargs):
    print(kwargs)
    o_bilgileri = {**kwargs}
    print(o_bilgileri)
    pass

ogrencKarti(oAdi="didem",oSoyadi="bozyel",oBolum="ekonometri")