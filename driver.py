import tkinter as tk
#from add_gui import ADD_GUI
import add_gui
from rep_gui import REP_GUI
from bnc_gui import BNC_GUI

# create persistent DB if not present

# driver windor
 
driver = tk.Tk()
driver.title('Expense tracker')

btn_add = tk.Button(driver,text="Add Expenses",font=('Arial',20),command=add_gui.ADD_GUI)
btn_add.pack()

btn_report = tk.Button(driver,text="See Report",font=('Arial',20),command=REP_GUI)
btn_report.pack()

btn_balance = tk.Button(driver,text="Pay Balance",font=('Arial',20),command=BNC_GUI)
btn_balance.pack()

driver.mainloop()
