from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from expense import Base

def load_sqlsession():
  engine = create_engine("sqlite:///_expenses.db",echo=True)
  #if it is the first time
  Base.metadata.create_all(bind=engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  return session
  

