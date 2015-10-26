class WritingPad:

    def __init__(self, numstr):
        self.numstr = numstr
        self.status = False
        self.acitve = []
        self.pages = []

    def print_agenda(self):
        if len(self.active):
            print ('=' * 35)
            for (index, task) in enumerate(self.pages[self.active][0]):
                if not task.status:
                    print (' {:2}  {}'.format(index, task.text))
            print ('=' * 35)
        else:
            print ("Nothing to do. Add something!")

    def add_task(self, text):
        newtask = Entry(text)
        if len(self.pages[-1]) < self.numstr:
            self.pages[-1].append(newtask)
        else:
            self.pages.append([newtask])

    def do_task(self, numtask):
        current_page = active[0]
        self.pages[current_page][numtask].do_task()
        if self.check_complete_page():
            self.turn_the_page()

    def contin_later(self, numtask):
        current_page = active[0]
        text = self.pages[current_page][numtask].text
        self.do_task(numtask)
        self.add_task(text)
        if self.check_page_completed():
            self.turn_the_page()

    def kill_page(self):
        current_page = active[0]
        for task in self.pages[current_page]:
            task.do_task()

    def turn_the_page(self):
        if len(self.active) < 2:
            print ("We can't turn the page. Work!")
        else:
            if self.status:
                self.active.append(active.pop(0))
            else:
                self.kill_page()
                self.active.pop(0)

    def check_page_completed(self):
        current_page = active[0]
        for task in self.pages[current_page]:
            if task.status:
                return false
        return true

    def check_page_full(self):
        if len(self.pages[active[0]]) < self.numstr:
            return false
        else:
            return true

    def change_text(self, index, text):
        self.pages[active[0]][index].text = text

class Entry:

    def __init__(self, text):
        self.text = text
        self.status = 0

    def do_task(self):
        self.status = 1

def copydb():
    with open('tasks.pkl', 'rb') as f:
        db = pickle.load(f)
    return db

def checkcreatefile():
    if not os.path.isfile("tasks.pkl"):
        with open('tasks.pkl', 'wb') as f:
            db = WritingPas(20)
            pickle.dump(db, f)

if __name__ == '__main__':
    
    checkcreatefile()
    db = copydb()

    while msg != 'exit' and msg != 'quit':
        msg = input(">>> ")
        if msg[:4] == "add " and msg[4:]:
            pass
        if msg[:9] == "complete " and msg[9:]:
            pass
        if msg[:15] == "continue later " and msg[15:]:
            pass
        if msg == "turn the page":
            pass
        if msg == "print":
            pass
        if msg == "help":
            print ("add, complete, continue later, "
                   "turn the page, print, exit")
        if msg == "print active":
            pass
        if msg == "print pages":
            pass
        if msg == "print flag":
            pass
        if msg == "save":
            pass
        if msg == "clear":
            pass
        if msg == "backup":
            pass
