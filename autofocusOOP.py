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

    def contin_later(self, task):
        pass

    def kill_page(self):
        pass

    def turn_the_page(self):
        pass


class Entry:

    def __init__(self, text):
        self.text = text
        self.status = 0

    def do_task(self):
        self.status = 1
