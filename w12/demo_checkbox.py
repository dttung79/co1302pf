from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window, run

window = create_window('Demo Checkbox', 400, 200)

#### EVENT HANDLERS ####
def calculate_bill():
    total = 0
    if phone_var.get() == 1:
        total += 2000
    elif phone_var.get() == 2:
        total += 1500
    elif phone_var.get() == 3:
        total += 2500

    if cover_var.get() == True:
        total += 15
    if pen_var.get() == True:
        total += 30
    if film_var.get() == True:
        total += 5

    lbl_bill.config(text=f'Total bill: ${total}')
    
#### GUI SETUP ####
lbl_phone = Label(window, text='Select a phone:')
lbl_phone.grid(row=0, column=0, padx=5, pady=5, sticky=W)

lbl_accessories = Label(window, text='Select accessories:')
lbl_accessories.grid(row=0, column=1, padx=5, pady=5, sticky=W)

phone_var = IntVar()

rd_iphone16 = Radiobutton(window, text='iPhone 16 ($2000)', 
                          variable=phone_var, value=1, command=calculate_bill)
rd_iphone16.grid(row=1, column=0, padx=5, pady=5, sticky=W)

rd_iphone15 = Radiobutton(window, text='iPhone 15 ($1500)', 
                          variable=phone_var, value=2, command=calculate_bill)
rd_iphone15.grid(row=2, column=0, padx=5, pady=5, sticky=W)

rd_samsung = Radiobutton(window, text='Samsung Fold 6 ($2500)', 
                         variable=phone_var, value=3, command=calculate_bill)
rd_samsung.grid(row=3, column=0, padx=5, pady=5, sticky=W)

cover_var = BooleanVar()
chk_cover = Checkbutton(window, text='Cover ($15)', 
                        variable=cover_var, command=calculate_bill)
chk_cover.grid(row=1, column=1, padx=5, pady=5, sticky=W)

pen_var = BooleanVar()
chk_pen = Checkbutton(window, text='Pen ($30)', 
                      variable=pen_var, command=calculate_bill)
chk_pen.grid(row=2, column=1, padx=5, pady=5, sticky=W)

film_var = BooleanVar()
chk_film = Checkbutton(window, text='Film ($5)', 
                       variable=film_var, command=calculate_bill)
chk_film.grid(row=3, column=1, padx=5, pady=5, sticky=W)

lbl_bill = Label(window, text='Total bill: $0')
lbl_bill.grid(row=4, column=0, padx=5, pady=5, sticky=W, columnspan=2)

#### RUN ####
run(window)