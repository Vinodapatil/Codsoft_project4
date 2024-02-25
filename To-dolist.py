import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("TO DO LIST")
        self.master.resizable(True, True)  # Allow window resizing

        self.tasks = []

        # Define styles
        self.style = {
            "font": ("Arial", 20),
            "button_bg": "#4CAF50",
            "button_fg": "black",
            "button_hover_bg": "#45a049",
        }

        # Create GUI elements
        self.task_entry = tk.Entry(master, font=self.style["font"])
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task,
                                    bg=self.style["button_bg"], fg=self.style["button_fg"],
                                    activebackground=self.style["button_hover_bg"],
                                    activeforeground=self.style["button_fg"], font=self.style["font"])
        self.add_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.task_listbox = tk.Listbox(master, font=self.style["font"],bg="black",fg="white")
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.mark_button = tk.Button(master, text="Mark as Complete", command=self.mark_task,
                                     bg=self.style["button_bg"], fg=self.style["button_fg"],
                                     activebackground=self.style["button_hover_bg"],
                                     activeforeground=self.style["button_fg"], font=self.style["font"])
        self.mark_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task,
                                       bg=self.style["button_bg"], fg=self.style["button_fg"],
                                       activebackground=self.style["button_hover_bg"],
                                       activeforeground=self.style["button_fg"], font=self.style["font"])
        self.delete_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # Set row and column weights to make the widgets expand and fill the window
        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure((0,1), weight=1)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            task = self.tasks.pop(task_index)
            self.task_listbox.delete(task_index)
            messagebox.showinfo("Info", f'Task "{task}" marked as complete.')
        else:
            messagebox.showwarning("Warning", "Please select a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            task = self.tasks.pop(task_index)
            self.task_listbox.delete(task_index)
            messagebox.showinfo("Info", f'Task "{task}" deleted.')
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
