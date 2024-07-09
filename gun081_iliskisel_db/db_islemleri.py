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
        kitaplar = session.query(Kitaplik).filter(Kitaplik.kitap_user==int(k_id)).all()
        # print(kitaplar)
        if len(kitaplar) > 0:
            for kitap in kitaplar:
                print(kitap.kitap_adi)
            return kitaplar
        else:
            print("Kitapliğiniz boş")
            return False
    except Exception as e:
        print(e)
        return False

def kitap_ekle(k_adi,k_sayfa_sayisi,user_id):
    try:
        yeni_kitap = Kitaplik(kitap_user=user_id,kitap_adi=k_adi,
                              kitap_sayfa_sayisi=int(k_sayfa_sayisi))
        session.add(yeni_kitap)
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False

def kitap_sil(kitap_id):
    try:
        session.query(Kitaplik).filter(Kitaplik.kitap_id==kitap_id).delete()
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False

k_adi = input("kullanıcı adı giriniz")
k_sifre = input("kullanıcı şifre giriniz")
kullanici = kGirisi(k_adi,k_sifre)
kitap_listele(kullanici.user_id)
# kitap_adi = input("ad")
# kitap_ss = int(input("sayfa"))
# kitap_ekle(kitap_adi,kitap_ss,kullanici.user_id)