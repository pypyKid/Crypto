from tkinter import *
import requests
from tkinter import messagebox

root = Tk()
root.title("Cryptography")
root.geometry("400x400")
Label(root, text="Enter your crypto below", font="Tahoma 14").pack()
entry = Entry(root, font="Tahoma 14")
entry.pack(pady=10)


def get_api():
    if len(entry.get()) != 0:
        r = requests.get(
            f"https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms={entry.get()}"
        )
        j = r.json()
        if entry.get().upper() in j:
            price = j[entry.get().upper()]
            lbl.config(text=f"{entry.get().upper()} price : {price}")
        else:
            messagebox.showwarning("Warning", "Crypto not found!")
    else:
        messagebox.showwarning("Warning", "Fill the fields first!")


Button(root, text="Generate", font="Tahoma 14", pady=5, padx=5, command=get_api).pack()
lbl = Label(root, text="", font="Tahoma 14", pady=10)
lbl.pack()
root.mainloop()
