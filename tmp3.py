import tkinter as tk

class App(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.main = MainWin(self)
        self.main.btchoose.bind("<Button-1>", self.choose)
        
    def choose(self, event):
        self.slave = tk.Toplevel(self)
        self.slave.grab_set()
        self.secwin = ChooseWin(self.slave)
        
class MainWin(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.btchoose = tk.Button(self, text='Choose!')
        self.btchoose.pack()


class ChooseWin(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)


root = tk.Tk()
app = App(root)
root.mainloop()
