"""
The app provides plane time-management system created by Mark Forster.
You can add items in your notebook, mark them done or continue later.
You can read about system and rules for using it in the website
http://markforster.squarespace.com/autofocus-system/
"""

mport pickle
import os
import glob

tasks_in_page = 20
msg_cant_turn_page = ("You have to do something from "	
                      "the current list firstly!")
msg_can_kill_page = ("You can turn the page without doing anything "
                     "but it will cause marking all tasks "
                     "in the page as completed.\n"
                     "Do you wish to proceed?")

def copydb():
    with open('tasks.pkl', 'rb') as f:
        db = pickle.load(f)
    return db

def print_agenda(db):
    if len(db["active"]):
        print ('=' * 35)
        for (index, task) in enumerate(db["pages"][db["active"][0]]):
            if not task[1]:
                print (' {:2}  {}'.format(index, task[0]))
        print ('=' * 35)
    else:
        print ("All tasks you planned are completed.")

def add(new_task, db):
    if len(db["pages"]):
        if len(db["pages"][-1]) < tasks_in_page:
            #Add a new task in the last page
            db["pages"][-1].append([new_task, 0])
        else:
            #Add a new page and a new task in it
            db["pages"].append([[new_task, 0]])
            index_new_page = len(db["pages"]) - 1
            if db["active"]:
                place_max = db["active"].index(max(db["active"]))
                db["active"].insert(place_max + 1, index_new_page)
            else:
                db["active"].append(index_new_page)
    else:
        db["pages"].append([[new_task, 0]])
        db["active"].append(0)
    return db

def complete(index_task, db):
    if 0 <= index_task < tasks_in_page:
        if not db["pages"][db["active"][0]][index_task][1]:
            db["isdone"] = True
            db["pages"][db["active"][0]][index_task][1] = 1
            check_active_page_completed(db)
        else:
            print ("The task is already completed")
    else:
        print ("Bad number. It must be from 0 to 19")
    return db
        
def continue_later(index_task, db):
    """
    Mark item as completed and copy it in the end of notebook
    """
    task = db["pages"][db["active"][0]][index_task][0]
    db = complete(index_task, db)
    db = add(task, db)
    return db

def demolish_page(db):
    """
    Mark all items in current page as completed and delete
    it from list of active pages
    """
    for task in db["pages"][db["active"][0]]:
        task[1] = 1
    del db["active"][0]
    return db

def turn_the_page(db):
    """
    Shift active pages: first page in active list become last one.
    """
    if len(db["active"]):
        if db["isdone"]:
            db["isdone"] = False
            db["active"] = db["active"][1:] + [db["active"][0]]
            print_agenda(db)
        else:
            if db["pages"][db["active"][0]] is not db["pages"][-1]:
                print (msg_can_kill_page)
                msg1 = input("Yes?  ")
                if msg1 == "Yes":
                    db = demolish_page(db)
                    print_agenda(db)
            else:
                print (msg_cant_turn_page)
    return db

def is_page_full(number_of_page):
    if len(db["pages"][number_of_page]) == tasks_in_page:
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

def savedb(db, filename):
    with open(filename, 'wb') as f:
        pickle.dump(db, f)

def checkcreatefile():
    if not os.path.isfile("tasks.pkl"):
        with open('tasks.pkl', 'wb') as f:
            db = {"isdone": False, "active": [], "pages": []}
            pickle.dump(db, f)

def backup(db):
    list_files = glob.glob("backup*.pkl")
    list_num_backup = [int(name[6:-4]) for name in list_files
                       if name[6:-4].isdigit()]
    new_num_backup = None
    if not list_num_backup:
        new_num_backup = 0
    else:
        last_backup = "backup" + str(max(list_num_backup)) + ".pkl"
        with open(last_backup, 'rb') as f:
            last_db = pickle.load(f)
        if last_db != db:
            new_num_backup = max(list_num_backup) + 1
    if new_num_backup != None:
        new_name_backup = "backup" + str(new_num_backup) + ".pkl"
        savedb(db, new_name_backup)
        if len(list_num_backup) > 4:
            first_file = "backup" + str(min(list_num_backup)) + ".pkl"
            os.remove(first_file)

if __name__ == '__main__':

    checkcreatefile()
    db = copydb()
    print_agenda(db)
    msg = ""

    while msg != 'exit' and msg != 'quit':
        msg = input(">>> ")
        if msg[:4] == "add " and msg[4:]:
            db = add(msg[4:], db)
        if msg[:9] == "complete " and msg[9:]:
            db = complete(int(msg[9:]), db)
        if msg[:15] == "continue later " and msg[15:]:
            db = continue_later(int(msg[15:]), db)
        if msg == "turn the page":
            db = turn_the_page(db)
        if msg == "print":
            print_agenda(db)
        if msg == "help":
            print ("add, complete, continue later, turn the page, "
                   "print, exit")
        if msg == "print active":
            print_active_pages(db)
        if msg == "print pages":
            print_pages(db)
        if msg == "print flag":
            print (db["isdone"])
        if msg == "save":
            savedb(db, "tasks.pkl")
        if msg == "clear":
            clear()
        if msg == "backup":
            backup(db)
    backup(db)
    savedb(db, "tasks.pkl")
