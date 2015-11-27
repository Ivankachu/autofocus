import tkinter as tk


class App:
    
    def __init__(self):
        self.main = MainWin()
        self.main.btnewwin.bind("<Button-1>", self.secondwin)
        
    def secondwin(self):
        secwin = SecondWin()

        
class MainWin():
    
    def __init__(self):
        self.root = tk.Tk()
        self.btnewwin = tk.Button(self.root, text='New Win!')
        self.btnewwin.pack()
        self.root.mainloop()


class SecondWin:
    
    def __init__(self):
        self.secwin = tk.Tk()
        self.secwin.mainloop()

app = App()
