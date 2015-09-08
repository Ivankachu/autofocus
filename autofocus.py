import pickle
import os

num_ts = 20 #Number of tasks in a page

def copydb():
    with open('tasks.pkl', 'rb') as f:
        db = pickle.load(f)
    return db

def print_agenda(active, pages):
    if len(active):
        print ('=' * 35)
        for (index, task) in enumerate(pages[active[0]]):
            if not task[1]:  #if task is not undone (1, not 0)
                print (' {:2}  {}'.format(index, task[0]))
        print ('=' * 35)
    else:
        print ("All tasks you planned are completed.")

def add(new_task, active, pages):
    if len(pages):
        if len(pages[-1]) < num_ts:
            pages[-1].append([new_task, 0])  #Add a new task in the last page.
        else:
            pages.append([[new_task, 0]])    #Add a new page and a new task in it.
            index_new_page = len(pages) - 1
            if active:                       #If there is something in active list
                place_max = active.index(max(active))
                active.insert(place_max + 1, index_new_page)
            else:
                active.append(index_new_page)
    else:
        pages.append([[new_task, 0]])
        active.append(0)
    savedb(flag, active, pages)

def complete(index_task, flag, active, pages):
    if 0 <= index_task < num_ts:
        if not pages[active[0]][index_task][1]:
            flag = True
            pages[active[0]][index_task][1] = 1
            check_active_page_completed()  #For the case if all tasks in the page is completed
            savedb(flag, active, pages)
        else:
            print ("The task is already completed")
    else:
        print ("Bad number. It must be from 0 to 19")

def continue_later(index_task, active, pages):
    task = pages[active[0]][index_task][0]
    complete(index_task)
    add(task, active, pages)

def demolish_page(active, pages):
    for task in pages[active[0]]:
        task[1] = 1
    del active[0]

def turn_the_page():
    global flag, active
    if len(active):
        if flag:
            flag = False
            active = active[1:] + [active[0]]
            if __name__ == '__main__':
                print_agenda(active, pages)
        elif pages[active[0]] is not pages[-1]:
            if __name__ == '__main__':
                print ("The active page is not started yet.")
                print ("If you turn the page, all uncompleted tasks will be demolished.")
                print ("Are you sure you want to turn the page?")
                msg1 = input("Yes or No?  ")
                if msg1 == "Yes":
                    demolish_page(active, pages)
                print_agenda(active, pages)
            else:
                demolish_page(active, pages)
        elif __name__ == '__main__':
            print ('You cannot turn the last page without completing something!')

def is_page_full(number_of_page):
    if len(pages[number_of_page]) == num_ts:
        return True
    else:
        return False

def check_active_page_completed():
    for task in pages[active[0]]:
        if not task[1]:
            break
    else:
        del pages[0]

def print_active_pages():
    print (active)

def print_pages():
    for (index, page) in enumerate(pages):
        print ("\n")
        print ("page ", index)
        for (indext, task) in enumerate(page):
            print (indext, task)
			
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def savedb(flag, active, pages):
    with open('tasks.pkl', 'wb') as f:
        pickle.dump([flag, active, pages], f)

if __name__ == '__main__':

    flag, active, pages = copydb()
    
    print_agenda(active, pages)

    msg = ''

    while msg != 'exit' and msg != 'quit':
        msg = input(">>> ")

        if msg[:3] == "add" and msg[4:]:
            add(msg[4:], active, pages)

        if msg[:8] == "complete" and msg[9:]:
            complete(int(msg[9:]), flag, active, pages)

        if msg[:14] == "continue later" and msg[15:]:
            continue_later(int(msg[15:]), active, pages)

        if msg == "turn the page":
            turn_the_page()
                    
        if msg == "print":
            print_agenda(active, pages)

        if msg == "help":
            print ("add, complete, continue later, turn the page, print, exit")

        if msg == "print active":
            print_active_pages()

        if msg == "print pages":
            print_pages()

        if msg == "print flag":
            print (flag)

        if msg == "save":
            savedb(flag, active, pages)

        if msg == 'clear':
            clear()
    savedb(flag, active, pages)
