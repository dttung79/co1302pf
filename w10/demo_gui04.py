from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window

def calculate(op):
    a = float(txt_a.get())
    b = float(txt_b.get())
    if op == '+': c = a + b
    elif op == '-': c = a - b
    elif op == 'x': c = a * b
    elif op == '/': c = a / b

    # set text of txt_result
    txt_result.delete(0, END)   # clear old text
    txt_result.insert(0, c)     # insert new text
    
def btn_add_click():
    calculate('+')

def btn_sub_click():
    calculate('-')

def btn_mul_click():
    calculate('x')

def btn_div_click():
    calculate('/')

window = create_window('Demo GUI 04', 400, 300)

lbl_a = Label(window, text='a:')
lbl_a.grid(row=0, column=0, sticky=E, padx=10, pady=10)

txt_a = Entry(window, width=25)
txt_a.grid(row=0, column=1, sticky=W, padx=10, pady=10, columnspan=4)

lbl_b = Label(window, text='b:')
lbl_b.grid(row=1, column=0, sticky=E, padx=10, pady=10)

txt_b = Entry(window, width=25)
txt_b.grid(row=1, column=1, sticky=W, padx=10, pady=10, columnspan=4)

btn_add = Button(window, text='+', command=btn_add_click)
btn_add.grid(row=2, column=1, sticky=E, padx=10, pady=10)

btn_sub = Button(window, text='-', command=btn_sub_click)
btn_sub.grid(row=2, column=2, sticky=W, padx=10, pady=10)

btn_mul = Button(window, text='x', command=btn_mul_click)
btn_mul.grid(row=2, column=3, sticky=E, padx=10, pady=10)

btn_div = Button(window, text='/', command=btn_div_click)
btn_div.grid(row=2, column=4, sticky=W, padx=10, pady=10)

lbl_result = Label(window, text='c:')
lbl_result.grid(row=3, column=0, sticky=E, padx=10, pady=10)

txt_result = Entry(window, width=25)
txt_result.grid(row=3, column=1, sticky=W, padx=10, pady=10, columnspan=4)


window.mainloop()