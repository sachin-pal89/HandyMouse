import sys
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("HandyMouse")
root.geometry("400x400")

WIDTH = 400
HEIGHT = 400


def onstop():
    root.quit()
    sys.exit()


# Defining a function to be performed by button
def onclick():
    exec(open('AiVirtualMouse.py').read())


canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack(fill="both", expand=True)

background_photo = (Image.open('aiHand.png'))
resized_image = background_photo.resize((430, 430), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
background = canvas.create_image(0, 0, image=new_image, anchor=NW)

my_text = canvas.create_text(220, 40, text="AI Virtual Mouse", font=("Helvetica", 20), fill="white")

button = Button(root, text="Start", padx=40, pady=5, command=onclick, fg="white", bg="green")

button2 = Button(root, text="Exit", padx=40, pady=5, command=onstop, fg="white", bg="red")

my_button1 = canvas.create_window(30, 200, anchor="w", window=button)

my_button2 = canvas.create_window(370, 200, anchor="e", window=button2)

root.mainloop()
