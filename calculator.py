from tkinter import *
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.geometry("400x400")
        master.config(bg='white')

        # Frame
        self.frame = Frame(master, height=500, width=300,bg='#81D8D0')
        self.frame.place(x=50, y=60)

        # Label
        self.name = Label(text="Calculator", fg='black', font=('Serif', 20, 'bold'), bg='white')
        self.name.place(x=130, y=20)

        # Entry
        self.calsi = Entry(self.frame)
        self.calsi.place(x=30, y=40, width=240, height=40)

        # Buttons
        buttons = [
            ('1', 30, 110), ('2', 90, 110), ('3', 150, 110),
            ('4', 30, 160), ('5', 90, 160), ('6', 150, 160),
            ('7', 30, 210), ('8', 90, 210), ('9', 150, 210),
            ('0', 90, 260),
            ('+', 210, 110), ('-', 210, 160), ('*', 210, 210), ('/', 210, 260),
            ('=', 150, 260), ('C', 30, 260)
        ]

        for (text, x, y) in buttons:
            button = Button(self.frame, text=text, font=('Serif', 12, 'bold'), command=lambda t=text: self.button_click(t))
            button.place(x=x, y=y, height=30, width=40)

    def button_click(self, value):
        if value == '=':
            self.calculate()
        elif value == 'C':
            self.clear_entry()
        else:
            self.calsi.insert(END, value)

    def clear_entry(self):
        self.calsi.delete(0, END)

    def calculate(self):
        try:
            expression = self.calsi.get()
            result = eval(expression)
            self.clear_entry()
            self.calsi.insert(0, result)
        except ZeroDivisionError:
            messagebox.showerror(title='ATTENTION', message='Division by zero is not possible')
        except Exception as e:
            messagebox.showerror(title='ATTENTION', message=f'Error: {e}')

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()