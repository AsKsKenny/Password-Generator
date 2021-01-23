import pyperclip
import tkinter as tk
from tkinter import Text, Tk
import secrets
import string

chars = string.digits + string.ascii_letters + string.punctuation

win = tk.Tk()
win.title("Password Generator by Ken Czyz")
win.geometry("520x60")

clipboard_var = ""
def test_button_click():
        var = "".join([secrets.choice(chars) for _ in range (40)])
        clipboard_var = var
        label_val.set(var)
        pyperclip.copy(clipboard_var)

my_button = tk.Button(win, width=25, text='Generate new 256-Bit Password', command=test_button_click)
my_button.grid(column=0, row=2)
label_val = tk.StringVar()
my_Label = tk.Entry(win, width=50, textvariable=label_val)
my_Label.grid(column=2, row=2, ipady=5)
win.mainloop()
