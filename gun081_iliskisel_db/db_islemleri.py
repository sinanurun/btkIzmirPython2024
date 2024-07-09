from orm_db import *

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def kGirisi(k_adi, k_sifre):
    kullanici = (session.query(User).
                 filter(User.user_adi==k_adi,
                                User.user_sifre == k_sifre).first())
    return kullanici

def kitap_listele(k_id):
    try:
        kitaplar = session.query(Kitaplik).filter(Kitaplik.kitap_user==k_id).all()
        if len(kitaplar) > 0:
            return kitaplar
        else:
            print("Kitapliğiniz boş")
            return False
    except:
        return False

k_adi = input("kullanıcı adı giriniz")
k_sifre = input("kullanıcı şifre giriniz")
kullanici = kGirisi(k_adi,k_sifre)

kitap_listele(kullanici.user_id)