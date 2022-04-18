import sys
from tkinter import *


# Defining a function to be performed by button
def onclick():
    exec(open('AiVirtualMouse.py').read())


def onstop():
    root.quit()
    sys.exit()


root = Tk()
root.title("HandyMouse")

# Creating label widget
label = Label(root, text="AI Virtual Mouse")

# Creating a button
button = Button(root, text="Start", padx=30, command=onclick, fg="white", bg="red")

button2 = Button(root, text="Exit", padx=30, command=onstop, fg="white", bg="red")

# Showing on the screen
label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
button.grid(row=1, column=0, pady=10)
button2.grid(row=1, column=1, pady=10)

root.mainloop()
