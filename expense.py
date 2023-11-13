import datetime

class Expense:

  def __init__(self,item=None,category=None,amount=None,ipf=None,spf=0.5,date=None,comment=None):
    """
    Expense class, example, {item='Tesco',category='groceries',amount=37,ipf=1}
    ipf stands for 'I paid fraction' and it should be 1 (0) if I (your partner) paid.
    spf stands for 'should've paid fraction' and it's 0.5 if the cost is spread evenly.
    when calculating the balance, we do amount*(ipf - spf) (positive means your partner owes you)
    """
#   if item is None or amount is None or ipf is None: raise NameError("The fields item, amount and ipf are mandatory")    
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
      self.comment = '-'

    self.ipf = ipf
    self.spf = spf
   


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
    self.comment = '-'
  
  
  def add_to_df(self,df):
    if self.item == '-' : raise NameError("The field item is mandatory")
    if self.category == '-' : raise NameError("The field category is mandatory")
    if self.amount == 0.00 : raise NameError("The field amount must be greater than zero")
    if self.item == '-' : raise NameError("The field ipf is mandatory")
    if (ipf < 0 ) or (ipf > 1): raise ValueError("ipf should be between 0 and 1")
    self.balance = self.amount*(self.ipf - self.spf)
    #and now add to the df
