"""
The app provides plane time-management system created by Mark Forster.
You can add items in your notebook, mark them done or continue later.
You can read about system and rules for using it in the website
http://markforster.squarespace.com/autofocus-system/
"""

import pickle
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
    """
    Copy DB of items to-do list from a file. DB is structured as a dictionary
    consisting of 4 items with keys: 'isdone', 'active', 'chosen' and 'pages'.
    Item 'isdone' is a flag (True of False) that means whether any task
    in the active page is already done in the current lap. The first number
    of that list is an index of current page.
    Item 'active' is a list of pages' indices that has undone tasks.
    Item 'chosen' is a index of chosen task in active page
    which is currently being executed.
    'chosen' = -1 means there is no chosen task now.
    Item 'pages' is a nested list of pages which consist of tasks and flags
    (0 or 1 - undone or done task).
    
    Example of DB dictionary:
    
    {
    "isdone": False,
    "active": [1, 2],
    "chosen": 5,
    "pages" : [
    [['text of task 1', 1], ['text of task 2', 1], ['text of task 3', 1]...],
    [['text of task 21', 1], ['text of task 22', 0], ['text of task 23', 0]...],
    [['text of task 31', 0], ['text of task 32', 0], ['text of task 33', 0]...],
    ]
    }
    
    """
    with open('tasks.pkl', 'rb') as f:
        db = pickle.load(f)
    return db

def print_agenda(db):
    """
    Print undone items from the current active page
    """
    if len(db["active"]):
        print ('=' * 35)
        for (index, task) in enumerate(db["pages"][db["active"][0]]):
            if not task[1]:
                print (' {:2}  {}'.format(index, task[0]))
        print ('=' * 35)
        if db["chosen"] != -1:
            print ("Chosen task:\n{}".\
                   format(db["pages"][db["active"][0]][db["chosen"]][0]))
    else:
        print ("All tasks you planned are completed.")

def add(new_task, db):
    """
    Add new item(task) in the end of the last page or in a new page
    """   
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

def complete(db):
    """
    Mark item as completed
    """
    if db["chosen"] != -1:
        db["isdone"] = True
        db["pages"][db["active"][0]][db["chosen"]][1] = 1
        check_active_page_completed(db)
    db["chosen"] = -1
        
def continue_later(db):
    """
    Mark item as completed and copy it in the end of notebook
    """
    if db["chosen"] != -1:
        task = db["pages"][db["active"][0]][db["chosen"]][0]
        print (task)
        db = complete(db)
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
    """
    Check whether current page is full of items.
    """
    return len(db["pages"][number_of_page]) >= tasks_in_page

def check_active_page_completed(db):
    """
    Check whether all items in current page are marked as completed.
    If so delete the page from the list of active pages.
    """
    for task in db["pages"][db["active"][0]]:
        if not task[1]:
            break
    else:
        del db["active"][0]

def print_active_pages(db):
    """
    Print list of active pages.
    """    
    print (db["active"])

def print_pages(db):
    """
    Print all items in all pages
    """    
    for (index, page) in enumerate(db["pages"]):
        print ("\n")
        print ("page ", index)
        for (index2, task) in enumerate(page):
            print ('{:3}  {:40}{}'.format(index2, task[0], task[1]))

def choose(num):
    if (db["chosen"] == -1 and 0 <= num < 20 and
        not db["pages"][db["active"][0]][num][1]):
        db["chosen"] = num

def clear():
    """
    Clear the screen of console
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def savedb(db, filename):
    """
    Save DB dictionary in file
    """
    with open(filename, 'wb') as f:
        pickle.dump(db, f)

def checkcreatefile():
    """
    Check whether file with DB is created?
    If it's not, create it and write empty DB.
    """
    if not os.path.isfile("tasks.pkl"):
        with open('tasks.pkl', 'wb') as f:
            db = {"isdone": False, "active": [], "chosen": -1, "pages": []}
            pickle.dump(db, f)

def backup(db):
    """
    Create a backup file of previous 4 versions of DB.
    Check for files 'backup<number>.pkl' and find out maximum number.
    Then create 'backup<number+1>.pkl' file consisting of current DB.
    If number of backup files is more than 4 delete file backup<min number>.pkl'.
    """
    FILENAME = "backup"
    list_files = glob.glob(FILENAME + "*.pkl")
    list_num_backup = [int(name[len(FILENAME):-4]) for name in list_files
                       if name[len(FILENAME):-4].isdigit()]
    new_num_backup = None
    if not list_num_backup:
        new_num_backup = 0
    else:
        last_backup = FILENAME + str(max(list_num_backup)) + ".pkl"
        with open(last_backup, 'rb') as f:
            last_db = pickle.load(f)
        if last_db != db:
            new_num_backup = max(list_num_backup) + 1
    if new_num_backup != None:
        new_name_backup = FILENAME + str(new_num_backup) + ".pkl"
        savedb(db, new_name_backup)
        if len(list_num_backup) > 4:
            first_file = FILENAME + str(min(list_num_backup)) + ".pkl"
            os.remove(first_file)

def get_act_ts(db):
    """
    Getting active tasks from the active page with its indices.
    Return list of tuples.
    """
    if db["pages"]:
        act_ts = []
        for i, ts in enumerate(db["pages"][db["active"][0]]):
            if not ts[1]:
                act_ts.append((i, ts[0]))
        return act_ts
    else:
        return []

if __name__ == '__main__':

    checkcreatefile()
    db = copydb()
    print_agenda(db)
    msg = ""

    while msg != 'exit' and msg != 'quit':
        msg = input(">>> ")
        if msg[:4] == "add " and msg[4:]:
            db = add(msg[4:], db)
        if msg[:7] == "choose " and msg[7:]:
            choose(int(msg[7:]))
        if msg[:8] == "complete":
            db = complete(db)
        if msg[:14] == "continue later":
            db = continue_later(db)
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
