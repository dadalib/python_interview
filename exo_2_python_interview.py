import queue

from tkinter import *
from tkinter.colorchooser import *
from functools import partial
import threading
import time
import re

exitFlag = 0



def make_queue():
    obj = queue.Queue(maxsize=10)
    obj.put(10)
    obj.put(64)
    obj.put(73)
    obj.put("Test")

   
    print(obj.get(1))

def use_tkinter():
    """Exo 63"""
    top = Tk()
    top.title("The putos")
    top.geometry("300x300+200+200")

    top.configure(bg='green')
    uname = Label(top,text = "Username", fg='yellow',bg='green').place(x=30,y=50)
    
    # Creating Label
    password = Label(top,text= "Password",bg='green',fg='yellow').place(x=30,y=90)
    
    sbmitn = Button(top,text="Submit",bg = "yellow",fg="green").place(x=100,y=120)
    top.mainloop()

def excercie100():
    pass

def display(answer,mylist):
    """Exo 67"""
    a = mylist.get(ACTIVE)
    answer.config(text=a)
    return


def sleep_time():
    sleep_time = 1
    print('Hello')
    time.sleep(sleep_time)
    print('Students')
    time.sleep(sleep_time)
    print("Hope you all are doing well")

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def print_ime(threadName,counter,delay):
        while counter:
            if exitFlag:
                threadName.exit()
                time.sleep(delay)
                print("%s: %s" % (threadName,time.ctime(time.time())))
                counter -=1

def check_phone_number(phone):
    """Using regex"""

    if re.search('\d{10}',phone):
        print("Phone Num: ",phone)

    else:
        print("invalid")

def validate_email(email):
    """Using regex"""
    regex = '@'
    if re.search(regex,email):
        print("Valid Email")
    else:
        print("Invalid email")

def read_line_existing_file():
    fo = open("test.py","r")

    str = fo.read(10)
    print("Read String is : ",str)
    fo.close()

def write_file():
    fw = open("name.txt","w")

    for i in range(1,6):
        print("Enter name")
        name = input()
        fw.write("Name\t" + name+"\n")
    fw.close()

def file_manipulation():
    """File Manipulation"""

    with open("hello.txt","w") as f:
        f.write("Good Morning Students") 
    
    with open('hello.txt','r') as f:
        data = f.readlines()
        for line in data:
            words = line.split()

        print(words)
        f.close()


    



if __name__ == "__main__":
    # make_queue()
    # use_tkinter()
    # top = Tk()
    # sb = Scrollbar(top)
    # sb.pack(side = RIGHT, fill = Y)
    # Lb=Label(top,text="select Favourite Fruit")
    # mylist = Listbox(top, yscrollcommand = sb.set)
    # answer=Label(top)

    # display=partial(display,answer,mylist)
    # b=Button(top,text="Show",command=display)

    # mylist.insert(1,"Kiwi")
    # mylist.insert(2,"Mango")
    # mylist.insert(3,"papaya")
    # mylist.insert(4,"Orange")
    # mylist.insert(5,"Apple")

    # Lb.pack()
    # mylist.pack(side = LEFT)
    # sb.config(command = mylist.yview)
    # b.pack(side=LEFT)
    # answer.pack(side=RIGHT)

    # mainloop()
    
    # sleep_time()
    # check_phone_number("0488129002")

    # validate_email("darwni.liiboullegmail.com")
    # read_line_existing_file()
    # write_file()
    file_manipulation()





