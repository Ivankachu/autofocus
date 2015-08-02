from tkinter import *

root = Tk()

label_add = Label(root, text = 'New task')
entry_add = Entry(root)
button_add = Button(root, text='Add')

label_add.grid(row=0, column=0)
entry_add.grid(row=0, column=1)
button_add.grid(row=0, column=2)


root.mainloop()
