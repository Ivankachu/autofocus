import autofocusc as af
from tkinter import *

widthpixels = 418
heightpixels = 370

def turn_the_page_gui(db):
    if len(db["active"]):
        if db["isdone"]:
            db["isdone"] = False
            db["active"] = db["active"][1:] + [db["active"][0]]
        elif db["pages"][db["active"][0]] is not db["pages"][-1]:
            if messagebox.askyesno("Warning!", af.msg_can_kill_page):
                db = af.demolish_page(db)
        else:
            messagebox.showwarning("Warning!", af.msg_cant_turn_page)
    return db           

def filllb():
    lbox.delete(0, END)
    if db["active"]:
        for i, task in enumerate(db["pages"][db["active"][0]]):
            lbox.insert(i, task[0])
            if not task[1]:
                if i == db["chosen"]:
                    lbox.itemconfig(i, bg='#2e8f7b', fg='white')
                else:
                    lbox.itemconfig(i, bg='#FFD699', fg='black')
            else:
                lbox.itemconfig(i, bg='#804D00', fg='white')
                
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
    act_ts[:] = []  #to clear list without losing object
    act_ts.extend(af.get_act_ts(db))
    if not act_ts: return
    choose_win = Toplevel(root)
    choose_win.grab_set()
    labtext = act_ts.pop(0)[1]
    choose_lab = Label(choose_win, text=labtext,
                                   font=("Helvetica", 16),
                                   height=3)
    bt_this_one = Button(choose_win, text="This one",
                                 command=lambda: push_this_one(choose_win),
                                 width=45,
                                 state = DISABLED)
    bt_next = Button(choose_win, text="Next", width=45,
                                 command=lambda: push_next(choose_lab),
                                 state = DISABLED)
    choose_lab.pack()
    bt_this_one.pack(side=LEFT)
    bt_next.pack(side=LEFT)
    win_to_center(choose_win)
    choose_win.after(1000, lambda: auto_next_task(choose_lab, choose_win,
                                            bt_this_one, bt_next))

def push_next(choose_lab):
    act_ts.append(act_ts.pop(0))
    choose_lab.config(text=act_ts[0][1])

def push_this_one(choose_win):
    db["chosen"] = act_ts[0]
    choose_win.destroy()
    filllb()

def auto_next_task(lab, win, bt_this_one, bt_next):
    if act_ts:
        lab.config(text=act_ts.pop(0)[1])
        win.after(1000, lambda: auto_next_task(lab, win, bt_this_one, bt_next))
    else:
        act_ts.extend(af.get_act_ts(db))
        lab.config(text=act_ts[0][1])
        bt_this_one.config(state = NORMAL)
        bt_next.config(state = NORMAL)
        
def win_to_center(win):
    win.update_idletasks()
    w = win.winfo_screenwidth()
    w = win.winfo_screenwidth()
    h = win.winfo_screenheight()
    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = int(w / 2 - size[0] / 2)
    y = int(h / 2 - size[1] / 2)
    win.geometry("{}x{}+{}+{}".format(size[0], size[1], x, y))

def createbutton(command, text, bg='#777', fg = 'white'):
    return Button(root, text=text, command=command, bg=bg, fg=fg)

af.checkcreatefile()
db = af.copydb()
act_ts = []

root = Tk()
root.geometry('{}x{}'.format(widthpixels, heightpixels))
win_to_center(root)
lbox = Listbox(root, height=20, width=50, activestyle = 'none')

filllb()
lbox.grid(rowspan=4, sticky=W+E, pady = 5,  padx = 5)

entry_add = Entry(root)
entry_add.grid(row=4, column=0, sticky=W+E, pady = 5,  padx = 5)
entry_add.bind('<Return>', lambda event: pushadd())

button_choose = createbutton(text='Make a choice!\nF5',
                             command=pushchoose, bg = '#444')
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
root.title("AutoFocus P")
root.bind('<F2>', lambda event: pushdone())
root.bind('<F3>', lambda event: pushcont())
root.bind('<F4>', lambda event: pushturn())
root.bind('<F5>', lambda event: pushchoose())

root.mainloop()
af.backup(db)
