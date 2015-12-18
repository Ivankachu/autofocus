import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.data = ''
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'Get data', width = 25, command = self.get_data)
        self.button2.pack()
        self.lab = tk.Label(self.frame, text = self.data)
        self.lab.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.grab_set()
        self.app = Demo2(self.newWindow)
        
    def get_data(self):
        self.data = self.app.data
        self.lab.configure(text = self.data)
        

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.entry_data = tk.Entry(self.frame)
        self.entry_data.pack()
        self.entry_data.bind('<Return>', lambda event: self.choose_it())
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        self.data = ''
    def close_windows(self):
        self.master.destroy()
    def choose_it(self):
        self.data = self.entry_data.get()
        

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
