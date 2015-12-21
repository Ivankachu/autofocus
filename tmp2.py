import tkinter as tk

class App:
    def __init__(self, master):
        self.win1 = Demo1(master, self)
    def fun_create(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.grab_set()
        self.app = Demo2(self.newWindow, self)
    def fun_close(self):
        pass


class Demo1:
    def __init__(self, master, parent):
        self.data = ''
        self.master = master
        self.frame = tk.Frame(self.master)
        self.lab = tk.Label(self.frame, text = self.data)
        self.button1 = tk.Button(self.frame, text = 'New Window',
                                 width = 25, command = parent.fun_create)
        self.lab.pack()
        self.button1.pack()
        self.frame.pack()

    def get_data(self):
        self.data = self.app.data
        self.lab.configure(text = self.data)
        

class Demo2:
    def __init__(self, master, parent):
        self.master = master
        self.parent = parent
        self.frame = tk.Frame(self.master)
        self.entry_data = tk.Entry(self.frame)
        self.entry_data.pack()
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25,
                                    command = self.read_message)
        self.quitButton.pack()
        self.frame.pack()
        self.data = ''

    def read_message(self):
        self.data = self.entry_data.get()
        self.master.destroy()
        self.parent.get_data()
        

def main(): 
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
