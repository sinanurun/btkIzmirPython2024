#veri tabanı oluşturma
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *  #tablolar arası ilişki kurmak için
from sqlalchemy import *

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True,autoincrement=True)
    user_adi = Column(String(100), nullable=False)
    user_sifre = Column(String(100), nullable=False)
    def __repr__(self):
        return f'{self.user_id} - {self.user_adi}'

class Kitaplik(Base):
    __tablename__ = 'kitaplik'
    kitap_id = Column(Integer, primary_key=True, autoincrement=True)
    kitap_adi = Column(String(100), nullable=False)
    kitap_sayfa_sayisi = Column(Integer, nullable=False)
    kitap_user = Column(Integer, ForeignKey('user.user_id'))
# kitaplik.sqlite oluşturmak ve tanımlanana tabloları
# oluşturulan veritabanına eklemek için aşağıdaki kodları yazıyoruz
engine = create_engine('sqlite:///kitaplik.sqlite')
Base.metadata.create_all(engine)