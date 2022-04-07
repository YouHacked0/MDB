import pymongo as c
from tkinter import *
import create_backup as backup
import config
import language_ru
import language_en

if config.language == "language_ru":
    name=language_ru.name
    age=language_ru.age
    rank=language_ru.rank
    salary=language_ru.salary
    enter=language_ru.enter
    type=language_ru.type
    value=language_ru.value
elif config.language == "language_en":
    name=language_en.name
    age=language_en.age
    rank=language_en.rank
    salary=language_en.salary
    enter=language_en.enter
    type=language_en.type
    value=language_en.value


def guiinsert():
    global e11
    global txt11
    global e12
    global txt12
    global e13
    global txt13
    global e14
    global txt14

    win = Toplevel(root)
    win.geometry("500x500")

    txt11 = Label(win, text=name)
    txt11.pack()

    e11 = Entry(win, width=13)
    e11.pack()

    txt12 = Label(win, text=age)
    txt12.pack()

    e12 = Entry(win, width=3)
    e12.pack()

    txt13 = Label(win, text=rank)
    txt13.pack()

    e13 = Entry(win, width=2)
    e13.pack()

    txt14 = Label(win, text=salary)
    txt14.pack()

    e14 = Entry(win, width=10)
    e14.pack()

    btn1 = Button(win, text="Enter", command=insert)
    btn1.pack()


def insert():
    user = {}
    user['personal_data'] = str(e11.get())
    user['age'] = str(e12.get())
    user['salary'] = str(e14.get())
    user['rank'] = str(e13.get())
    res = collections.insert_one(user)


def guiedit():
    global e31
    global txt31
    global e32
    global txt32
    global e33
    global e30
    win = Toplevel(root)
    win.geometry("500x500")

    txt31 = Label(win, text=name)
    txt31.pack()

    e31 = Entry(win, width=13)
    e31.pack()

    txt32 = Label(win, text=type)
    txt32.pack()

    e32 = Entry(win, width=13)
    e32.pack()

    txt33 = Label(win, text=value)
    txt33.pack()

    e33 = Entry(win, width=13)
    e33.pack()

    btn3 = Button(win, text=enter, command=edit)
    btn3.pack()


def edit():
    if e31.get() != "Все":
        type = str(e32.get())
        if type == "имя": type = "personal_data"
        elif type == "ранг": type = "rank"
        elif type == "зарплата": type = "salary"
        elif type == "возраст": type = "age"
        user = {}
        user['personal_data'] = str(e31.get())
        rank = {}
        rank[type] = str(e33.get())
        for users in collections.find({}):
            if user == users:
                user[type] = users[type]
        res = collections.update_one(user, {"$set": rank})
    if e31.get() == "Все":
        type = str(e32.get())
        rank = {}
        rank[type] = str(e33.get())
        if type == "имя":
            for human in collections.find({}):
                human['personal_data'] = e33.get()
        elif type == "ранг":
            for human in collections.find({}):
                human['rank'] = e33.get()
        elif type == "зарплата":
            for human in collections.find({}):
                human['salary'] = e33.get()
        elif type == "возраст":
            for human in collections.find({}):
                human['age'] = e33.get()
        res = collections.update_many({"$set": rank})

def guiremove():
    global e21
    global txt21

    win = Toplevel(root)
    win.geometry("500x500")

    txt21 = Label(win, text=name)
    txt21.pack()

    e21 = Entry(win, width=13)
    e21.pack()

    btn2 = Button(win, text=enter, command=delete)
    btn2.pack()


def delete():
    user = {}
    user['personal_data'] = str(e21.get())
    res = collections.delete_one(user)


def gui_users():
    win = Toplevel(root)
    win.geometry("1000x500")

    # txt41 = Label(win, text=[listt for listt in collections.find({})])
    txt41 = Label(win, text=get_users())
    txt41.pack()


def get_users():
    users = ""
    for i in collections.find({}):
        users += str(i)
        users += "\n"
    return users


def guicount_users():
    win = Toplevel(root)
    win.geometry("1000x500")

    # txt41 = Label(win, text=[listt for listt in collections.find({})])
    txt41 = Label(win, text=count_users())
    txt41.pack()


def count_users():
    users = 0
    for i in collections.find({}):
        users += 1
    return users


def guiinfo():
    global e41
    global status1

    win = Toplevel(root)
    win.geometry("1000x300")

    txt41 = Label(win, text=name)
    txt41.pack()

    e41 = Entry(win, width=13)
    e41.pack()

    btn = Button(win, text=enter, command=info)
    btn.pack()

    status1 = Label(win, text="...")
    status1.pack()


def info():
    fio = str(e41.get())
    status1.configure(text=collections.find_one({'personal_data': fio}))

# SalaryManager
def clicksredn():
     win = Toplevel(root)
     out = Label(win, text=sredn_salary())
     out.pack()

def sredn_salary():
    allusers = 0
    for x in collections.find({}):
        allusers += 1
    sum_ = 0
    for i in collections.find({}):
       sum_ += int(i['salary'])
    return sum_ // allusers

def clicksum():
    win = Toplevel(root)
    out = Label(win, text=sum_salary())
    out.pack()

def sum_salary():
    sum_salary_ = 0
    for i in collections.find({}):
        sum_salary_ += int(i['salary'])
    return sum_salary_

def clickmax_and_min():
    win = Toplevel(root)
    out = Label(win, text=max_and_min())
    out.pack()

def max_and_min():
    salary = []
    for i in collections.find({}):
        salary.append(int(i['salary']))
        maximum = max(salary)
        minimum = min(salary)
    return {'max': maximum, 'min': minimum}


def createbackup():
    backup.add()


root = Tk()
root.geometry("1000x500")
root.title("MongoDB Graphic Interface")
db_client = c.MongoClient(config.url)
current_db = db_client[config.db_name]
collections = current_db[config.collection_name]


insert_ = Button(root, text="✘ Add", command=guiinsert)
edit_ = Button(root, text="✘ Edit", command=guiedit)
del_ = Button(root, text="✘ Del", command=guiremove)
getusers_ = Button(root, text="✘ List", command=gui_users)
info_ = Button(root, text="✘ Info", command=guiinfo)
sredn_salary_ = Button(root, text="✘ Srednaya Salary", command=clicksredn)
sum_salary_ = Button(root, text="✘ Sum Salary", command=clicksum)
max_and_min_ = Button(root, text="✘ Max and Min", command=clickmax_and_min)
createbackup_ = Button(root, text="✘ Create Backup", command=createbackup)
count_ = Button(root, text="✘ Count Users", command=guicount_users)
insert_.pack()
edit_.pack()
del_.pack()
getusers_.pack()
info_.pack()
sredn_salary_.pack()
sum_salary_.pack()
max_and_min_.pack()
count_.pack()
createbackup_.pack()


root.mainloop()