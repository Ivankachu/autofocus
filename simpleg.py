from tkinter import *

class App:
    def __init__(self):
        self.root = Tk()
        self.bt = Button(self.root, text='Push Me', command=self.pushme)
        self.bt.pack()
        self.li = ['Aaaaa', 'Bbbbb', 'Ccccc', 'Ddddd', 'Eeeee']
        self.root.mainloop()
    def pushme(self):
        self.newwin = Toplevel(self.root)
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
