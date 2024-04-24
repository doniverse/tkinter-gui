from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(themename="darkly")

root.title("TTK Bootstrap!")
# root.iconbitmap("images/codemy.ico")
root.geometry('500x350')


def checker():
    if var1.get() == 1:
        my_label.config(text="Checked!")
    else:
        my_label.config(text="Unchecked!")


# Label
my_label = Label(text="Click the checkbox", font=("Helvatica", 18))
my_label.pack(pady=(40, 10))

# CheckButton
var1 = IntVar()
my_check = tb.Checkbutton(bootstyle="primary", text="Check Me Out!", variable=var1, onvalue=1, offvalue=0, command=checker)
my_check.pack(pady=10)

# ToolButton
var2 = IntVar()
my_check2 = tb.Checkbutton(bootstyle="danger, toolbutton", text="ToolButton!!", variable = var2, onvalue= 1, offvalue= 0, command=checker)
my_check2.pack(pady=10)


# Outline ToolButton
var3 = IntVar()
my_check3 = tb.Checkbutton(bootstyle="danger, toolbutton, outline", text="Outline ToolButton", variable = var2, onvalue= 1, offvalue= 0, command=checker)
my_check3.pack(pady=10)

#round toggle button
var4 = IntVar()
my_check4 = tb.Checkbutton(bootstyle="danger, toolbutton, outline", text="Outline ToolButton", variable = var2, onvalue= 1, offvalue= 0, command=checker)
my_check4.pack(pady=10)

# Outlines Toolbutton
# In Love With Web Dev


root.mainloop()