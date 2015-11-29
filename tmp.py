import tkinter as tk


class App:
    
    def __init__(self):
        self.root = tk.Tk()
        self.main = MainWin(self.root)
        self.main.btnewwin.bind("<Button-1>", self.secondwin)
        self.root.mainloop()
        
    def secondwin(self, event):
        self.slave = tk.Toplevel(self.root)
        self.secwin = SecondWin(self.slave)

        
class MainWin:
    
    def __init__(self, master):
        self.btnewwin = tk.Button(master, text='New Win!')
        self.btnewwin.pack()


class SecondWin:
    
    def __init__(self, master):
        self.master = master
       

app = App()

