import tkinter as tk


class App:
    
    def __init__(self):
        self.main = MainWin()
        self.main.btnewwin.bind("<Button-1>", self.secondwin)
        self.main.mainloop()
        
    def secondwin(self):
        self.secwin = SecondWin()
        self.secwin.mainloop()

        
class MainWin(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.root = tk.Tk()
        self.btnewwin = tk.Button(self.root, text='New Win!')
        self.btnewwin.pack()


class SecondWin(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        

app = App()
