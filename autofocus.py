import pickle
import os
import glob

num_ts = 20 #Number of tasks in a page

def copydb():
    with open('tasks.pkl', 'rb') as f:
        db = pickle.load(f)
    return db

def print_agenda(db):
    if len(db["active"]):
        print ('=' * 35)
        for (index, task) in enumerate(db["pages"][db["active"][0]]):
            if not task[1]:  #if task is not undone (1, not 0)
                print (' {:2}  {}'.format(index, task[0]))
        print ('=' * 35)
    else:
        print ("All tasks you planned are completed.")

def add(new_task, db):
    if len(db["pages"]):
        if len(db["pages"][-1]) < num_ts:
            db["pages"][-1].append([new_task, 0])  #Add a new task in the last page.
        else:
            db["pages"].append([[new_task, 0]])    #Add a new page and a new task in it.
            index_new_page = len(db["pages"]) - 1
            if db["active"]:                           #If there is something in active list
                place_max = db["active"].index(max(db["active"]))
                db["active"].insert(place_max + 1, index_new_page)
            else:
                db["active"].append(index_new_page)
    else:
        db["pages"].append([[new_task, 0]])
        db["active"].append(0)
    return db

def complete(index_task, db):
    if 0 <= index_task < num_ts:
        if not db["pages"][db["active"][0]][index_task][1]:
            db["isdone"] = True
            db["pages"][db["active"][0]][index_task][1] = 1
            check_active_page_completed(db)  #For the case if all tasks in the page are completed
        else:
            print ("The task is already completed")
    else:
        print ("Bad number. It must be from 0 to 19")
    return db
        
def continue_later(index_task, db):
    task = db["pages"][db["active"][0]][index_task][0]
    db = complete(index_task, db)
    db = add(task, db)
    return db

def demolish_page(db):
    for task in db["pages"][db["active"][0]]:
        task[1] = 1
    del db["active"][0]
    return db

def turn_the_page(db):
    if len(db["active"]):
        if db["isdone"]:
            db["isdone"] = False
            db["active"] = db["active"][1:] + [db["active"][0]]
            print_agenda(db)
        elif db["pages"][db["active"][0]] is not db["pages"][-1]:
            print ("The active page is not started yet.")
            print ("If you turn the page, all uncompleted tasks will be demolished.")
            print ("Are you sure you want to turn the page?")
            msg1 = input("Yes?  ")
            if msg1 == "Yes":
                db = demolish_page(db)
            print_agenda(db)
        else:
            db = demolish_page(db)
    else:
        print ('You cannot turn the last page without completing something!')
    return db

def is_page_full(number_of_page):
    if len(db["pages"][number_of_page]) == num_ts:
        return True
    else:
        return False

def check_active_page_completed(db):
    for task in db["pages"][db["active"][0]]:
        if not task[1]:
            break
    else:
        del db["active"][0]

def print_active_pages(db):
    print (db["active"])

def print_pages(db):
    for (index, page) in enumerate(db["pages"]):
        print ("\n")
        print ("page ", index)
        for (index2, task) in enumerate(page):
            print ('{:3}  {:40}{}'.format(index2, task[0], task[1]))

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def savedb(db):
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(db, f)

def checkcreatefile():
    if not os.path.isfile("tasks.pkl"):
        with open('tasks.pkl', 'wb') as f:
            db = {"isdone": False, "active": [], "pages": []}
            pickle.dump(db, f)

def backup():
    list_files = glob.glob("backup*.pkl")
    list_num_backup = sorted([int(name[6:-4]) for name in list_files])
    print (list_num_backup)

if __name__ == '__main__':

    checkcreatefile()
    db = copydb()
    print_agenda(db)
    msg = ""

    while msg != 'exit' and msg != 'quit':
        msg = input(">>> ")
        
        if msg[:4] == "add " and msg[4:]:
            db = add(msg[4:], db)
            savedb(db)
        if msg[:9] == "complete " and msg[9:]:
            db = complete(int(msg[9:]), db)
            savedb(db)
        if msg[:15] == "continue later " and msg[15:]:
            db = continue_later(int(msg[15:]), db)
            savedb(db)
        if msg == "turn the page":
            db = turn_the_page(db)
            savedb(db)
        if msg == "print":
            print_agenda(db)
        if msg == "help":
            print ("add, complete, continue later, turn the page, print, exit")
        if msg == "print active":
            print_active_pages(db)
        if msg == "print pages":
            print_pages(db)
        if msg == "print flag":
            print (db["isdone"])
        if msg == "save":
            savedb(db)
        if msg == "clear":
            clear()
        if msg == "backup":
            backup()
    savedb(db)
