class WritingPad:

    def __init__(self, numstr):
        self.numstr = numstr

    def add_task(self, task):
        pass

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
