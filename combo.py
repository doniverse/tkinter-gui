from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(themename="darkly")

root.title("TTK Bootstrap!")
# root.iconbitmap("images/codemy.ico")
root.geometry('500x350')

def clicker():
    my_label.config(text=f"You clicked on {my_combo.get()}")

# Create binding function
def click_bind(e):
    my_label.config(text=f"You cliked on {my_combo.get()}")

# Create a Label
my_label = tb.Label(root, text="Hello, World!", font=("Helvatica", 14), bootstyle="default")
my_label.pack(pady= 30)

# Create dropdown options
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Saturday", "Sunday"]

# Create combobox
my_combo = tb.Combobox(root, bootstyle="info", values=days,)
my_combo.pack(pady=20)
# combo default
my_combo.current(0)

# Create a button
my_button = tb.Button(root, text="Click Me!", command=clicker, bootstyle="danger")
my_button.pack(pady=20)

# Bind the combobox
my_combo.bind("<<ComboboxSelected>>", click_bind)


root.mainloop()