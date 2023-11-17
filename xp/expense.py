import datetime
from expensetracker.xp import defaults
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, Boolean


Base = declarative_base()

class Expense(Base):

  __tablename__ = "Expenses"

  item     = Column("Item", String)
  category = Column("Category", String)
  amount   = Column("Amount", Float)
  ipf      = Column("Ipf", Float)
  spf      = Column("Spf", Float)
  name     = Column("Name", String)
  date     = Column("Date", String)
  comment  = Column("Comment", String)
  balance  = Column("Balance", Float)
  is_paid  = Column("IsPaid", Boolean)
  key      = Column("Key", String, primary_key=True)


  def __init__(self,item=None,category=None,amount=None,ipf=None,spf=0.5,date=None,comment=None):
    """
    Expense class, example, {item='Tesco',category='groceries',amount=37,ipf=1}
    ipf stands for 'I paid fraction' and it should be 1 (0) if I (your partner) paid.
    spf stands for 'should've paid fraction' and it's 0.5 if the cost is spread evenly.
    when calculating the balance, we do amount*(ipf - spf) (positive means your partner owes you)
    """

    if item is not None:
      self.item = item
    else:
      self.item = '-'
    if category is not None:
      self.category = category
    else:
      self.category = '-'
    if amount is not None:
      self.amount = float(amount)
    else:
      self.amount = 0.00
    if date is None:
     self.date = datetime.date.today()
    else:
     ###aim137 see what format is the date input
     pass
    if comment is not None:
      self.comment = comment
    else:
      self.comment = ''

    self.ipf = ipf
    self.spf = spf
    self.is_paid = False
    self.key = datetime.datetime.today().strftime('%Y%m%d-%H.%M.%S')
    self.amount_string = ''
    self.name = 'TBD'
   


  def add_category(self,cat):
    self.category = cat

  def add_item(self,item):
    self.item = item

  def add_amount(self,amount):
    self.amount = amount
   
  def add_ipf(self,ipf):
    self.ipf = ipf
 
  def reset(self,keep_cat=False):
    if not keep_cat: self.category = '-'
    self.item = '-'
    self.amount = 0.00
    self.comment = ''
    self.amount_string = ''
  
  
  def prepare_to_save(self):
    if self.item == '-' : return False
    if self.category == '-' : return False
    if self.amount == 0.00 : return False
    if self.ipf == '-' : return False
    if (self.ipf < 0 ) or (self.ipf > 1): return False
    self.balance = self.amount*(self.ipf - self.spf)
    if self.ipf == 1: self.name = defaults.name1
    if self.ipf == 0: self.name = defaults.name2
    return True
    #and now add to the df

  def __repr__(self):
    return f'{self.category.ljust(13)} {self.item.ljust(13)} : {self.amount: 8.2f} GBP paid by {self.name.ljust(10)} on {str(self.date).ljust(13)}- Net={self.balance: 8.2f} GBP Paid={self.is_paid} Comment={self.comment}'
