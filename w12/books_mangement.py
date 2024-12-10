from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window, run
from tkinter import filedialog
import csv

window = create_window('Demo Checkbox', 650, 300)
names = []
authors = []
prices = []

#### EVENT HANDLERS ####
def btn_load_click():
    try:
        book_file = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
        reader = csv.reader(open(book_file, 'r'))
        next(reader)  # skip the header

        for row in reader:
            lst_books.insert(END, row[0])
            names.append(row[0])
            authors.append(row[1])
            prices.append(row[2])

    except FileNotFoundError:
        msb.showerror('Error', 'File not found')
        return

def lst_books_select(event):
    select_index = lst_books.curselection()[0]  # get selected index from listbox
    name = names[select_index]
    author = authors[select_index]
    price = prices[select_index]

    set_text(txt_name, name)
    set_text(txt_author, author)
    set_text(txt_price, price)

def set_text(txt, text):
    txt.delete(0, END)
    txt.insert(0, text)

def btn_add_click():
    if txt_name.get() == '' or txt_author.get() == '' or txt_price.get() == '':
        msb.showerror('Error', 'Please fill in all fields')
        return
    
    name = txt_name.get()
    author = txt_author.get()
    try:
        price = int(txt_price.get())
    except ValueError:
        msb.showerror('Error', 'Price must be a number')
        return

    names.append(name)
    authors.append(author)
    prices.append(price)

    lst_books.insert(END, name)

    msb.showinfo('Info', f'Book {name} added successfully')

def btn_edit_click():
    # get selected index
    sel_index = lst_books.curselection()[0]
    if sel_index == -1:
        msb.showerror('Error', 'Please select a book')
        return
    # get new values from textboxes
    name = txt_name.get()
    author = txt_author.get()
    price = int(txt_price.get())
    # update the lists
    names[sel_index] = name
    authors[sel_index] = author
    prices[sel_index] = price
    # update the listbox
    lst_books.delete(sel_index)
    lst_books.insert(sel_index, name)

    msb.showinfo('Info', f'Book {name} updated successfully')

def btn_delete_click():
    # get selected index
    sel_index = lst_books.curselection()[0]
    if sel_index == -1:
        msb.showerror('Error', 'Please select a book')
        return
    name = names.pop(sel_index)
    author = authors.pop(sel_index)
    price = prices.pop(sel_index)
    # update the listbox
    lst_books.delete(sel_index)

    msb.showinfo('Info', f'Book {name} deleted successfully')

def btn_save_click():
    try:
        book_file = filedialog.asksaveasfilename(filetypes=[('CSV files', '*.csv')])
        writer = csv.writer(open(book_file, 'w', newline=''))
        writer.writerow(['Name', 'Author', 'Price'])
        for i in range(len(names)):
            writer.writerow([names[i], authors[i], prices[i]])

        msb.showinfo('Info', 'Books saved successfully')
    except FileNotFoundError:
        msb.showerror('Error', 'File not found')

#### GUI SETUP ####
lbl_books = Label(window, text='Select books:')
lbl_books.grid(row=0, column=0, padx=5, pady=5, sticky=W)

lst_books = Listbox(window, selectmode=SINGLE, width=30, height=10, exportselection=0)
lst_books.grid(row=1, column=0, padx=5, pady=5, sticky=W, rowspan=4, columnspan=2)
lst_books.bind('<<ListboxSelect>>', lst_books_select)

lbl_details = Label(window, text='Book details:')
lbl_details.grid(row=0, column=2, padx=5, pady=5, sticky=W, columnspan=4)

lbl_name = Label(window, text='Name:')
lbl_name.grid(row=1, column=2, padx=5, pady=5, sticky=W)

txt_name = Entry(window, width=30)
txt_name.grid(row=1, column=3, padx=5, pady=5, sticky=W, columnspan=3)

lbl_author = Label(window, text='Author:')
lbl_author.grid(row=2, column=2, padx=5, pady=5, sticky=W)

txt_author = Entry(window, width=30)
txt_author.grid(row=2, column=3, padx=5, pady=5, sticky=W, columnspan=3)

lbl_price = Label(window, text='Price:')
lbl_price.grid(row=3, column=2, padx=5, pady=5, sticky=W)

txt_price = Entry(window, width=30)
txt_price.grid(row=3, column=3, padx=5, pady=5, sticky=W, columnspan=3)

btn_add = Button(window, text='Add', width=5, command=btn_add_click)
btn_add.grid(row=4, column=3, padx=5, pady=5, sticky=W)

btn_edit = Button(window, text='Edit', width=5, command=btn_edit_click)
btn_edit.grid(row=4, column=4, padx=5, pady=5, sticky=W)

btn_delete = Button(window, text='Delete', width=5, command=btn_delete_click)   
btn_delete.grid(row=4, column=5, padx=5, pady=5, sticky=W)

btn_load = Button(window, text='Load', width=5, command=btn_load_click)
btn_load.grid(row=5, column=0, padx=5, pady=5, sticky=W)

btn_save = Button(window, text='Save', width=5, command=btn_save_click)
btn_save.grid(row=5, column=1, padx=5, pady=5, sticky=E)

btn_exit = Button(window, text='Exit', width=5, command=window.destroy)
btn_exit.grid(row=5, column=5, padx=5, pady=5, sticky=E)
#### RUN ####

run(window)