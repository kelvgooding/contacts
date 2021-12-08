# Modules

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Variables

import sqlite3
import os

user = os.getlogin()

connection = sqlite3.connect(fr"C:\Users\{user}\Dropbox\Programming\Databases\contacts.db")
cursor = connection.cursor()
print("Successfully Connected to SQLite3!\n")

# Database Connection

# Tkinter Config

root = Tk()
root.title("Kontacts")
root.geometry("1000x500")
root.configure(bg="#374A6C")
root.resizable(False, False)

# External UI

# SQL

filter_all = cursor.execute("SELECT * FROM contacts order by grouped ASC, first_name;")


# Actions

def filter_family():
    family = ("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Family",))


def filter_friends():
    friend = ("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Friends",))


def filter_neighbours():
    neighbours = ("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Neighbours",))


def filter_work():
    work = ("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Work",))


def filter_other():
    other = ("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Other",))


def filter_hidden():
    hidden = ("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Hidden",))


# Widgets

frame1 = Frame(root, padx=50, pady=25, bg="#374A6C")
frame2 = Frame(root, padx=50, pady=5, bg="#374A6C")
frame3 = Frame(root, padx=50, pady=5, bg="#374A6C")

tree = ttk.Treeview(frame1)

lbl1 = Label(frame2, text="Name", bg="#374A6C", fg="#FFFFFF")
lbl2 = Label(frame2, text="Mobile", bg="#374A6C", fg="#FFFFFF")
lbl3 = Label(frame2, text="Mailbox", bg="#374A6C", fg="#FFFFFF")

E1 = Entry(frame2, width=29)
E2 = Entry(frame2, width=29)
E3 = Entry(frame2, width=29)

btn1 = Button(frame3, height=3, width=16, text="Family", command=filter_family)
btn2 = Button(frame3, height=3, width=16, text="Friends", command=filter_friends)
btn3 = Button(frame3, height=3, width=16, text="Neighbours", command=filter_neighbours)
btn4 = Button(frame3, height=3, width=16, text="Work", command=filter_work)
btn5 = Button(frame3, height=3, width=16, text="Other", command=filter_other)
btn6 = Button(frame3, height=3, width=16, text="Hidden", command=filter_hidden)

# Treeview

tree["columns"] = ("Name", "Mobile", "Mailbox", "Postcode", "Group",)

tree.column("#0", width=120, minwidth=25)
tree.column("Name", anchor=W, width=150)
tree.column("Mobile", anchor=CENTER, width=150)
tree.column("Mailbox", anchor=CENTER, width=300)
tree.column("Postcode", anchor=CENTER, width=80)
tree.column("Group", anchor=CENTER, width=80)

tree.heading("#0", text="Label", anchor=W)
tree.heading("Name", text="Name", anchor=W)
tree.heading("Mobile", text="Mobile", anchor=CENTER)
tree.heading("Mailbox", text="Mailbox", anchor=CENTER)
tree.heading("Postcode", text="Postcode", anchor=CENTER)
tree.heading("Group", text="Group", anchor=CENTER)

tree.column("#0", width=0, stretch=NO)
tree.heading("#0", text="", anchor=W)

count = 0
for i in filter_all:
    tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[3], i[4], i[7], i[8]))
    count += 1

# Tkinter Layout Management

frame1.grid(column=0, row=0)
frame2.grid(column=0, row=1)
frame3.grid(column=0, row=2)

tree.grid(column=0, row=0)

btn1.grid(column=0, row=1, pady=10)
btn2.grid(column=1, row=1, pady=10)
btn3.grid(column=2, row=1, pady=10)
btn4.grid(column=3, row=1, pady=10)
btn5.grid(column=4, row=1, pady=10)
btn6.grid(column=5, row=1, pady=10)

lbl1.grid(column=0, row=0, pady=10, padx=50)
E1.grid(column=0, row=1, pady=10, padx=50)

lbl2.grid(column=1, row=0, pady=10, padx=50)
E2.grid(column=1, row=1, pady=10, padx=50)

lbl3.grid(column=2, row=0, pady=10, padx=50)
E3.grid(column=2, row=1, pady=10, padx=50)

root.mainloop()
