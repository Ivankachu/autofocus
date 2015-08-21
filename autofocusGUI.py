import autofocus as af
from tkinter import *


widthpixels = 393
heightpixels = 350

root = Tk()
root.geometry('{}x{}'.format(widthpixels, heightpixels))

lbox = Listbox(root, height=20, width=50)

def filllb():
    lbox.delete(0, END)
    i = 0
    for task in af.pages[af.active[0]]:
        lbox.insert(i, task[0])
        if task[1]:
            lbox.itemconfig(i, bg='indigo', fg='white')
        i += 1

def pushadd():
    af.add(entry_add.get())
    entry_add.delete(0, END)
    filllb()

def pushturn():
    af.turn_the_page()
    filllb()

def pushdone():
    af.complete(lbox.curselection()[0])
    filllb()

def pushcont():
    af.continue_later(lbox.curselection()[0])
    filllb()

def tabber(widget1, widget2):
    if root.focus_get() != widget1:
        widget1.bind('<Tab>', '<FocusIn>')
    else:
        widget2.bind('<Tab>', '<FocusIn>')

filllb()

lbox.grid(rowspan=3, sticky=W+E)

entry_add = Entry(root)
entry_add.grid(row=3, column=0, sticky=W+E)
entry_add.bind('<Tab>', tabber(entry_add, lbox))
lbox.bind('<Tab>', tabber(lbox, entry_add))

button_add = Button(root, text='Add new task', command=pushadd)
button_add.grid(row=3, column=1, sticky=W+E)

button_done = Button(root, text='Done!\n\nF2', command=pushdone)
button_done.bind('<F2>', lambda event: pushdone())
button_done.grid(row=0, column=1, sticky=N+W+E+S)

button_cont = Button(root, text='Continue later\n\nF3', command=pushcont)
button_cont.bind('<F3>', lambda event: pushcont())
button_cont.grid(row=1, column=1, sticky=N+W+E+S)

button_turn = Button(root, text='Turn the Page!\n\nF4', command=pushturn)
button_turn.bind('<F4>', lambda event: pushturn())
button_turn.grid(row=2, column=1, sticky=N+W+E+S)

root.resizable(width=FALSE, height=FALSE)
root.mainloop()
