from tkinter import ttk
from tkinter import font
from tkinter.font import Font



from yahoo_fin import stock_info
from tkinter import *
from PIL import Image, ImageTk


def stock_price():

 price = stock_info.get_live_price(e1.get())
 Current_stock.set(price)

 price2 = stock_info.get_data(e1.get())
 Current_stock2.set(price2)

master = Tk()





Current_stock = StringVar()

Current_stock2 = StringVar()

Label(master, text="Hello! Welcome to the Stocks :)").grid(row=0)
Label(master, text="Company: ").grid(row=1, sticky=E)
Label(master, text="Stock Price: ").grid(row=3, sticky=E)

Label(master, text="History: ").grid(row=7, sticky=E)


result = Label(master, text="", textvariable=Current_stock,).grid(row=3, column=1, sticky=W)

result = Label(master, text="", textvariable=Current_stock2,).grid(row=7, column=1, sticky=E)

e1 = Entry(master)
e1.grid(row=1, column=1)

b = Button(master, text="Show", command=stock_price)
b.grid(row=1, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

master.mainloop()


