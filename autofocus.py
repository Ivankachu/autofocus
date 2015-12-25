###############################################################################
import tkinter as tk
#For working with getting instance WritingPad and Entry from pickle file
from autofocuso import WritingPad, Entry
import autofocuso as af

class Autofocus:
    
    def __init__(self, db, root):
        self.db = db
        self.root = root
        self.main = MainWin(self.root, self, db)
        Autofocus.wincenter(self.root)
        
    def choose(self):
        self.slave = tk.Toplevel(self.root)
        self.slave.grab_set()
        self.secwin = ChooseWin(self.slave)
        Autofocus.wincenter(self.slave)

    def chooseq(self, num):
        self.db.choose(num)

    def done(self):
        pass
        #if lbox.curselection():
        #    self.db.do(lbox.curselection()[0])

    def cont(self):
        pass
        #if lbox.curselection():
        #    self.db.contin_later(lbox.curselection()[0])

    def add(self):
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

    def __init__(self, master, parent, db):
        self.master = master
        self.parent = parent
        self.width = 500
        self.height = 500
        self.db = db
        #self.master.geometry('{}x{}'.format(self.width, self.height))

        self.lbox      = tk.Listbox(self.master, height=20, width=50,
                                    activestyle = 'none')
        self.inputbox  = tk.Entry(self.master)
        self.btchoose  = tk.Button(self.master, text='Choose!',
                                   command=parent.choose)
        self.btchooseq = tk.Button(self.master, text='Choose quick!',
                                      command=self.push_chooseq)
        self.btdone    = tk.Button(self.master, text='Done!',
                                   command=parent.done)
        self.btcont    = tk.Button(self.master, text='Continue\nlater',
                                      command=parent.cont)
        self.btadd     = tk.Button(self.master, text='Add',
                                   command=parent.add)
        
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
        self.inputbox.bind('<Return>', lambda event: self.parent.add)
        self.filllb()

    def filllb(self):
        self.lbox.delete(0, tk.END)
        if self.parent.db.active:
            for i, task in enumerate(db.pages[db.active[0]]):
                self.lbox.insert(i, task.text)
                if i == self.db.chosen:
                    self.lbox.itemconfig(i, bg='#315D99', fg='white')
                else:
                    if task.status:
                        self.lbox.itemconfig(i, bg='#804D00', fg='white')
                    else:
                        self.lbox.itemconfig(i, bg='#FFD699', fg='black')

    def push_chooseq(self):
        if self.lbox.curselection():
            self.parent.chooseq(self.lbox.curselection()[0])
        self.filllb()


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
