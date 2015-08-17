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
            lbox.itemconfig(i, fg='green')
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

#def convertindex(numinlist):
#    """
#    Convert a number of the selected item in the listbox
#    into the number string in the page
#    """
#    countinpage = 0
#    countinlist = -1
#    for task in af.pages[af.active[0]]:
#        if not task[1]:
#            countinlist += 1
#        if countinlist == numinlist:
#            return countinpage
#        countinpage += 1

lbox.grid(rowspan=3, sticky=W+E)

filllb()

entry_add = Entry(root)
entry_add.grid(row=3, column=0, sticky=W+E)

button_add = Button(root, text='Add new task', command=pushadd)
button_add.grid(row=3, column=1, sticky=W+E)

button_done = Button(root, text='Done!', command=pushdone)
button_done.grid(row=0, column=1, sticky=N+W+E+S)

button_cont = Button(root, text='Continue later', command=pushcont)
button_cont.grid(row=1, column=1, sticky=N+W+E+S)

button_turn = Button(root, text='Turn the Page!', command=pushturn)
button_turn.grid(row=2, column=1, sticky=N+W+E+S)

root.mainloop()
