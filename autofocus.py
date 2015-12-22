import tkinter as tk
#For working with getting instance WritingPad and Entry from pickle file
from autofocuso import WritingPad, Entry
import autofocuso as af

class Autofocus:
    
    def __init__(self, db, root):
        self.db = db
        self.root = root
        self.main = MainWin(self.root, self)
        Autofocus.wincenter(self.root)
        
    def choose(self):
        self.slave = tk.Toplevel(self.root)
        self.slave.grab_set()
        self.secwin = ChooseWin(self.slave)
        Autofocus.wincenter(self.slave)

    def chooseq(self, event):
        pass

    def done(self, event):
        if lbox.curselection():
            self.db.do(lbox.curselection()[0])

    def cont(self, event):
        if lbox.curselection():
            self.db.contin_later(lbox.curselection()[0])

    def add(self, event):
        pass

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

    def __init__(self, master, parent):
        self.master = master
        self.width = 500
        self.height = 500
        #self.master.geometry('{}x{}'.format(self.width, self.height))

        self.lbox      = tk.Listbox(self.master, height=20, width=50,
                                    activestyle = 'none')
        self.inputbox  = tk.Entry(self.master)
        self.btchoose  = self.make_bt(text='Choose!', command=parent.choose)
        self.btchooseq = self.make_bt(text='Choose quick!')
        self.btdone    = self.make_bt(text='Done!')
        self.btcont    = self.make_bt(text='Continue\nlater')
        self.btadd     = self.make_bt(text='Add')
        
        self.lbox.grid     (rowspan=4, column=0)
        self.inputbox.grid (row=4, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
        self.btchoose.grid (row=0, column=1, sticky=tk.W+tk.E+tk.N+tk.S,
                            padx=5, pady=2)
        self.btchooseq.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S,
                            padx=5, pady=2)
        self.btdone.grid   (row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S,
                            padx=5, pady=2)
        self.btcont.grid   (row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S,
                            padx=5, pady=2)
        self.btadd.grid    (row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S,
                            padx=5, pady=2)


    def make_bt(self, text="", command=None):
        return tk.Button(self.master, text=text, command=command)


class ChooseWin:
    
    def __init__(self, master):
        self.master = master
        self.width = 800
        self.height = 200
        self.master.geometry('{}x{}'.format(self.width, self.height))
        self.labchoose = tk.Label(self.master, text='task #1')
        self.labchoose.pack()

    def show_tasks(self):
        pass


af.checkcreatefile()
root = tk.Tk()
db = af.copydb()
app = Autofocus(db, root)
root.mainloop()
