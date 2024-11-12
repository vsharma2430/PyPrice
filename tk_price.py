from tkinter import *
from base.stock_price import *

def stock_price():
    try:
        price = get_stock_price_print(e1.get())
        Current_stock.set(f'{price}')
    finally:
        Current_stock.set(f'Failed')


if(__name__ == '__main__'):
    master = Tk()
    Current_stock = StringVar()
    Label(master, text="Symbol : ").grid(row=0, sticky=W)
    Label(master, text="Price : ").grid(row=3, sticky=W)
    result2 = Label(master, text="", textvariable=Current_stock,).grid(row=3, column=1, sticky=W)
    
    e1 = Entry(master)
    e1.grid(row=0, column=1)
    b = Button(master, text="Show", command=stock_price)
    b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)
    mainloop()