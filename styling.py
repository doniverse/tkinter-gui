from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(themename="darkly")

root.title("TTK Bootstrap!")
# root.iconbitmap("images/codemy.ico")
root.geometry('500x350')

# Style 
my_style = tb.Style()
my_style.configure('success.Outline.TButton', font=("Helvatica", 18))

# Create a button
my_button = tb.Button(text="Hello, World!", bootstyle="success", style="success.Outline.TButton")
my_button.pack(pady=40)


root.mainloop()