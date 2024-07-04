def ogrencKarti(a,b,c,d=8,*args,**kwargs):
    print(a,b,c,d)
    print(args)
    print(kwargs)
    o_bilgileri = {**kwargs}
    print(o_bilgileri)
    pass

ogrencKarti(1,2,3,4,78,96,54,32,12,58,oAdi="didem",oSoyadi="bozyel",oBolum="ekonometri")