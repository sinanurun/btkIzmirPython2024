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
