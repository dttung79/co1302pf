from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window

def btn_invoice_click():
    # get product name
    product = txt_product.get()
    # get price
    price = float(txt_price.get())
    # get quantity
    qty = int(txt_qty.get())
    # total price
    total = price * qty
    invoice = f'{product}: ${total:.2f}'
    
    lbl_invoice['text'] = invoice

window = create_window('Demo GUI 03', 400, 200)
# create widgets
lbl_product = Label(window, text='Product')
lbl_product.grid(row=0, column=0, sticky=E)

txt_product = Entry(window, width=20)
txt_product.grid(row=0, column=1, sticky=W)

lbl_price = Label(window, text='Price')
lbl_price.grid(row=1, column=0, sticky=E)

txt_price = Entry(window, width=20)
txt_price.grid(row=1, column=1, sticky=W)

lbl_qty = Label(window, text='Quantity')
lbl_qty.grid(row=2, column=0, sticky=E)

txt_qty = Entry(window, width=20)
txt_qty.grid(row=2, column=1, sticky=W)

btn_invoice = Button(window, text='Invoice', width=15, command=btn_invoice_click)
btn_invoice.grid(row=3, column=1, sticky=W)

lbl_invoice = Label(window, text='$0.00')
lbl_invoice.grid(row=4, column=1, sticky=W)


window.mainloop()