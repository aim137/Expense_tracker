import tkinter as tk
import expense
import defaults
from expense import Expense
from functions import load_sqlsession

current_expense = Expense()

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
class ADD_GUI:

  def __init__(self,name1='Gary',name2='Karen'):
    
    self.root = tk.Tk()
    self.root.geometry("469x575")
    self.root.title("Add expenses")
    self.list_of_expenses = []
    self.name1 = name1
    self.name2 = name2
    current_expense.amount_string = ''
    
    
    # Category
    label_cat = tk.Label(self.root, text="Choose category:",font=('Arial',18))
    label_cat.pack()
    
    buttonframe_cat = tk.Frame(self.root)
    buttonframe_cat.columnconfigure(0,weight=1)
    buttonframe_cat.columnconfigure(1,weight=1)
    
    btn_cat1 = tk.Button(buttonframe_cat, text="Bills",     command=lambda: self.pre_populate_category("Bills"))
    btn_cat1.grid(row=0,column=1,sticky=tk.W+tk.E)
    btn_cat2 = tk.Button(buttonframe_cat, text="Groceries", command=lambda: self.pre_populate_category("Groceries"))
    btn_cat2.grid(row=0,column=2,sticky=tk.W+tk.E)
    btn_cat3 = tk.Button(buttonframe_cat, text="Transport", command=lambda: self.pre_populate_category("Transport"))
    btn_cat3.grid(row=0,column=3,sticky=tk.W+tk.E)
    btn_cat4 = tk.Button(buttonframe_cat, text="Memberships", command=lambda: self.pre_populate_category("Memberships"))
    btn_cat4.grid(row=1,column=1,sticky=tk.W+tk.E)
    btn_cat5 = tk.Button(buttonframe_cat, text="Leisure",   command=lambda: self.pre_populate_category("Leisure"))
    btn_cat5.grid(row=1,column=2,sticky=tk.W+tk.E)
    btn_cat6 = tk.Button(buttonframe_cat, text="Other",     command=lambda: self.pre_populate_category("Other"))
    btn_cat6.grid(row=1,column=3,sticky=tk.W+tk.E)
    
    buttonframe_cat.pack(fill='x')
    
    # Item
    label_item = tk.Label(self.root, text="Choose item:",font=('Arial',18))
    label_item.pack()

    buttonframe_item = tk.Frame(self.root)
    buttonframe_item.columnconfigure(0,weight=1)
    buttonframe_item.columnconfigure(1,weight=1)
    
    self.btn_item1 = tk.Button(buttonframe_item, text='-',command=lambda: self.pre_populate_item('-'))
    self.btn_item1.grid(row=0,column=1,sticky=tk.W+tk.E)
    self.btn_item2 = tk.Button(buttonframe_item, text='-',command=lambda: self.pre_populate_item('-'))
    self.btn_item2.grid(row=0,column=2,sticky=tk.W+tk.E)
    self.btn_item3 = tk.Button(buttonframe_item, text='-',command=lambda: self.pre_populate_item('-'))
    self.btn_item3.grid(row=0,column=3,sticky=tk.W+tk.E)
    self.btn_item4 = tk.Button(buttonframe_item, text='-',command=lambda: self.pre_populate_item('-'))
    self.btn_item4.grid(row=1,column=1,sticky=tk.W+tk.E)
    self.btn_item5 = tk.Button(buttonframe_item, text='-',command=lambda: self.pre_populate_item('-'))
    self.btn_item5.grid(row=1,column=2,sticky=tk.W+tk.E)
    self.btn_item6 = tk.Button(buttonframe_item, text='-',command=lambda: self.pre_populate_item('-'))
    self.btn_item6.grid(row=1,column=3,sticky=tk.W+tk.E)
    self.btn_item7 = tk.Button(buttonframe_item, text='-',command=lambda: self.pre_populate_item('-'))
    self.btn_item7.grid(row=2,column=1,sticky=tk.W+tk.E)
    self.btn_item8 = tk.Button(buttonframe_item, text='-',command=lambda: self.pre_populate_item('-'))
    self.btn_item8.grid(row=2,column=2,sticky=tk.W+tk.E)
    self.btn_item9 = tk.Button(buttonframe_item, text='-',command=lambda: self.pre_populate_item('-'))
    self.btn_item9.grid(row=2,column=3,sticky=tk.W+tk.E)

    buttonframe_item.pack(fill='x')
    
    # Amount
    label_amount = tk.Label(self.root, text="Choose amount:",font=('Arial',18))
    label_amount.pack()
    
    buttonframe_amount = tk.Frame(self.root)
    buttonframe_amount.columnconfigure(0,weight=1)
    buttonframe_amount.columnconfigure(1,weight=1)
    
    self.btn_amount1 = tk.Button(buttonframe_amount, text='1',command=lambda: self.concatenate_amount('1'))
    self.btn_amount1.grid(row=0,column=1,sticky=tk.W+tk.E)
    self.btn_amount2 = tk.Button(buttonframe_amount, text='2',command=lambda: self.concatenate_amount('2'))
    self.btn_amount2.grid(row=0,column=2,sticky=tk.W+tk.E)
    self.btn_amount3 = tk.Button(buttonframe_amount, text='3',command=lambda: self.concatenate_amount('3'))
    self.btn_amount3.grid(row=0,column=3,sticky=tk.W+tk.E)
    self.btn_amount4 = tk.Button(buttonframe_amount, text='4',command=lambda: self.concatenate_amount('4'))
    self.btn_amount4.grid(row=1,column=1,sticky=tk.W+tk.E)
    self.btn_amount5 = tk.Button(buttonframe_amount, text='5',command=lambda: self.concatenate_amount('5'))
    self.btn_amount5.grid(row=1,column=2,sticky=tk.W+tk.E)
    self.btn_amount6 = tk.Button(buttonframe_amount, text='6',command=lambda: self.concatenate_amount('6'))
    self.btn_amount6.grid(row=1,column=3,sticky=tk.W+tk.E)
    self.btn_amount7 = tk.Button(buttonframe_amount, text='7',command=lambda: self.concatenate_amount('7'))
    self.btn_amount7.grid(row=2,column=1,sticky=tk.W+tk.E)
    self.btn_amount8 = tk.Button(buttonframe_amount, text='8',command=lambda: self.concatenate_amount('8'))
    self.btn_amount8.grid(row=2,column=2,sticky=tk.W+tk.E)
    self.btn_amount9 = tk.Button(buttonframe_amount, text='9',command=lambda: self.concatenate_amount('9'))
    self.btn_amount9.grid(row=2,column=3,sticky=tk.W+tk.E)
    self.btn_amount10 = tk.Button(buttonframe_amount, text='.',command=lambda: self.concatenate_amount('.'))
    self.btn_amount10.grid(row=3,column=1,sticky=tk.W+tk.E)
    self.btn_amount11 = tk.Button(buttonframe_amount, text='0',command=lambda: self.concatenate_amount('0'))
    self.btn_amount11.grid(row=3,column=2,sticky=tk.W+tk.E)
    self.btn_amount12 = tk.Button(buttonframe_amount, text='Del',command=self.backspace_amount)
    self.btn_amount12.grid(row=3,column=3,sticky=tk.W+tk.E)

    buttonframe_amount.pack(fill='x')
    
    #Who paid
    label_whopaid = tk.Label(self.root, text="Who paid:",font=('Arial',18))
    label_whopaid.pack()

    self.ipf = tk.IntVar() #Groups radiobuttons together if they share the same variable
    self.ipf.set(1)
    self.whopays = tk.Radiobutton(self.root,text=self.name1,variable=self.ipf,value=1)
    self.whopays.pack()
    self.whopays = tk.Radiobutton(self.root,text=self.name2,variable=self.ipf,value=0)
    self.whopays.pack()
    
    text_comment = tk.StringVar()
    text_comment.set('')
    self.entry_comment = tk.Entry(self.root,textvariable=text_comment,font=('Arial',18))
    self.entry_comment.pack()

    self.summary_label = tk.Label(self.root,text=f'Summary')
    self.summary_label.pack()
    self.category_label = tk.Label(self.root,text=f'Category: {current_expense.category}')
    self.category_label.pack()
    self.item_label = tk.Label(self.root,text=f'Item: {current_expense.item}')
    self.item_label.pack()
    self.amount_label = tk.Label(self.root,text=f'Amount: {current_expense.amount} GBP')
    self.amount_label.pack()
    self.ipf_label = tk.Label(self.root,text=f'Paid by: -')
    self.ipf_label.pack()
    

    clear_btn = tk.Button(self.root,text='Clear',command= self.clear_expense,font=('Arial',16))
    clear_btn.pack()
    add_btn = tk.Button(self.root,text='Add',command= self.add_expense_to_list,font=('Arial',16))
    add_btn.pack()

    save_btn = tk.Button(self.root,text='Save to DB',command=self.save_to_db,font=('Arial',16))
    save_btn.pack()
    close_btn = tk.Button(self.root,text='Close',command=self.close_add_gui,font=('Arial',16))
    close_btn.pack()

    self.root.mainloop()

    
#<><><><><><><><><><><><><><

  def pre_populate_category(self,_value):
    global current_expense
    if (current_expense.category != _value):
      current_expense.reset()
    current_expense.add_category(_value)

    item1,item2,item3,item4,item5,item6,item7,item8,item9 = defaults.items[_value] 
    self.btn_item1['text'] = item1      
    self.btn_item1['command'] = lambda: self.pre_populate_item(item1)
    self.btn_item2['text'] = item2      
    self.btn_item2['command'] = lambda: self.pre_populate_item(item2)
    self.btn_item3['text'] = item3      
    self.btn_item3['command'] = lambda: self.pre_populate_item(item3)
    self.btn_item4['text'] = item4      
    self.btn_item4['command'] = lambda: self.pre_populate_item(item4)
    self.btn_item5['text'] = item5      
    self.btn_item5['command'] = lambda: self.pre_populate_item(item5)
    self.btn_item6['text'] = item6      
    self.btn_item6['command'] = lambda: self.pre_populate_item(item6)
    self.btn_item7['text'] = item7      
    self.btn_item7['command'] = lambda: self.pre_populate_item(item7)
    self.btn_item8['text'] = item8      
    self.btn_item8['command'] = lambda: self.pre_populate_item(item8)
    self.btn_item9['text'] = item9      
    self.btn_item9['command'] = lambda: self.pre_populate_item(item9)
    
    self.update_summary()


  def pre_populate_item(self,_value):
    global current_expense
    if (current_expense.item != _value):
      current_expense.reset(keep_cat=True)
    current_expense.add_item(_value)
    #add default prices
    if _value in defaults.values.keys():
      current_expense.add_amount(defaults.values[_value])
    else:
      current_expense.add_amount(0.00)
    
    self.update_summary()
 
  def concatenate_amount(self,_string):
    global current_expense
    if _string == '.' and _string in current_expense.amount_string: return
    current_expense.amount_string += _string
    current_expense.amount = float(current_expense.amount_string)
    self.update_summary()
    print(current_expense.amount_string)
 
  def backspace_amount(self):
    global current_expense
    current_expense.amount_string = current_expense.amount_string[:-1]
    current_expense.amount = float(current_expense.amount_string)
    self.update_summary()


  def update_summary(self):
    global current_expense
    self.category_label['text']=f'category: {current_expense.category}'
    self.item_label['text']=f'Item: {current_expense.item}'
    self.amount_label['text']=f'Amount: {current_expense.amount:.2f} GPB'
    if self.ipf.get() == 1 : self.ipf_label['text']=f'Paid by: {self.name1}'
    if self.ipf.get() == 0 : self.ipf_label['text']=f'Paid by: {self.name2}'
  # self.entry_amount['textvariable'] = text_value
   
  def clear_expense(self):
    global current_expense
    current_expense.reset()
    current_expense.amount_string = ''
    self.update_summary()
   
  def add_expense_to_list(self):
    global current_expense
    current_expense.ipf = self.ipf.get()
    should_add = current_expense.prepare_to_save(self.name1,self.name2)
    print(current_expense)
    if should_add:
      self.list_of_expenses.append(current_expense)
      current_expense = Expense(category=current_expense.category)
      self.update_summary()
    else:
      raise ValueError
      #aim137 cambiar esto por algun mensaje

  def save_to_db(self):
    session = load_sqlsession()
    for exp in self.list_of_expenses:
      session.add(exp)
    session.commit()
    self.saved_ok = True

  def close_add_gui(self):
    if self.saved_ok:
      self.root.destroy()
    else:
      pass
      #aim137 cambiar esto por algun mensaje


#><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
if __name__ == '__main__':
  ADD_GUI()
