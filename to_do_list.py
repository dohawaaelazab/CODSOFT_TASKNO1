import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f0f0")

        # Title
        self.title_label = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, font=("Arial", 14))
        self.task_entry.pack(pady=10, fill="x", padx=20)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, width=10, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=0, padx=5)

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task, width=10, bg="#2196F3", fg="white")
        self.update_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, width=10, bg="#f44336", fg="white")
        self.delete_button.grid(row=0, column=2, padx=5)

        self.done_button = tk.Button(self.button_frame, text="Mark Done", command=self.mark_done, width=10, bg="#FF9800", fg="white")
        self.done_button.grid(row=1, column=1, pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, font=("Arial", 14), selectbackground="#d3d3d3")
        self.task_listbox.pack(pady=10, fill="both", expand=True, padx=20)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.task_listbox)
        self.scrollbar.pack(side="right", fill="y")
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task != "":
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a new task!")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def mark_done(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, f"✔ {task}")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as done!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()   # <-- This line keeps the window open
