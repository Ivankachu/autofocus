from autofocus import copydb
from tkinter import *

flag, active, pages = copydb()
widthpixels = 393
heightpixels = 350

root = Tk()
root.geometry('{}x{}'.format(widthpixels, heightpixels))

lbox = Listbox(root, height=20, width=50)

i = 0
for task in pages[active[0]]:
    if not task[1]:
        lbox.insert(i + 1, task[0])
        i += 1

lbox.grid(rowspan=3, columnspan=2, sticky=W+E)

entry_add = Entry(root)
button_add = Button(root, text='Add new task')

entry_add.grid(row=3, column=0, sticky=W+E)
button_add.grid(row=3, column=1, sticky=W+E)

button_done = Button(root, text='Done!')
button_done.grid(row=0, column=1, sticky=N+W+E+S)

button_continuelater = Button(root, text='Continue later')
button_continuelater.grid(row=1, column=1, sticky=N+W+E+S)

button_turnthepage = Button(root, text='Turn the Page!')
button_turnthepage.grid(row=2, column=1, sticky=N+W+E+S)

root.mainloop()
