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

priceperitem_label.grid(row=0, column=0)
priceperitem_entry.grid(row=0, column=1)
numberofitems_label.grid(row=1, column=0)
numberofitems_entry.grid(row=1, column=1)
totalprice_label.grid(row=2, column=0)
totalprice_entry.grid(row=2, column=1)
calculate_button.grid(row=3, column=0)

window.mainloop()