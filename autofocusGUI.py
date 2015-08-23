import autofocus as af
from tkinter import *


widthpixels = 393
heightpixels = 350

root = Tk()
root.geometry('{}x{}'.format(widthpixels, heightpixels))

lbox = Listbox(root, height=20, width=50)

def turn_the_page_gui(flag, active, pages):
    if len(active):
        if flag:
            flag = False
            active = active[1:] + [active[0]]
        elif pages[active[0]] is not pages[-1]:
            if messagebox.askyesno(
                "Warning!",
                "If you turn the page, all uncompleted tasks will be demolished.\
                Are you sure you want to turn the page?"):
                for task in pages[active[0]]:
                    task[1] = 1
                del active[0]
        else:
            messagebox.showwarning(
                "Warning!",
                "You cannot turn the last page without completing something!")
        return flag, active, pages           

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
    af.flag, af.active, af.pages = turn_the_page_gui(af.flag, af.active, af.pages)
    filllb()

def pushdone():
    af.complete(lbox.curselection()[0])
    filllb()

def pushcont():
    af.continue_later(lbox.curselection()[0])
    filllb()

filllb()

lbox.grid(rowspan=3, sticky=W+E)

entry_add = Entry(root)
entry_add.grid(row=3, column=0, sticky=W+E)

button_add = Button(root, text='Add new task', command=pushadd)
button_add.grid(row=3, column=1, sticky=W+E)

button_done = Button(root, text='Done!\nF2', command=pushdone)
button_done.bind('<F2>', lambda event: pushdone())
button_done.grid(row=0, column=1, sticky=N+W+E+S)

button_cont = Button(root, text='Continue later\nF3', command=pushcont)
button_cont.bind('<F3>', lambda event: pushcont())
button_cont.grid(row=1, column=1, sticky=N+W+E+S)

button_turn = Button(root, text='Turn the Page!\nF4', command=pushturn)
button_turn.bind('<F4>', lambda event: pushturn())
button_turn.grid(row=2, column=1, sticky=N+W+E+S)

root.resizable(width=FALSE, height=FALSE)
root.mainloop()
