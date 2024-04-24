from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(themename="darkly")

root.title("TTK Bootstrap!")
# root.iconbitmap("images/codemy.ico")
root.geometry('500x350')

# Create a function for the Button
counter = 0
def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        my_label.config(text = "Hello World!")
    else:
        my_label.config(text="Goodbye Milko!")




# Create a Label
my_label = tb.Label(text="Hello, World!", font=("Helvatica", 28), bootstyle="default, inverse")
my_label.pack(pady= 50)

# Create a button
my_button = tb.Button(text="Click Me!", width=40, bootstyle="success, outline", command = changer)
my_button.pack(pady=20)


root.mainloop()