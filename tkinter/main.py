import tkinter

def hello():
    print("Hello World!")

window = tkinter.Tk() # Create a window
window.title("My First GUI Program") # Set the title of the window
button = tkinter.Button(window, text = 'hello world', command=hello) # Create a button with the label "hello world"
button.pack() # Add the button in the window
window.mainloop() # Start the main event loop of the window