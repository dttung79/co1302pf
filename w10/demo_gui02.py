from tkinter import *
from tkinter import messagebox as msb

def btn_vietnamese_click():
    lbl_translate['text'] = 'Xin chao, The gioi!'

def btn_francaise_click():
    lbl_translate['text'] = 'Bonjour, le monde!'

def btn_spanish_click():
    lbl_translate['text'] = 'Hola, Mundo!'

# create a window
window = Tk()
window.title('Demo GUI 02') # set title of window
window.geometry('400x200')  # set dimension width x height

# create widgets
lbl_hello = Label(window, text='Hello, World!')
lbl_hello.grid(row=0, column=0, sticky=W)

btn_vietnamese = Button(window, text='Vietnamese', width=15, command=btn_vietnamese_click)
btn_vietnamese.grid(row=0, column=1, sticky=W)

lbl_translate = Label(window, text='')
lbl_translate.grid(row=0, column=2, sticky=W)

btn_francaise = Button(window, text='Francaise', width=15, command=btn_francaise_click)
btn_francaise.grid(row=1, column=1, sticky=W)

btn_spanish = Button(window, text='Spanish', width=15, command=btn_spanish_click)
btn_spanish.grid(row=2, column=1, sticky=W)


window.mainloop()