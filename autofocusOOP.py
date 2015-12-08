import os
import pickle

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
        for index, page in enumerate(self.pages):
            print ('Page', index)
            print ('-------')
            for task in page:
                print (task.text, task.status)
            print()

    def check_page_full(self):
        return len(self.pages[active[0]]) >= self.numstr

    def change_text(self, index, text):
        self.pages[active[0]][index].text = text

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
        msg = input(">>> ")
        if msg == 'exit' or msg == 'quit':
            break
        if msg[:4] == "add " and msg[4:]:
            db.add(msg[4:])
            continue
        if msg[:7] == "choose " and msg[7:]:
            db.choose(int(msg[7:]))
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
            db.turn_the_page()
            db.print_agenda()
            continue
        if msg == "print":
            db.print_agenda()
            continue
        if msg[:7] == "change " and msg[7:]:
            db.change_text(msg[7:])
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
        print ("There is no such command", msg)
    savedb(db, 'db.pkl')

