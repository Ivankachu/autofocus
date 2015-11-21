from tkinter import *

class App:
    def __init__(self):
        self.width = 400
        self.height = 300
        self.root = Tk()
        self.root.geometry('{}x{}'.format(self.width, self.height))
        self.root.update_idletasks()
        self.center(self.root)
        self.bt = Button(self.root, text='Push Me', command=self.pushme)
        self.bt.pack()
        self.li = ['Aaaaa', 'Bbbbb', 'Ccccc', 'Ddddd', 'Eeeee']
        self.root.mainloop()
    def center(self, win):
        win.update_idletasks()
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
        x = int(w / 2 - size[0] / 2)
        y = int(h / 2 - size[1] / 2)
        win.geometry("{}x{}+{}+{}".format(size[0], size[1], x, y))
    def pushme(self):
        self.newwin = Toplevel(self.root)
        self.newwin.geometry('{}x{}'.format(600, 200))
        self.center(self.newwin)
        self.newwin.grab_set()
        self.showli = self.li[:]
        self.lab = Label(self.newwin, text=self.showli.pop(0))
        self.lab.pack()
        self.lab.after(1000, self.changelabel)
    def changelabel(self):
        if not self.showli:
            self.lab.config(text='')
            return
        self.lab.config(text=self.showli.pop(0))
        self.lab.after(1000, self.changelabel)

app = App()
