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
        self.secwin = ChooseWin(self.slave, self.db)
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

    def __init__(self, master, parent, db):
        self.master = master
        self.parent = parent
        self.db = db
        self.master.resizable(width=tk.FALSE, height=tk.FALSE)
        
##        self.width = 500
##        self.height = 500
##        self.master.geometry('{}x{}'.format(self.width, self.height))

        self.lbox      = tk.Listbox(self.master, height=20, width=50,
                                    activestyle = 'none', bg='#FFD699')
        self.inputbox  = tk.Entry(self.master)
        self.btchoose  = tk.Button(self.master, text='Choose!',
                                   command=parent.choose)
        self.btchooseq = tk.Button(self.master, text='Choose quick!',
                                      command=self.push_chooseq)
        self.btdone    = tk.Button(self.master, text='Done!',
                                   command=self.push_done)
        self.btcont    = tk.Button(self.master, text='Continue\nlater',
                                      command=self.push_contin_later)
        self.btturn    = tk.Button(self.master, text ='Turn the page!',
                                   command=self.push_turn)
        self.btadd     = tk.Button(self.master, text='Add',
                                   command=self.push_add)
        
        self.lbox.grid     (rowspan=5, column=0)
        self.inputbox.grid (row=5, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
        self.btchoose.grid (row=0, column=1, sticky=tk.W+tk.E+tk.N+tk.S,
                            padx=5, pady=2)
        self.btchooseq.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S,
                            padx=5, pady=2)
        self.btdone.grid   (row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S,
                            padx=5, pady=2)
        self.btcont.grid   (row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S,
                            padx=5, pady=2)
        self.btturn.grid   (row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S,
                            padx=5, pady=2)
        self.btadd.grid    (row=5, column=1, sticky=tk.W+tk.E+tk.N+tk.S,
                            padx=5, pady=2)
        self.inputbox.bind('<Return>', lambda event: self.push_add())
        self.filllb()

    def filllb(self):
        self.lbox.delete(0, tk.END)
        if self.parent.db.active:
            for i, task in enumerate(db.pages[db.active[0]]):
                self.lbox.insert(i, task.text)
                if i == self.db.chosen:
                    self.lbox.itemconfig(i, bg='#317332', fg='white')
                else:
                    if task.status:
                        self.lbox.itemconfig(i, bg='#804D00', fg='white')
                    else:
                        self.lbox.itemconfig(i, bg='#FFD699', fg='black')

    def push_chooseq(self):
        if self.lbox.curselection():
            self.db.choose(self.lbox.curselection()[0])
        self.filllb()

    def push_done(self):
        if self.db.chosen > -1:
            self.db.do()
            self.db.chosen = -1
            self.filllb()

    def push_contin_later(self):
        if self.db.chosen > -1:
            self.db.contin_later()
            self.db.chosen = -1
            self.filllb()

    def push_turn(self):
        if not self.db.check_page_completed() and self.db.chosen == -1:
            if db.status:
                self.db.turn_the_page()
                self.filllb()
            else:
                if tk.messagebox.askyesno("Warning!", af.MSG_CAN_KILL):
                    self.kill_page()
                    self.db.turn_the_page()
                    self.filllb()
        else:
            tk.messagebox.showwarning("Warning!", af.MSG_CANT_TURN)

    def push_add(self):
        msg = self.inputbox.get().strip()
        if msg:
            self.db.add(msg)
            af.backup(db)
            self.filllb()
        self.inputbox.delete(0, tk.END)
        

class ChooseWin:
    
    def __init__(self, master, db):
        self.master = master
        self.width = 800
        self.height = 200
        self.db = db
        self.master.geometry('{}x{}'.format(self.width, self.height))
        self.labchoose = tk.Label(self.master, text='')
        self.labchoose.pack()
        self.btchooseit = tk.Button(self.master, text='Choose it',
                                state = tk.DISABLED)
        self.btnext_task = tk.Button(self.master, text='Next',
                                command=self.push_next, state = tk.DISABLED)
        self.btchooseit.pack()
        self.btnext_task.pack()
        
        self.show_tasks(0)
        self.choose_task(0)

    def show_tasks(self, i):
        if i < len(self.db.pages[self.db.active[0]]):
            msg = db.pages[db.active[0]][i].text
            self.labchoose.config(text=msg)
            i += 1
            self.master.after(300, lambda: self.show_tasks(i))

    def choose_task(self, i):
##        self.btchooseit.config(state = tk.NORMAL)
##        self.btnext_task.config(state = tk.NORMAL)
        msg = db.pages[db.active[0]][i].text
        self.labchoose.config(text=msg)

    def push_next(self):
        i = (i + 1) % len(self.db.pages[self.db.active[0]])
        msg = db.pages[db.active[0]][i].text
        self.labchoose.config(text=msg)

    def push_chooseit(self):
        pass
        

af.checkcreatefile()
root = tk.Tk()
db = af.copydb()
app = Autofocus(db, root)
root.mainloop()
af.backup(db)
