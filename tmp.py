import tkinter as tk


class App:
    def __init__(self):
        self.main = MainWin()
        self.main.btnewwin.bind("<Button-1>", self.secondwin)
    def printing(self, message):
        print (message)
        
    def secondwin(self):
        secwin = SecondWin()

        
class MainWin:
    def __init__(self):
        self.root = tk.Tk()
        self.btnewwin = tk.Button(self.root, text='New Win!')
        self.btnewwin.pack()
        self.bthi = tk.Button(self.root, text='Print "Hi!"')
        self.bthi.pack()
        self.btbye = tk.Button(self.root, text='Print "Bye"!')
        self.btbye.pack()
        self.root.mainloop()

class SecondWin:
    def __init__(self):
        self.secwin = tk.Tk()
        self.message = Label(self.secwin, text="")
        self.message.pack()
        self.secwin.mainloop()

app = App()
