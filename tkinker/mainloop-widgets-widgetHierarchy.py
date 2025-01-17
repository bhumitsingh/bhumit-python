'''
mainloop() -
    Event Loop: mainloop() keeps the window open and responsive. Without it, your GUI would display and immediately close.
    Listening for Events: It waits for the user to interact with the GUI and processes those interactions.
    Infinite Loop: It runs continuously until the window is closed, allowing for real-time updates and input handling.
'''
import tkinter

def hello():
    print("Hello World!")

if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Tkinter First App") # Set the title of the window
    window.geometry('600x400')

    frame = tkinter.Frame(window) # Create a frame to hold the widgets
    frame.pack()

    label = tkinter.Label(frame, text="Hello, World!") # Create a label widget
    label.pack()
    button = tkinter.Button(frame,text="Hello World", command = hello)
    button.pack()

    print(str(button))

    window.mainloop()

    print("Program Ended") # Anything after the mainloop executes after the window is closed