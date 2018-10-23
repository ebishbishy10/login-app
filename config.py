from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base ,User

engine =create_engine('sqlite:///userData.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
# myfirst = User(username='mohammedGamal' ,email='elbishbishy10@gmail.com',password='a7aa7aa7a')
# session.add (myfirst)
# session.commit()
session.query(User).all()
