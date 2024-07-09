from tkinter import *
from tkinter import ttk

# create a class task
class Task:
    def __init__(self, root):
        self.root = root
        self.root.title('TO-DO-LIST-BY-KJ')
        self.root.geometry('850x510+400+250')
        
        self.label = Label(self.root, text = 'TO-DO-LIST-BY-KJ', font = 'Comic, 25 bold', 
                           width=10, bd=5, bg="light pink", fg = 'black')
        self.label.pack(side='top', fill=BOTH)
        
        self.label2 = Label(self.root, text = 'ADD TASK', font = 'Comic, 18 bold', 
                           width=10, bd=5, bg="light blue", fg = 'black')
        self.label2.place(x=60, y=54)
        
        self.label3 = Label(self.root, text = 'LIST', font = 'Comic, 18 bold', 
                           width=10, bd=5, bg="light blue", fg = 'black')
        self.label3.place(x=540, y=54)
        
        self.main_text = Listbox(self.root, height=16,bd=8, width=25, font='Comic, 18 italic bold')
        self.main_text.place(x=490, y=98)
        
        self.text = Text(self.root , bd=5, height=2, width=30, font='comic, 10 bold') 
        self.text.place(x=20, y=120) 
        
        # <-------- add task --------->
        def addtask():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)
        
        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)
            
            
        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()
            
        # <------- buttons to add or delete task ------->
        self.button = Button(self.root, text="Add", font="sarif, 20 bold italic", width=10, bd=5, 
                             bg='light green', fg='black',command=addtask)
        self.button.place(x=30, y=180)
        
        self.button2 = Button(self.root, text="Delete", font="sarif, 20 bold italic", width=10, bd=5, 
                             bg='light green', fg='black',command=delete)
        self.button2.place(x=30, y=400)
        
        
        
def main():
    root = Tk()
    ui = Task(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
    
