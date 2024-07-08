from db_olustur import *

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

birimler = session.query(Birim).all()
print(birimler)

birimadi = input("bir birim adi giriniz")

yeniBirim = Birim(birim_adi=birimadi)
session.add(yeniBirim)
session.commit()
birimler = session.query(Birim).all()
print(birimler)