import tkinter

def computePrice():
    totalprice = int(priceperitem_entry.get())*int(numberofitems_entry.get())
    totalprice_entry.insert(0, string=str(totalprice))

window = tkinter.Tk()
priceperitem_label = tkinter.Label(window, text = "Price per item")
priceperitem_entry = tkinter.Entry(window)
numberofitems_label = tkinter.Label(window, text = "Number of items")
numberofitems_entry = tkinter.Entry(window)
totalprice_label = tkinter.Label(window, text = "Total price")
totalprice_entry = tkinter.Entry(window)
calculate_button = tkinter.Button(window, text = 'Calculate Total' , command = computePrice)

priceperitem_label.pack()
priceperitem_entry.pack()
numberofitems_label.pack()
numberofitems_entry.pack()
totalprice_label.pack(side='left',)
totalprice_entry.pack(side='right',)
calculate_button.pack(fill='x')

window.mainloop()
