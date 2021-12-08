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

# Tkinter Config

root = Tk()
root.title("Contacts - Unfiltered (All)")
root.geometry("854x367")
root.configure(bg="#FFFFFF")
root.resizable(False, False)
root.iconbitmap(r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\Contacts\icons\icon_contacts.ico")


def on_enter(e):
    e.widget['background'] = "#336D96"
    e.widget["foreground"] = "#FFFFFF"


def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'
    e.widget["foreground"] = "#000000"


# External UI

# SQL

filter_all = cursor.execute("select * from contacts where grouped IS NOT (?) order by first_name ASC;", ("Archive",))


# Actions

def nofilter():
    global count
    nofilter = cursor.execute("select * from contacts where grouped IS NOT (?) order by first_name ASC;", ("Archive",))
    tree.delete(*tree.get_children())
    for i in nofilter:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7], i[4],))
        count += 1
    root.title("Contacts - Unfiltered (All)")


def family():
    global count
    filter_family = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Family",))
    tree.delete(*tree.get_children())
    for i in filter_family:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7], i[4],))
        count += 1
    root.title("Contacts - Filtered (Family)")


def friends():
    global count
    filter_friends = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Friend",))
    tree.delete(*tree.get_children())
    for i in filter_friends:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7], i[4],))
        count += 1
    root.title("Contacts - Filtered (Friends)")


def neighbours():
    global count
    filter_neighbours = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;",
                                       ("Neighbour",))
    tree.delete(*tree.get_children())
    for i in filter_neighbours:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7], i[4],))
        count += 1
    root.title("Contacts - Filtered (Neighbours)")


def work():
    global count
    filter_work = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Work",))
    tree.delete(*tree.get_children())
    for i in filter_work:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7], i[4],))
        count += 1
    root.title("Contacts - Filtered (Work)")


def other():
    global count
    filter_other = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Other",))
    tree.delete(*tree.get_children())
    for i in filter_other:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7], i[4],))
        count += 1
    root.title("Contacts - Filtered (Other)")


def archived():
    global count
    filter_other = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Archive",))
    tree.delete(*tree.get_children())
    for i in filter_other:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7], i[4],))
        count += 1
    root.title("Contacts - Filtered (Archived)")


# Widgets
frame1 = Frame(root, bg="#FFFFFF")
frame2 = Frame(root, bg="#FFFFFF")

scrollbar = Scrollbar(frame1, orient=VERTICAL, )
tree = ttk.Treeview(frame1, selectmode=EXTENDED, yscrollcommand=scrollbar.set, height=15)
scrollbar.grid(row=0, column=1, sticky="ns")
scrollbar.config(command=tree.yview)

btn1 = Button(frame2, height=2, width=16, text="All", command=nofilter, activebackground="#336d96",
              activeforeground="#FFFFFF")
btn2 = Button(frame2, height=2, width=16, text="Family", command=family, activebackground="#336d96",
              activeforeground="#FFFFFF")
btn3 = Button(frame2, height=2, width=16, text="Friends", command=friends, activebackground="#336d96",
              activeforeground="#FFFFFF")
btn4 = Button(frame2, height=2, width=16, text="Neighbours", command=neighbours, activebackground="#336d96",
              activeforeground="#FFFFFF")
btn5 = Button(frame2, height=2, width=16, text="Work", command=work, activebackground="#336d96",
              activeforeground="#FFFFFF")
btn6 = Button(frame2, height=2, width=16, text="Other", command=other, activebackground="#336d96",
              activeforeground="#FFFFFF")
btn7 = Button(frame2, height=2, width=16, text="Archived", command=archived, activebackground="#336d96",
              activeforeground="#FFFFFF")

# Treeview

tree["columns"] = ("Name", "Mobile", "Mailbox", "Postcode", "Birthday",)

tree.column("#0", width=120, minwidth=25)
tree.column("Name", anchor=CENTER, width=186)
tree.column("Mobile", anchor=CENTER, width=186)
tree.column("Mailbox", anchor=CENTER, width=270)
tree.column("Postcode", anchor=CENTER, width=96)
tree.column("Birthday", anchor=CENTER, width=96)

tree.heading("#0", text="Label", anchor=W)
tree.heading("Name", text="Name", anchor=CENTER)
tree.heading("Mobile", text="Mobile", anchor=CENTER)
tree.heading("Mailbox", text="Mailbox", anchor=CENTER)
tree.heading("Postcode", text="Postcode", anchor=CENTER)
tree.heading("Birthday", text="Birthday", anchor=CENTER)

tree.column("#0", width=0, stretch=NO)
tree.heading("#0", text="", anchor=W)

for i in filter_all:
    tree.insert(parent="", index="end", iid=count, text="", values=(i[0] + " " + i[1], i[2], i[3], i[7], i[4],))
    count += 1

# Tkinter Layout Management

frame1.grid(column=0, row=0)
frame2.grid(column=0, row=2)

tree.grid(column=0, row=0)

btn1.grid(column=0, row=1)
btn1.bind("<Enter>", on_enter)
btn1.bind("<Leave>", on_leave)

btn2.grid(column=1, row=1)
btn2.bind("<Enter>", on_enter)
btn2.bind("<Leave>", on_leave)

btn3.grid(column=2, row=1)
btn3.bind("<Enter>", on_enter)
btn3.bind("<Leave>", on_leave)

btn4.grid(column=3, row=1)
btn4.bind("<Enter>", on_enter)
btn4.bind("<Leave>", on_leave)

btn5.grid(column=4, row=1)
btn5.bind("<Enter>", on_enter)
btn5.bind("<Leave>", on_leave)

btn6.grid(column=5, row=1)
btn6.bind("<Enter>", on_enter)
btn6.bind("<Leave>", on_leave)

btn7.grid(column=6, row=1)
btn7.bind("<Enter>", on_enter)
btn7.bind("<Leave>", on_leave)

root.mainloop()
