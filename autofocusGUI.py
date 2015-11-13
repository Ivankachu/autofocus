import autofocus as af
from tkinter import *

widthpixels = 418
heightpixels = 370

af.checkcreatefile()
db = af.copydb()
root = Tk()
root.geometry('{}x{}'.format(widthpixels, heightpixels))
lbox = Listbox(root, height=20, width=50, activestyle = 'none')

def turn_the_page_gui(db):
    if len(db["active"]):
        if db["isdone"]:
            db["isdone"] = False
            db["active"] = db["active"][1:] + [db["active"][0]]
        elif db["pages"][db["active"][0]] is not db["pages"][-1]:
            if messagebox.askyesno("Warning!", af.msg_can_kill_page):
                db = demolish_page(db)
        else:
            messagebox.showwarning("Warning!", af.msg_cant_turn_page)
    return db           

def filllb():
    lbox.delete(0, END)
    i = 0
    if db["active"]:
        for task in db["pages"][db["active"][0]]:
            lbox.insert(i, task[0])
            if task[1]:
                lbox.itemconfig(i, bg='#804D00', fg='white')
            else:
                lbox.itemconfig(i, bg='#FFD699', fg='black')
            i += 1

def pushadd():
    msg = entry_add.get().strip()
    if msg:
        af.add(msg, db)
        af.savedb(db, "tasks.pkl")
        filllb()
    entry_add.delete(0, END)
    
def pushturn():
    global db
    db = turn_the_page_gui(db)
    af.savedb(db, "tasks.pkl")
    filllb()

def pushdone():
    if lbox.curselection():
        af.complete(lbox.curselection()[0], db)
        af.savedb(db, "tasks.pkl")
        filllb()

def pushcont():
    if lbox.curselection():
        af.continue_later(lbox.curselection()[0], db)
        af.savedb(db, "tasks.pkl")
        filllb()
        
def pushchoose():
    choosewin = Toplevel(root)

def createbutton(command, text, bg='#777', fg = 'white'):
    return Button(root, text=text, command=command, bg=bg, fg=fg)

filllb()
lbox.grid(rowspan=4, sticky=W+E, pady = 5,  padx = 5)

entry_add = Entry(root)
entry_add.grid(row=4, column=0, sticky=W+E, pady = 5,  padx = 5)
entry_add.bind('<Return>', lambda event: pushadd())

button_choose = createbutton(text='Make a choice!\nF5', command=pushchoose,
                     bg = '#444')
button_add = createbutton(text='Add new task', command=pushadd)
button_done = createbutton(text='Done!\nF2', command=pushdone)
button_cont = createbutton(text='Continue later\nF3', command=pushcont)
button_turn = createbutton(text='Turn the Page!\nF4', command=pushturn)

button_choose.grid(row=0, column=1, sticky=W+E+N+S, pady = 5, padx = 5)
button_add.grid(row=4, column=1, sticky=W+E, pady = 5,  padx = 5)
button_done.grid(row=1, column=1, sticky=W+E+N+S, pady = 5, padx = 5)
button_cont.grid(row=2, column=1, sticky=W+E+N+S, pady = 5,  padx = 5)
button_turn.grid(row=3, column=1,  sticky=W+E+N+S, pady = 5,  padx = 5)

root.resizable(width=FALSE, height=FALSE)
root.title("AutoFocus")
root.bind('<F2>', lambda event: pushdone())
root.bind('<F3>', lambda event: pushcont())
root.bind('<F4>', lambda event: pushturn())
root.bind('<F5>', lambda event: pushchoose())

root.mainloop()
af.backup(db)
