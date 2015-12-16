import tkinter as tk
from tkinter import *
from tkinter import ttk


class Demo1( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Demo 1")
        self.button1 = Button( self, text = "Button 1", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )

    def new_window(self):
        self.newWindow = Demo2()

class Demo2(Frame):     
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Demo 2")
        new.button = tk.Button(  text = "Button 2", width = 25,
                                 command = self.close_window )
        new.button.pack()

    def close_window(self):
        self.destroy()

def main(): 
    Demo1().mainloop()

if __name__ == '__main__':
    main()
