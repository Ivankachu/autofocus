import tkinter as tk
#For working with getting instance WritingPad and Entry from pickle file
from autofocusoop import WritingPad, Entry
import autofocusoop as af

class Autofocus:
    
    def __init__(self, db):
        self.db = db
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
        #self.master.geometry('{}x{}'.format(self.width, self.height))

        self.lbox      = tk.Listbox(self.master, height=20, width=50,
                                    activestyle = 'none')
        self.inputbox  = tk.Entry(self.master)
        self.btchoose  = self.make_bt(text='Choose!')
        self.btchooseq = self.make_bt(text='Choose quick!')
        self.btdone    = self.make_bt(text='Done!')
        self.btcont    = self.make_bt(text='Continue\nlater')
        self.btadd     = self.make_bt(text='Add')
        
        self.lbox.grid     (rowspan=4, column=0)
        self.inputbox.grid (row=4, column=0, sticky=W+E+N+S)
        self.btchoose.grid (row=0, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.btchooseq.grid(row=1, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.btdone.grid   (row=2, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.btcont.grid   (row=3, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.btadd.grid    (row=4, column=1, sticky=W+E+N+S, padx=5, pady=5)

    def make_bt(self, text=""):
        return tk.Button(self.master, text=text)


class ChooseWin:
    
    def __init__(self, master):
        self.master = master
        self.width = 800
        self.height = 200
        self.master.geometry('{}x{}'.format(self.width, self.height))
        self.labchoose = tk.Label(self.master, text='task #1')
        self.labchoose.pack()


af.checkcreatefile()
db = af.copydb()
app = Autofocus(db)

