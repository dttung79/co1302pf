from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window, run

window = create_window('Demo Radio', 400, 200)

#### EVENT HANDLERS ####
def btn_buy_click():
    # get movie name
    movie = txt_movie.get()
    # get price
    price = float(txt_price.get())
    # get VIP status
    vip = vip_var.get() # 1 if Yes, 0 if No
    if vip == 1:
        price *= 0.9
    
    receipt = f'Movie: {movie}\nPrice: {price:.2f}\nDiscount: {'Yes' if vip == 1 else 'No'}'
    msb.showinfo('Receipt', receipt)
    
#### GUI SETUP ####
lbl_movie = Label(window, text='Movie:')
lbl_movie.grid(row=0, column=0, padx=5, pady=5, sticky=E)

txt_movie = Entry(window, width=15)
txt_movie.grid(row=0, column=1, padx=5, pady=5, sticky=W, columnspan=2)

lbl_price = Label(window, text='Price:')
lbl_price.grid(row=1, column=0, padx=5, pady=5, sticky=E)

txt_price = Entry(window, width=15)
txt_price.grid(row=1, column=1, padx=5, pady=5, sticky=W, columnspan=2)

lbl_vip = Label(window, text='VIP:')
lbl_vip.grid(row=2, column=0, padx=5, pady=5, sticky=E)

vip_var = IntVar()  # a variable to store the selected value
vip_var.set(0)      # 0 is the default value
rd_yes = Radiobutton(window, text='Yes', value=1, variable=vip_var)
rd_yes.grid(row=2, column=1, padx=5, pady=5, sticky=W)

rd_no = Radiobutton(window, text='No', value=0, variable=vip_var)
rd_no.grid(row=2, column=2, padx=5, pady=5, sticky=W)

btn_buy = Button(window, text='Buy', width=15, command=btn_buy_click)
btn_buy.grid(row=3, column=1, padx=5, pady=5, sticky=W, columnspan=2)

#### RUN ####
run(window)