from tkinter import *
from tkinter import messagebox as msb

# define event handler for button OK
def btn_ok_click():
    msb.showinfo('OK', 'You clicked OK button')

def btn_show_python_click():
    # get text from label
    s = lbl_python['text']
    msb.showinfo('Info', s)

def btn_swap_click():
    # get text from label hello
    s1 = lbl_hello['text']
    # get text from label python
    s2 = lbl_python['text']
    # swap text
    lbl_hello['text'] = s2
    lbl_python['text'] = s1
    
# create a window
window = Tk()
window.title('Demo GUI 01') # set title of window
window.geometry('300x200')  # set dimension width x height
# create widgets
lbl_hello = Label(window, text='Hello, World!')
# place widget on window
lbl_hello.grid(row=0, column=0, sticky=W)
# run the window

lbl_python = Label(window, text='Python is fun!')
lbl_python.grid(row=1, column=1, sticky=E)

btn_ok = Button(window, text='OK', command=btn_ok_click)
btn_ok.grid(row=0, column=1, sticky=E)

btn_python = Button(window, text='Show Python', command=btn_show_python_click)
btn_python.grid(row=0, column=2, sticky=W)

btn_swap = Button(window, text='Swap', command=btn_swap_click)
btn_swap.grid(row=0, column=3, sticky=W)

# run window
window.mainloop()