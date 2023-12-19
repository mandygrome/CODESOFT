import tkinter as tk
from tkinter import messagebox
import random
from tkinter import *

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry('400x400')
        self.master.title("Password Generator")

        # Labels
        labels = {'n_letters': 'letters:', 'n_symbols': 'Symbols:', 'n_numbers': 'Digits:'}
        for key, value in labels.items():
            label = tk.Label(text=value)
            label.place(x=120, y=140 + 40 * list(labels.keys()).index(key), width=50)

        # Entries
        self.letters_entry = tk.Entry(width=15)
        self.letters_entry.place(x=175, y=140)
        self.symbols_entry = tk.Entry(width=15)
        self.symbols_entry.place(x=175, y=180)
        self.numbers_entry = tk.Entry(width=15)
        self.numbers_entry.place(x=175, y=220)
        self.password_entry = tk.Entry(width=30)
        self.password_entry.place(x=130, y=70, height=40)

        # Button
        generate = tk.Button(self.master, text='GENERATE', bg='green', command=self.generate_pass)
        generate.place(x=175, y=350, height=25, width=92)

    def generate_pass(self):
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '@#$&'

        try:
            n_letters = int(self.letters_entry.get())
            n_symbols = int(self.symbols_entry.get())
            n_numbers = int(self.numbers_entry.get())
        except ValueError:
            messagebox.showerror(title='ATTENTION', message='Please enter valid numbers.')
            return

        if n_letters < 0 or n_symbols < 0 or n_numbers < 0:
            messagebox.showerror(title='ATTENTION', message='Please enter positive numbers.')
            return

        password_list = [random.choice(letters) for _ in range(n_letters)]
        password_list += [random.choice(symbols) for _ in range(n_symbols)]
        password_list += [random.choice(numbers) for _ in range(n_numbers)]

        random.shuffle(password_list)

        password = ''.join(password_list)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        messagebox.showinfo(title='CONFIRMATION', message='Password generated successfully!!')


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()