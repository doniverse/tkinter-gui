from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = Tk()

root.title("TTK Bootstrap!")
root.geometry('500x350')

# Create Entry Function
def speak():
    my_label.config(text=f"You typed: {my_entry.get()}")
# Create Entry Widget
my_entry = tb.Entry(root, bootstyle="success", font=("Helvatica", 18), foreground="#003660", width=5)
# PASSWORD: my_entry = tb.Entry(root, bootstyle="success", font=("Helvatica", 18), foreground="#003660", width=5, show='*')
my_entry.pack(pady=50)

# Create Button
my_button = tb.Button(root, bootstyle="danger outline", text="Click Me", command=speak)
my_button.pack(pady=20)

#Create Label
my_label = tb.Label(root, text="")
my_label.pack(pady=20)

root.mainloop()