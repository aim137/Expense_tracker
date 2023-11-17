import tkinter as tk
from expensetracker.xp.expense import Expense
from expensetracker.xp import defaults
from expensetracker.xp.functions import load_sqlsession
from tkinter.messagebox import showinfo


class BNC_GUI():

  def __init__(self):
    
    self.root = tk.Tk()
    self.root.geometry("469x230")
    self.root.title("Calculate balance")

    self.session = load_sqlsession()
    self.query,self.lof_exp = self.get_unpaid_data()
    self.total_balance = self.calculate_balance()

    self.label_balance = tk.Label(self.root,text=f'Balance: {self.total_balance:.2f} GPB',font=('Arial',18))
    self.label_balance.pack(padx=20,pady=20)
    if self.total_balance > 0:
      _text = f'In favour of {defaults.name1}'
    elif self.total_balance < 0:
      _text = f'In favour of {defaults.name2}'
    else:
      _text = f'Even steven!'

    self.label_who = tk.Label(self.root, text=_text,font=('Arial',18))
    self.label_who.pack(padx=20,pady=20)
    
    buttonframe_paid = tk.Frame(self.root)
    buttonframe_paid.columnconfigure(0,weight=1)
    buttonframe_paid.columnconfigure(1,weight=1)
    self.back_btn = tk.Button(buttonframe_paid,text="Go back",command=self.root.destroy,font=('Arial',18)) 
    self.back_btn.grid(row=0,column=0,sticky=tk.W+tk.E)
    self.paid_btn = tk.Button(buttonframe_paid,text="Mark as paid",command=self.mark_as_paid,font=('Arial',18)) 
    self.paid_btn.grid(row=0,column=1,sticky=tk.W+tk.E)
    buttonframe_paid.pack(padx=20,pady=20,fill='x')


    self.root.mainloop()

  def get_unpaid_data(self):
    _q =  self.session.query(Expense).filter(Expense.is_paid == False)
    _l = _q.all()
    return _q,_l
    
  def calculate_balance(self):
    _balance = 0 
    for i in self.lof_exp:
      _balance += i.balance
    return _balance

  def mark_as_paid(self):
    self.query.update({Expense.is_paid :True})#,synchronize_session='evaluate')
    self.session.commit()


    self.root.destroy()


if __name__ == '__main__':
  BNC_GUI()
