class WritingPad:

    def __init__(self, numstr):
        self.numstr = numstr
        self.status = False
        self.acitve = []
        self.pages = []

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
        pass

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
