import tkinter as tk
from datetime import datetime
from expensetracker.xp.expense import Expense
from expensetracker.xp.defaults import items
from expensetracker.xp.functions import load_sqlsession,get_unpaid_data
from matplotlib import pyplot as plt


class REP_GUI():

  def __init__(self):

    self.root = tk.Tk()
    self.root.geometry("469x530")
    self.root.title("Report")
    self.tag = datetime.today().strftime('%Y%m%d-%H.%M.%S')

    self.session = load_sqlsession()
    self.query,self.lof_exp = get_unpaid_data(self.session)
    X,Y = self.data_by_category()

    self.save_report()

    self.labelframe_cats = tk.Frame(self.root)
    self.labelframe_cats.columnconfigure(0,weight=1)
    self.labelframe_cats.columnconfigure(1,weight=1)
    for i,(x,y) in enumerate(zip(X,Y)):
      self.label_of_one_category(i,x,y)
    self.labelframe_cats.pack()

    self.plot_pie_chart(X,Y)
    
    #Display chart here

    back_btn = tk.Button(self.root,text="Go back",command=self.root.destroy,font=('Arial',18)) 
    back_btn.pack(padx=20,pady=20,fill='x')

    self.root.mainloop()




#<><><><><><><><>

  def data_by_category(self):
    _y = [] #accumlated sums
    for _cat in items.keys():
      _lof_exp_cat = self.query.filter(Expense.category == _cat).all()
      if len(_lof_exp_cat):
        _y.append(sum([_exp.amount for _exp in _lof_exp_cat]))
      else:
        _y.append(0.00)
    return items.keys(),_y
  
  def label_of_one_category(self,i,x,y):
    amount = f'{y:.2f}'
    label_cat = tk.Label(self.labelframe_cats,text=f'{x.ljust(20)}',font=('Arial',18))
    label_cat.grid(row=i,column=0,sticky=tk.W)
    label_val = tk.Label(self.labelframe_cats,text=f'{amount.rjust(6)} GPB',font=('Arial',18))
    label_val.grid(row=i,column=1,sticky=tk.E)

  def plot_pie_chart(self,X,Y):
    fig, ax = plt.subplots()
    explode = [0.0 for i in X]
    explode[0] = 0.1
    ax.pie(Y, 
           labels=X, 
           explode=explode,
           autopct='%1.1f%%',
          )
    fig.savefig(f'Plot_{self.tag}.pdf')

  def save_report(self):
    with open(f'Report_{self.tag}.txt','w') as f:
      for exp in self.lof_exp:
        f.write(exp.__repr__()+'\n')

if __name__ == "__main__":
  REP_GUI()
