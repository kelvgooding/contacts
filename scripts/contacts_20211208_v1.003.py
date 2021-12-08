# Modules

from tkinter import *
from tkinter import ttk

# Variables

import sqlite3
import os

# Variables
count = 0
user = os.getlogin()

# Database Connection

connection = sqlite3.connect(fr"C:\Users\{user}\Dropbox\Programming\Databases\contacts.db")
cursor = connection.cursor()
print("Successfully Connected to SQLite3!\n")

# Tkinter Config

root = Tk()
root.title("Contacts")
root.geometry("731x363")
root.configure(bg="#374A6C")
root.resizable(False, False)

# External UI

# SQL

filter_all = cursor.execute("select * from contacts where grouped IS NOT (?) order by first_name ASC;", ("Hidden",))

# Actions

def nofilter():
    global count
    nofilter = cursor.execute("select * from contacts where grouped IS NOT (?) order by first_name ASC;", ("Hidden",))
    tree.delete(*tree.get_children())
    for i in nofilter:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7],))
        count += 1

def family():
    global count
    filter_family = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Family",))
    tree.delete(*tree.get_children())
    for i in filter_family:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7],))
        count += 1

def friends():
    global count
    filter_friends = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Friends",))
    tree.delete(*tree.get_children())
    for i in filter_friends:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7],))
        count += 1

def neighbours():
    global count
    filter_neighbours = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Neighbours",))
    tree.delete(*tree.get_children())
    for i in filter_neighbours:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7],))
        count += 1

def work():
    global count
    filter_work = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Work",))
    tree.delete(*tree.get_children())
    for i in filter_work:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7],))
        count += 1

def other():
    global count
    filter_other = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Other",))
    tree.delete(*tree.get_children())
    for i in filter_other:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7],))
        count += 1

def hidden():
    global count
    filter_hidden = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Hidden",))
    tree.delete(*tree.get_children())
    for i in filter_hidden:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7],))
        count += 1

# Widgets
frame1 = Frame(root, bg="#374A6C")
frame2 = Frame(root, bg="#374A6C")

scrollbar = Scrollbar(frame1, orient=VERTICAL,)
tree = ttk.Treeview(frame1, selectmode=EXTENDED, yscrollcommand=scrollbar.set, height=14)
scrollbar.grid(row=0, column=1, sticky="ns")
scrollbar.config(command=tree.yview)

btn1 = Button(frame2, height=3, width=16, text="All", command=nofilter)
btn2 = Button(frame2, height=3, width=16, text="Family", command=family)
btn3 = Button(frame2, height=3, width=16, text="Friends", command=friends)
btn4 = Button(frame2, height=3, width=16, text="Neighbours", command=neighbours)
btn5 = Button(frame2, height=3, width=16, text="Work", command=work)
btn6 = Button(frame2, height=3, width=16, text="Other", command=other)

# Treeview

tree["columns"] = ("Name", "Mobile", "Mailbox", "Postcode",)

tree.column("#0", width=120, minwidth=25)
tree.column("Name", anchor=CENTER, width=160)
tree.column("Mobile", anchor=CENTER, width=160)
tree.column("Mailbox", anchor=CENTER, width=311)
tree.column("Postcode", anchor=CENTER, width=80)

tree.heading("#0", text="Label", anchor=W)
tree.heading("Name", text="Name", anchor=CENTER)
tree.heading("Mobile", text="Mobile", anchor=CENTER)
tree.heading("Mailbox", text="Mailbox", anchor=CENTER)
tree.heading("Postcode", text="Postcode", anchor=CENTER)

tree.column("#0", width=0, stretch=NO)
tree.heading("#0", text="", anchor=W)

for i in filter_all:
    tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7],))
    count += 1

# Tkinter Layout Management

frame1.grid(column=0, row=0)
frame2.grid(column=0, row=2)

tree.grid(column=0, row=0)

btn1.grid(column=0, row=1)
btn2.grid(column=1, row=1)
btn3.grid(column=2, row=1)
btn4.grid(column=3, row=1)
btn5.grid(column=4, row=1)
btn6.grid(column=5, row=1)

root.mainloop()
