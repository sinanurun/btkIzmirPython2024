from orm_db import *

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()