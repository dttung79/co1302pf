from tkinter import *

def create_window(title, width, height):
    window = Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    return window

def run(window):
    window.mainloop()