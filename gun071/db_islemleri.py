from orm_db import *

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def birimListele():
    birimler = session.query(Birim).all()
    for birim in birimler:
        print(birim.birim_id, birim.birim_adi)
    return birimler

def birimEkle():
    birimadi = input("bir birim adi giriniz")
    yeniBirim = Birim(birim_adi=birimadi)
    session.add(yeniBirim)
    session.commit()

def birimGuncelle():
    birimListele()
    birimid = int(input("Güncellemek istediğiniz birimin idsi giriniz"))
    birim = session.query(Birim).filter(Birim.birim_id == birimid).first()
    yeni_birim_adi = input("Yeni birim adini giriniz")
    birim.birim_adi = yeni_birim_adi
    session.commit()
    return birimListele()

def birimSil():
    birimListele()
    birimid = int(input("Silmek istediğiniz birimin idsi giriniz"))
    birim = session.query(Birim).filter(Birim.birim_id == birimid).delete()
    session.commit()
    return birimListele()


birimGuncelle()
birimSil()

