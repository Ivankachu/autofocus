import tkinter as tk

class Main:
    def __init__(self, master):
        self.width = 500
        self.height = 500
        self.root = tk.Tk()
        self.root.geometry('{}x{}'.format(self.width, self.height))
        self.btchoose = tk.Button(self.root, text='Choose!')
        self.btdone = tk.Button(self.root, text='Done!')
        self.btcont = tk.Button(self.root, text='Continue\nlater')
        self.btadd =tk. Button(self.root, text='Add')
        self.btchoose.grid(row=0, column=1)
        self.btdone.grid(row=1, column=1)
        self.btcont.grid(row=2, column=1)
        self.btadd.grid(row=3, column=1)


class ChooseWin:
    def __init__(self, master):
        self.master = master
        self.width = 800
        self.height = 300
        self.master.geometry('{}x{}'.format(self.width, self.height))


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.main = Main(self.root)
        self.center(self.root)
        self.main.btchoose.bind("<Button-1>", self.choose)
        self.root.mainloop()
    def center(self, win):
        win.update_idletasks()
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
        x = int(w / 2 - size[0] / 2)
        y = int(h / 2 - size[1] / 2)
        win.geometry("{}x{}+{}+{}".format(size[0], size[1], x, y))
    def choose(self, event):
        self.slave = tk.Toplevel(self.root)
        self.newwin = ChooseWin(self.slave)
        self.center(self.slave)
        self.newwin.grab_set()

app = App()
