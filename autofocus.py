import pickle
import os

num_ts = 20 #Number of tasks in a page

with open('tasks.pkl', 'rb') as f:
    flag, active, pages = pickle.load(f)

def print_agenda():
    print ('=' * 35)
    for (index, task) in enumerate(pages[active[0]]):
        if not task[1]:  #if task is not undone (1, not 0)
            print (' {:2}  {}'.format(index, task[0]))
    print ('=' * 35)

def add(new_task):
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

def complete(index_task):
    global flag
    if 0 <= index_task < num_ts:
        if not pages[active[0]][index_task][1]:
            flag = True
            pages[active[0]][index_task][1] = 1
            check_active_page_completed()  #For the case if all tasks in the page is completed
        else:
            print ("The task is already completed")
    else:
        print ("Bad number. It must be from 0 to 19")

def continue_later(index_task):
    task = pages[active[0]][index_task][0]
    complete(index_task)
    add(task)

def turn_the_page():
    global flag, active
    if len(active) > 1:
        if flag:
            flag = False
            active = active[1:] + [active[0]]
        else:
            for task in pages[active[0]]:
                task[1] = 1
            del active[0]
        print_agenda()

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

def print_flag():
    print (flag)

def save():
    with open('tasks.pkl', 'wb') as f:
        pickle.dump([flag, active, pages], f)

if __name__ == '__main__':
    if len(active):
        print_agenda()
    else:
        print ("All tasks you planned are completed.")

    msg = ''

    while msg != 'exit' and msg != 'quit':
        msg = input(">>> ")

        if msg[:3] == "add" and msg[4:]:
            add(msg[4:])

        if msg[:8] == "complete" and msg[9:]:
            complete(int(msg[9:]))

        if msg[:14] == "continue later" and msg[15:]:
                continue_later(int(msg[15:]))

        if msg == "turn the page":
            if flag:
                turn_the_page()
                print ("Done!")
            else:
                print ("The active page is not started yet.")
                print ("If you turn the page, all uncompleted tasks will be demolished.")
                print ("Are you sure you want to turn the page?")
                msg1 = input("Yes or No?    ")
                if msg1 == "Yes":
                    turn_the_page()
                    
        if msg == "print":
            print_agenda()

        if msg == "help":
            print ("add, complete, continue later, turn the page, print, exit")

        if msg == "print active":
            print_active_pages()

        if msg == "print pages":
            print_pages()

        if msg == "print flag":
            print_flag()

        if msg == "save":
            save()

        if msg == 'clear':
            clear()
            
save()
