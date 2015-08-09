import autofocus
from tkinter import *

root = Tk()

tasks = ['task ' + str(i) for i in range(20)]

lbox = Listbox(root)

for (index, task) in enumerate(tasks):
    lbox.insert(index + 1, task)

lbox.grid(rowspan=3, columnspan=2, sticky=W+E+N+S)

label_add = Label(root, text='New task')
entry_add = Entry(root)
button_add = Button(root, text='Add')

label_add.grid(row=3, column=0)
entry_add.grid(row=3, column=1)
button_add.grid(row=3, column=2)

button_done = Button(root, text='Done!')
button_done.grid(row=0, column=2)
button_continuelater = Button(root, text='Continue later')
button_continuelater.grid(row=1, column=2)
button_turnthepage = Button(root, text='Turn the Page!')
button_turnthepage.grid(row=2, column=2)

root.mainloop()