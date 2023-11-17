from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from expensetracker.xp.expense import Base, Expense
from expensetracker.xp import defaults

def load_sqlsession():
  engine = create_engine(f"sqlite:///{defaults.db_path}/{defaults.db_name}",echo=True)
  #if it is the first time
  Base.metadata.create_all(bind=engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  return session

def get_unpaid_data(session):
  _q =  session.query(Expense).filter(Expense.is_paid == False)
  _l = _q.all()
  return _q,_l