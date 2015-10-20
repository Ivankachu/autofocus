class WritingPad:

    def __init__(self, numstr):
        self.numstr = numstr
        self.status = False
        self.acitve = []
        self.pages = []

    def add_task(self, task):
        if len(self.pages[-1]) < self.numstr:
            self.pages[-1].append(task)
        else:
            self.pages.append([task])

    def do_task(self, task):
        pass

    def contin_later(self, task):
        pass

    def kill_page(self):
        pass

    def turn_the_page(self):
        pass


class Entry:

    def __init__(self, task):
        self.task = task
        self.status = 0

    def do_task(self):
        self.status = 1
