import tkinter as tk


class Autofocus:
    
    def __init__(self):
        self.root = tk.Tk()
        self.main = MainWin(self.root)
        self.main.btchoose.bind("<Button-1>", self.choose)
        Autofocus.wincenter(self.root)
        self.root.mainloop()
        
    def choose(self, event):
        self.slave = tk.Toplevel(self.root)
        self.slave.grab_set()
        self.secwin = ChooseWin(self.slave)
        Autofocus.wincenter(self.slave)

    def wincenter(win):
        win.update_idletasks()
        w = win.winfo_screenwidth()
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
        x = int(w / 2 - size[0] / 2)
        y = int(h / 2 - size[1] / 2)
        win.geometry("{}x{}+{}+{}".format(size[0], size[1], x, y))

        
class MainWin:
    
    def __init__(self, master):
        self.master = master
        self.width = 500
        self.height = 500
        self.master.geometry('{}x{}'.format(self.width, self.height))

        self.lbox = tk.Listbox(self.master, height=20, width=50, activestyle = 'none')
        self.inputbox = tk.Entry(self.master)
        self.btchoose = tk.Button(self.master, text='Choose!')
        self.btdone = tk.Button(self.master, text='Done!')
        self.btcont = tk.Button(self.master, text='Continue\nlater')
        self.btadd = tk.Button(self.master, text='Add')
        
        self.lbox.grid(rowspan=3, column=0)
        self.inputbox.grid(row=3, column=0)
        self.btchoose.grid(row=0, column=1)
        self.btdone.grid(row=1, column=1)
        self.btcont.grid(row=2, column=1)
        self.btadd.grid(row=3, column=1)


class ChooseWin:
    
    def __init__(self, master):
        self.master = master
        self.width = 800
        self.height = 200
        self.master.geometry('{}x{}'.format(self.width, self.height))
        
       

app = Autofocus()

