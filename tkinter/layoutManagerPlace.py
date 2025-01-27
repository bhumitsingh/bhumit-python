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

priceperitem_label.place(x=0, y=0)
priceperitem_entry.place(x=100, y=0)
numberofitems_label.place(x=0, y=20)
numberofitems_entry.place(x=100, y=20)
totalprice_label.place(x=0, y=40)
totalprice_entry.place(x=100, y=40)
calculate_button.place(x=0, y=60)

window.mainloop()