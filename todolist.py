from tkinter import *
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("TO DO LIST")
        self.master.geometry('400x500')

        self.heading = Label(text="TO DO LIST", font=("Rangile", 24, 'bold'), fg='red')
        self.heading.place(x=115, y=0)

        # Frame
        self.frame = Frame(self.master, height=250, width=300, highlightbackground="red", highlightthickness=3)
        self.frame.place(x=50, y=50)

        self.tasklist = Listbox(self.frame, font=('times new roman', 12, 'bold'), fg='white', bg='#6F8FAF', selectmode=EXTENDED)
        self.tasklist.place(x=2, y=2, height=243, width=290)

        self.scrollbar = Scrollbar(self.master, command=self.tasklist.yview, width=12)
        self.scrollbar.place(x=336, y=54, height=240)
        self.tasklist.config(yscrollcommand=self.scrollbar.set)

        self.getdata = Entry(self.master, width=35, highlightbackground='black', highlightthickness=1)
        self.getdata.place(x=50, y=330, height=25)

        # Buttons
        self.add_button = Button(self.master, text='ADD', bg='red', width=9, command=self.add_data)
        self.add_button.place(x=275, y=330, height=25)

        self.create_button = Button(self.master, text='CREATE', bg='red', width=15, command=self.create)
        self.create_button.place(x=65, y=380, height=30)

        self.update_button = Button(self.master, text='UPDATE', bg='red', width=15, command=self.update)
        self.update_button.place(x=220, y=380, height=30)

        self.delete_button = Button(self.master, text='DELETE', bg='red', width=15, command=self.delete)
        self.delete_button.place(x=65, y=430, height=30)

        self.done_button = Button(self.master, text='DONE', bg='red', width=15, command=self.done)
        self.done_button.place(x=220, y=430, height=30)

        self.show_list()

    def show_list(self):
        with open("manav.txt", 'r') as f:
            data = f.readlines()
            if len(data) != 0:
                for i in data:
                    self.tasklist.insert(END, i)

    def add_data(self):
        task = self.getdata.get()
        self.tasklist.insert(END, task)
        self.getdata.delete(0, END)

    def create(self):
        with open("manav.txt", 'r') as f:
            data = f.readlines()
        if len(data) == 0:
            task_count = self.tasklist.size()
            for i in range(task_count):
                task = self.tasklist.get(i)
                with open("manav.txt", 'a') as f:
                    f.write(f"{task}\n")
            messagebox.showinfo(title='Confirmation', message='You created tasklist successfully  !!')
        else:
            messagebox.showerror(title='ATTENTION', message='You already created task list')

    def update(self):
        task_count = self.tasklist.size()
        for i in range(self.size, task_count):
            task = self.tasklist.get(i)
            with open("manav.txt", 'a') as f:
                f.write(f"{task}\n")
        self.size = self.tasklist.size()
        messagebox.showinfo(title='UPDATE', message='You update tasklist successfully  !!')

    def delete(self):
        to_delete = self.tasklist.curselection()
        for i in to_delete:
            data = self.tasklist.get(i)
            self.tasklist.delete(i)
            with open("manav.txt", "r") as file:
                lines = file.readlines()
            filtered_lines = [line for line in lines if line.strip() != data.strip()]
            with open("manav.txt", "w") as file:
                file.writelines(filtered_lines)
            messagebox.showinfo(title='DELETE', message='Your deleted task successfully  !!')

    def done(self):
        change = self.tasklist.curselection()
        for i in change:
            data = self.tasklist.get(i)
            with open('manav.txt', 'r', encoding="utf-8") as file:
                file_content = file.read()
            new_data = f"{data} ✔"
            modified_content = file_content.replace(data, new_data)

            with open('manav.txt', 'w', encoding="utf-8") as file:
                file.write(modified_content)
            self.tasklist.insert(change, new_data)
            self.tasklist.itemconfig(i, fg='green')
            messagebox.showinfo(title='COMPLETION', message='You completed task successfully  !!')
            self.tasklist.delete(i + 1)

if __name__ == "__main__":
    root = Tk()
    app = ToDoListApp(root)
    root.mainloop()