import tkinter as tk

def actualizar_label(texto):
  global btn3
  btn3['text'] = texto

root = tk.Tk()

labelaa = 'pre'

btn1=tk.Button(text="Hola", command= lambda: actualizar_label('Hola'))
btn2=tk.Button(text="Chau", command= lambda: actualizar_label('Chau'))

btn3=tk.Button(text='--')

btn1.pack()
btn2.pack()
btn3.pack()

root.mainloop()
