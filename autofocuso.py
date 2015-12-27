import os
import pickle
import glob
import filecmp

MSG_CANT_TURN = ("You have to do something from "	
                 "the current list firstly!")

MSG_CAN_KILL = ("You can turn the page without doing anything "
                "but it will cause marking all tasks "
                "in the page as completed.\n"
                "Do you want to proceed?")

class WritingPad:

    def __init__(self, numstr):
        self.numstr = numstr
        self.status = False
        self.active = []
        self.pages = []
        self.chosen = -1

    def print_agenda(self):
        if len(self.active):
            print ('=' * 35)
            for (index, task) in enumerate(self.pages[self.active[0]]):
                if not task.status:
                    print (' {:2}  {}'.format(index, task.text))
            print ('=' * 35)
        else:
            print ("Nothing to do. Add something!")
        if self.chosen != -1:
            print ("\nCurrent chosen task:\n",
                   self.pages[self.active[0]][self.chosen].text, sep='')

    def add(self, text):
        newtask = Entry(text)
        if not self.pages or len(self.pages[-1]) >= self.numstr:
            self.active.append(len(self.pages))
            self.pages.append([newtask])
        else:
            self.pages[-1].append(newtask)

    def choose(self, numtask):
        if self.chosen == -1 and not self.pages[self.active[0]][numtask].status:
            self.chosen = numtask

    def do(self):
        if self.chosen != -1:
            current_page = self.active[0]
            self.pages[current_page][self.chosen].do()
            if self.check_page_completed():
                self.turn_the_page()
            self.chosen = -1
            self.status = True

    def contin_later(self):
        if self.chosen != -1:
            current_page = self.active[0]
            text = self.pages[current_page][self.chosen].text
            self.do()
            self.add(text)
            if self.check_page_completed():
                self.turn_the_page()
            self.chosen = -1

    def kill_page(self):
        current_page = self.active[0]
        for task in self.pages[current_page]:
            task.do()

    def turn_the_page(self):
        if len(self.active) < 2:
            print ("We can't turn the page. Work!")
        else:
            if self.status:
                self.active.append(self.active.pop(0))
            else:
                self.kill_page()
                self.active.pop(0)
            self.chosen = -1
            self.status = False

    def check_page_completed(self):
        current_page = self.active[0]
        for task in self.pages[current_page]:
            if task.status:
                return False
        return True

    def print_pages(self):
        for index_page, page in enumerate(self.pages):
            print ('Page', index_page)
            print ('-------')
            for index_task, task in enumerate(page):
                print (" {:<4}{:<25.25}{:>3}".format(index_task, task.text, task.status))
            print()

    def check_page_full(self):
        return len(self.pages[active[0]]) >= self.numstr

    def change_text(self, index, text):
        self.pages[self.active[0]][index].text = text

    def get_act_ts():
        act_ts = {}
        for i, ts in enumerate(db.pages[db.active[0]]):
            if not ts.status:
                act_ts[i] = ts.text
        return act_ts


class Entry:

    def __init__(self, text):
        self.text = text
        self.status = 0

    def do(self):
        self.status = 1

def copydb():
    with open('db.pkl', 'rb') as f:
        db = pickle.load(f)
    return db

def savedb(db, filename):
    with open(filename, 'wb') as f:
        pickle.dump(db, f)

def checkcreatefile():
    if not os.path.isfile("db.pkl"):
        with open('db.pkl', 'wb') as f:
            db = WritingPad(20)
            pickle.dump(db, f)

def backup(db):
    """
    Create a backup file of previous 4 versions of DB.
    Check for files 'backup<number>.pkl' and find out maximum number.
    Then create 'backup<number+1>.pkl' file consisting of current DB.
    If number of backup files is more than 4 delete file backup<min number>.pkl'.
    
    """
    savedb(db, 'db.pkl')
    FILENAME = "backupn"
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
        if not filecmp.cmp(last_backup, 'db.pkl'):
            new_num_backup = max(list_num_backup) + 1
    if new_num_backup != None:
        new_name_backup = FILENAME + str(new_num_backup) + ".pkl"
        savedb(db, new_name_backup)
        if len(list_num_backup) > 4:
            first_file = FILENAME + str(min(list_num_backup)) + ".pkl"
            os.remove(first_file)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    
    checkcreatefile()
    db = copydb()
    db.print_agenda()
    msg = ''

    while True:
        msg = input(">>> ").strip()
        if msg == 'exit' or msg == 'quit':
            break
        if msg[:4] == "add " and msg[4:]:
            db.add(msg[4:])
            continue
        if msg[:7] == "choose " and msg[7:]:
            if db.chosen == -1:
                db.choose(int(msg[7:]))
            else:
                print ("The task is already chosen. Do it!")
            continue
        if msg == "complete":
            db.do()
            db.print_agenda()
            continue
        if msg == "continue later":
            db.contin_later()
            db.print_agenda()
            continue
        if msg == "turn the page":
            if db.chosen == -1:
                if db.status:
                    db.turn_the_page()
                    db.print_agenda()
                else:
                    print ("You can turn the page without doing anything "
                           "but it will cause marking all tasks "
                           "in the page as completed.\n"
                           "Do you want to proceed?")
                    msg = input("Yes/No?   ")
                    if msg == "Yes":
                        db.turn_the_page()
                        db.print_agenda()
            else:
                print ("You have a chosen task. Do it or continue later!")
            continue
        if msg == "print":
            db.print_agenda()
            continue
        if msg[:7] == "change " and msg[7:]:
            index, *newtext = msg[7:].split()
            db.change_text(int(index), " ".join(newtext))
            db.print_agenda()
            continue
        if msg == "save":
            savedb(db, "db.pkl")
            continue
        if msg == "help":
            print ("add, complete, continue later, "
                   "turn the page, print, exit")
            continue
        if msg == "print active":
            print (db.active)
            continue
        if msg == "print pages":
            db.print_pages()
            continue
        if msg == "print status":
            print (db.status)
            continue
        if msg == "clear":
            clear()
            continue
        if msg == "backup":
            backup(db)
            continue
        print ("There is no such command", msg)
    savedb(db, 'db.pkl')

