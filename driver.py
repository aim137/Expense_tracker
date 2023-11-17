import tkinter as tk
from expensetracker.gui.add_gui import ADD_GUI
from expensetracker.gui.rep_gui import REP_GUI
from expensetracker.gui.bnc_gui import BNC_GUI

def run():
  # driver window
  driver = tk.Tk()
  driver.geometry("229x237")
  driver.title('Expense tracker')
  
  btn_add = tk.Button(driver,text="Add Expenses",font=('Arial',20),command=ADD_GUI)
  btn_add.pack(padx=20,pady=20)
  
  btn_balance = tk.Button(driver,text="Pay Balance",font=('Arial',20),command=BNC_GUI)
  btn_balance.pack(padx=20,pady=20)
  
  btn_report = tk.Button(driver,text="See Report",font=('Arial',20),command=REP_GUI)
  btn_report.pack(padx=20,pady=20)
  
  driver.mainloop()

if __name__ == "__main__":
  run()