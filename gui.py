import tkinter as tk
import expense
import defaults
from expense import Expense

new_expense = Expense()

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
class GUI:

  def __init__(self,name1='Gary',name2='Karen'):
    
    self.root = tk.Tk()
    self.root.geometry("469x575")
    self.root.title("Add expenses")
    
    
    #text_item = tk.Text(self.root,height=2,width=16,font=("Arial", 24))
    #text_item.grid(columnspan=5)
    #hola = tk.Menubutton(self.root)
    #hola.grid(columnspan=5)
    
    label = tk.Label(self.root, text="Choose category:",font=('Arial',18))
    label.pack()
    
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
    
    text_value = tk.StringVar()
    text_value.set('')
    self.entry_amount = tk.Entry(self.root,textvariable=text_value,font=('Arial',18))
    self.entry_amount.pack()

    ipf = tk.IntVar() #Groups radiobuttongs together if they share the same variable
    ipf.set(1)
    self.whopays = tk.Radiobutton(self.root,text=name1,variable=ipf,value=1)
    self.whopays.pack()
    self.whopays = tk.Radiobutton(self.root,text=name2,variable=ipf,value=0)
    self.whopays.pack()
    
    text_comment = tk.StringVar()
    text_comment.set('')
    self.entry_comment = tk.Entry(self.root,textvariable=text_comment,font=('Arial',18))
    self.entry_comment.pack()

    self.summary_label = tk.Label(self.root,text=f'Summary')
    self.summary_label.pack()
    self.category_label = tk.Label(self.root,text=f'Category: {new_expense.category}')
    self.category_label.pack()
    self.item_label = tk.Label(self.root,text=f'Item: {new_expense.item}')
    self.item_label.pack()
    self.amount_label = tk.Label(self.root,text=f'Amount: {new_expense.amount} GBP')
    self.amount_label.pack()
    self.ipf_label = tk.Label(self.root,text=f'Paid by: -')
    self.ipf_label.pack()
    

    clear_btn = tk.Button(self.root,text='Clear',command= self.clear_expense,font=('Arial',16))
    clear_btn.pack()
    add_btn = tk.Button(self.root,text='Add',command= self.add_expense_to_df,font=('Arial',16))
    add_btn.pack()

    self.root.mainloop()

    
#<><><><><><><><><><><><><><

  def pre_populate_category(self,_value):
    print('----')
    if (new_expense.category != _value):
      new_expense.reset()
    new_expense.add_category(_value)

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
    if (new_expense.item != _value):
      new_expense.reset(keep_cat=True)
    new_expense.add_item(_value)
    #add default prices
    if _value in defaults.values.keys():
      new_expense.add_amount(defaults.values[_value])
    else:
      new_expense.add_amount(0.00)
    
    self.update_summary()

  def update_summary(self):
    self.category_label['text']=f'category: {new_expense.category}'
    self.item_label['text']=f'Item: {new_expense.item}'
    text_value = tk.StringVar()
    text_value.set(new_expense.amount)
    self.amount_label['text']=f'Amount: {text_value.get()} GPB'
    self.ipf_label['text']=f'Paid by: {text_value.get()} GPB'
    self.entry_amount['textvariable'] = text_value
   
  def clear_expense(self):
    new_expense.reset()
    self.update_summary()
   
  def add_expense_to_df(self):
    print(f'{self.entry_amount.get()}     {new_expense.amount}')
    pass
    #call new_expense.add_to_df(self.df) , i.e., passing self.df to it.


#><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
GUI(name1='ElPeri',name2='LaPira')
