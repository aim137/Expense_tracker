from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from expensetracker.xp.expense import Base
from expensetracker.xp import defaults

def load_sqlsession():
  engine = create_engine(f"sqlite:///{defaults.db_name}",echo=True)
  #if it is the first time
  Base.metadata.create_all(bind=engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  return session
  

