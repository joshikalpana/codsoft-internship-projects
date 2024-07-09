

# Create a class task
from tkinter import *
from tkinter import ttk

# Create a class Task
class Task:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        # Create a frame
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(N, W, E, S))
        
        # Create an entry widget to add tasks
        self.task_entry = ttk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)
        
        # Create a button to add tasks
        self.add_button = ttk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)
        
        # Create a listbox to display tasks
        self.task_listbox = Listbox(self.frame, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        # Create a button to delete tasks
        self.delete_button = ttk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        # Initialize a list to hold the tasks
        self.tasks = []

    def add_task(self):
        """Adds a task to the listbox."""
        task_description = self.task_entry.get()
        if task_description.strip():
            self.tasks.append(task_description)
            self.task_listbox.insert(END, task_description)
            self.task_entry.delete(0, END)
        else:
            print("Task description cannot be empty.")
    
    def delete_task(self):
        """Deletes the selected task from the listbox."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
        else:
            print("No task selected.")

def main():
    root = Tk()
    ui = Task(root)
    root.mainloop()

if __name__ == "__main__":
    main()

