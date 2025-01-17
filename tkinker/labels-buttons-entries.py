import tkinter

if __name__ == "__main__":
    window = tkinter.Tk()
    def printentry():
        print(textentry.get())
    window.title("My First GUI")
    window.geometry("800x600")

    label = tkinter.Label(window, text="Hello, World!", bg="orange", fg= "blue", width=50)
    label.pack()
    textentry = tkinter.Entry(window)
    textentry.pack()
    button = tkinter.Button(window, text = "Hello", bg="yellow" , activebackground="blue", activeforeground="white", command=printentry)
    button.pack()

    window.mainloop()