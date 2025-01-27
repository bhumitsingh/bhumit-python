'''
mainloop() -
    - Event Loop: mainloop() keeps the window open and responsive. Without it, your GUI would display and immediately close.
    - Listening for Events: It waits for the user to interact with the GUI and processes those interactions.
    - Infinite Loop: It runs continuously until the window is closed, allowing for real-time updates and input handling.
widgets -  Tkinter provides a wide variety of widgets that you can use to create your graphical user interface (GUI). Each 
           widget serves a different purpose and allows you to interact with users in various ways. Here's an overview of 
           some of the most commonly used widgets in Tkinter, along with their key features and examples!
    - Buttons: Used to trigger actions or open new windows.
    - Labels: Display text or images.
    - Entries: Allow users to input text or numbers.
    - Checkbuttons: Used to select multiple options from a list.
    - Radiobuttons: Used to select one option from a list.
    - Menus: Allow users to select options from a dropdown menu.
    - Frames: Used to group related widgets together and improve the organization of your GUI.
    - Text Boxes: Allow users to input multi-line text.
    - Scrollbars: Used to scroll through large amounts of text or images.
    - Listboxes: Allow users to select one or multiple items from a list.
    - OptionMenus: Allow users to select one option from a list.
widget hierarchy - 
    Tkinter uses a hierarchical structure to organize widgets. This hierarchy is essential for managing and updating your GUI.
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

    print(str(button)) # Print the button object to the console

    window.mainloop()

    print("Program Ended") # Anything after the mainloop executes after the window is closed