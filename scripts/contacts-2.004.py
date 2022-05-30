# Release Notes

"""
Version 2.004 Release Notes

- FocusIn and FocusOut have been added to all field on the Add page.
- Application will start centered.

"""

# Modules

from tkinter import *
from tkinter import ttk, Frame
import sqlite3
import os
from tkinter import messagebox

# Variables

count = 0
user = os.getlogin()

# Database Connection

connection = sqlite3.connect(fr"C:\Users\{user}\Dropbox\Dev\Python\Projects\Contacts\db\contacts.db")
cursor = connection.cursor()

# Tkinter Config

root = Tk()
root.title("Contacts - Unfiltered (All)")
root.geometry("854x387+75+75")
root.configure(bg="#FFFFFF")
root.resizable(False, False)
root.iconbitmap(fr"C:\Users\{user}\Dropbox\Dev\Python\Projects\Contacts\media\icons\icon_contacts.ico")

def on_enter(e):
    e.widget['background'] = "#336D96"
    e.widget["foreground"] = "#FFFFFF"


def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'
    e.widget["foreground"] = "#000000"


# SQL

filter_all = cursor.execute("select * from contacts where grouped IS NOT (?) order by first_name ASC;", ("Archived",))


# Actions

def nofilter():
    global count
    nofilter = cursor.execute("select * from contacts where grouped IS NOT (?) order by first_name ASC;", ("Archived",))
    tree.delete(*tree.get_children())
    for i in nofilter:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[2], i[3], i[4], i[8], i[5],))
        count += 1
    root.title("Contacts - Unfiltered (All)")


def family():
    global count
    filter_family = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Family",))
    tree.delete(*tree.get_children())
    for i in filter_family:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[2], i[3], i[4], i[8], i[5],))
        count += 1
    root.title("Contacts - Filtered (Family)")


def friends():
    global count
    filter_friends = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Friends",))
    tree.delete(*tree.get_children())
    for i in filter_friends:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[2], i[3], i[4], i[8], i[5],))
        count += 1
    root.title("Contacts - Filtered (Friends)")


def neighbours():
    global count
    filter_neighbours = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;",
                                       ("Neighbours",))
    tree.delete(*tree.get_children())
    for i in filter_neighbours:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[2], i[3], i[4], i[8], i[5],))
        count += 1
    root.title("Contacts - Filtered (Neighbours)")


def work():
    global count
    filter_work = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Work",))
    tree.delete(*tree.get_children())
    for i in filter_work:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[2], i[3], i[4], i[8], i[5],))
        count += 1
    root.title("Contacts - Filtered (Work)")


def other():
    global count
    filter_other = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Other",))
    tree.delete(*tree.get_children())
    for i in filter_other:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[2], i[3], i[4], i[8], i[5],))
        count += 1
    root.title("Contacts - Filtered (Other)")


def archived():
    global count
    filter_other = cursor.execute("SELECT * FROM contacts where grouped=(?) order by first_name ASC;", ("Archived",))
    tree.delete(*tree.get_children())
    for i in filter_other:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[2], i[3], i[4], i[8], i[5],))
        count += 1
    root.title("Contacts - Filtered (Archived)")


def hide_all_frames():
    action_add_frame1.grid_forget()
    action_modify_frame1.grid_forget()
    frame1.grid_forget()
    frame2.grid_forget()


def button_home():
    # Hide all frames previously showing

    hide_all_frames()

    # Show default frames

    frame1.grid()
    frame2.grid()

    # Resize Window

    root.geometry("854x367")
    root.title("Contacts - Unfiltered (All)")


def menu_add():
    # List of Groups

    groups = ["Family", "Friends", "Neighbours", "Work", "Other", "Archived"]

    # Hide Previous Frames

    hide_all_frames()

    # Geometry

    root.geometry("500x428")
    root.config(bg="#9DB0CF")
    root.title("Contacts - Add")

    # Frames

    action_add_frame1.grid(column=0, row=0, sticky="nsew")

    action_add_frame2 = Frame(action_add_frame1, pady=10, padx=20, bg="#9DB0CF")
    action_add_frame2.grid(column=0, row=1)

    action_add_labelframe2 = LabelFrame(action_add_frame2, text="Contact Details", bg="#9DB0CF", pady=5)
    action_add_labelframe2.grid(column=0, row=0, pady=5)

    action_add_labelframe3 = LabelFrame(action_add_frame2, text="Address", bg="#9DB0CF", pady=5)
    action_add_labelframe3.grid(column=0, row=1, pady=5)

    action_add_frame3 = Frame(action_add_frame2, bg="#9DB0CF", pady=5)
    action_add_frame3.grid(column=0, row=2, pady=5)

    # Field - First Name

    Label3 = Label(action_add_labelframe2, text="First Name:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label3.grid(column=0, row=4)
    field1 = Entry(action_add_labelframe2, font="Arial 10", width=40, fg="#999999")
    field1.insert(END, "Enter First Name")
    field1.grid(column=1, row=4, padx=20, pady=5)

    def field1_firstname(e):
        if field1.get() == "Enter First Name":
            field1.delete(0, "end")
            field1.config(fg="#000000")
        elif field1.get() == "":
            field1.insert(END, "Enter First Name")
            field1.config(fg="#999999")
        else:
            field1.config(fg="#000000")

    field1.bind("<FocusIn>", field1_firstname)
    field1.bind("<FocusOut>", field1_firstname)

    # Field - Last Name

    Label4 = Label(action_add_labelframe2, text="Last Name:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label4.grid(column=0, row=5)
    field2 = Entry(action_add_labelframe2, font="Arial 10", width=40, fg="#999999")
    field2.insert(END, "Enter Last Name")
    field2.grid(column=1, row=5, padx=20, pady=5)

    def field2_lastname(e):
        if field2.get() == "Enter Last Name":
            field2.delete(0, "end")
            field2.config(fg="#000000")
        elif field2.get() == "":
            field2.insert(END, "Enter Last Name")
            field2.config(fg="#999999")
        else:
            field2.config(fg="#000000")

    field2.bind("<FocusIn>", field2_lastname)
    field2.bind("<FocusOut>", field2_lastname)

    # Field - Number

    Label6 = Label(action_add_labelframe2, text="Number:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label6.grid(column=0, row=7)
    field4 = Entry(action_add_labelframe2, font="Arial 10", width=40, fg="#999999")
    field4.insert(END, "+44 XXXX XXX XXX")
    field4.grid(column=1, row=7, padx=20, pady=5)

    def field4_mobilenumber(e):
        if field4.get() == "+44 XXXX XXX XXX":
            field4.delete(0, "end")
            field4.config(fg="#000000")
        elif field4.get() == "":
            field4.insert(END, "+44 XXXX XXX XXX")
            field4.config(fg="#999999")
        else:
            field4.config(fg="#000000")

    field4.bind("<FocusIn>", field4_mobilenumber)
    field4.bind("<FocusOut>", field4_mobilenumber)

    # Field - Mailbox

    Label7 = Label(action_add_labelframe2, text="Mailbox:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label7.grid(column=0, row=8)
    field5 = Entry(action_add_labelframe2, font="Arial 10", width=40, fg="#999999")
    field5.insert(END, "john.doe@example.com")
    field5.grid(column=1, row=8, padx=20, pady=5)

    def field5_mailbox(e):
        if field5.get() == "john.doe@example.com":
            field5.delete(0, "end")
            field5.config(fg="#000000")
        elif field5.get() == "":
            field5.insert(END, "john.doe@example.com")
            field5.config(fg="#999999")
        else:
            field5.config(fg="#000000")

    field5.bind("<FocusIn>", field5_mailbox)
    field5.bind("<FocusOut>", field5_mailbox)

    # Field - Birthday

    Label8 = Label(action_add_labelframe2, text="Birthday:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label8.grid(column=0, row=9)
    field6 = Entry(action_add_labelframe2, font="Arial 10", width=40, fg="#999999")
    field6.insert(END, "DD/MM")
    field6.grid(column=1, row=9, padx=20, pady=5)

    def field6_birthday(e):
        if field6.get() == "DD/MM":
            field6.delete(0, "end")
            field6.config(fg="#000000")
        elif field6.get() == "":
            field6.insert(END, "DD/MM")
            field6.config(fg="#999999")
        else:
            field6.config(fg="#000000")

    field6.bind("<FocusIn>", field6_birthday)
    field6.bind("<FocusOut>", field6_birthday)

    # Field - Street

    Label9 = Label(action_add_labelframe3, text="Street:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label9.grid(column=0, row=8)
    field7 = Entry(action_add_labelframe3, font="Arial 10", width=40, fg="#999999")
    field7.insert(END, "Enter Street Name")
    field7.grid(column=1, row=8, padx=20, pady=5)

    def field7_street(e):
        if field7.get() == "Enter Street Name":
            field7.delete(0, "end")
            field7.config(fg="#000000")
        elif field7.get() == "":
            field7.insert(END, "Enter Street Name")
            field7.config(fg="#999999")
        else:
            field7.config(fg="#000000")

    field7.bind("<FocusIn>", field7_street)
    field7.bind("<FocusOut>", field7_street)

    # Field - City/Town

    Label10 = Label(action_add_labelframe3, text="City/Town:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label10.grid(column=0, row=9)
    field8 = Entry(action_add_labelframe3, font="Arial 10", width=40, fg="#999999")
    field8.insert(END, "Enter City/Town")
    field8.grid(column=1, row=9, padx=20, pady=5)

    def field8_citytown(e):
        if field8.get() == "Enter City/Town":
            field8.delete(0, "end")
            field8.config(fg="#000000")
        elif field8.get() == "":
            field8.insert(END, "Enter City/Town")
            field8.config(fg="#999999")
        else:
            field8.config(fg="#000000")

    field8.bind("<FocusIn>", field8_citytown)
    field8.bind("<FocusOut>", field8_citytown)

    # Field - Postcode

    Label11 = Label(action_add_labelframe3, text="Postcode:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label11.grid(column=0, row=10)
    field9 = Entry(action_add_labelframe3, font="Arial 10", width=40, fg="#999999")
    field9.insert(END, "Enter Postcode")
    field9.grid(column=1, row=10, padx=20, pady=5)

    def field9_postcode(e):
        if field9.get() == "Enter Postcode":
            field9.delete(0, "end")
            field9.config(fg="#000000")
        elif field9.get() == "":
            field9.insert(END, "Enter Postcode")
            field9.config(fg="#999999")
        else:
            field9.config(fg="#000000")

    field9.bind("<FocusIn>", field9_postcode)
    field9.bind("<FocusOut>", field9_postcode)

    # Field - Group

    Label12 = Label(action_add_labelframe3, text="Group:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label12.grid(column=0, row=11)
    field10 = ttk.Combobox(action_add_labelframe3, value=groups, width=44)
    field10.grid(column=1, row=11, padx=20, pady=5)

    def add():
        if field1.get() == "Enter First Name":
            field1.delete(0, END)
            field1.insert(END, "-")
        if field2.get() == "Enter Last Name":
            field2.delete(0, END)
            field2.insert(END, "-")
        if field4.get() == "+44 XXXX XXXX XXX":
            field2.delete(0, END)
            field4.insert(END, "-")
        if field5.get() == "john.doe@example.com":
            field5.delete(0, END)
            field5.insert(END, "-")
        if field6.get() == "DD/MM":
            field6.delete(0, END)
            field6.insert(END, "-")
        if field7.get() == "Enter Street Name":
            field7.delete(0, END)
            field7.insert(END, "-")
        if field8.get() == "Enter City/Town":
            field8.delete(0, END)
            field8.insert(END, "-")
        if field9.get() == "Enter Postcode":
            field9.delete(0, END)
            field9.insert(END, "-")
        cursor.execute(f"INSERT INTO contacts values (?,?,?,?,?,?,?,?,?,?)",
                       (field1.get(), field2.get(), f"{field1.get()} {field2.get()}", field4.get(), field5.get(), field6.get(),
                        field7.get(), field8.get(), field9.get(), field10.get()))
        connection.commit()
        messagebox.showinfo("Contacts - Add", "A new contact has now been added!")
        field1.delete(0, END)
        field2.delete(0, END)
        field4.delete(0, END)
        field5.delete(0, END)
        field6.delete(0, END)
        field7.delete(0, END)
        field8.delete(0, END)
        field9.delete(0, END)
        field10.delete(0, END)

    # Search Button

    BTN1_add = Button(action_add_frame3, text="Add", command=add, height=2, width=16, activebackground="#336d96", activeforeground="#FFFFFF")
    BTN1_add.grid(column=0, row=0, padx=10)
    BTN1_add.bind("<Enter>", on_enter)
    BTN1_add.bind("<Leave>", on_leave)

    # Update Button

    BTN2_update = Button(action_add_frame3, text="Home", command=button_home, height=2, width=16, activebackground="#336d96", activeforeground="#FFFFFF")
    BTN2_update.grid(column=1, row=0, padx=10)
    BTN2_update.bind("<Enter>", on_enter)
    BTN2_update.bind("<Leave>", on_leave)


def menu_modify():
    # Hide All Frames

    hide_all_frames()

    # Geometry

    root.geometry("500x590")
    root.config(bg="#9DB0CF")
    root.title("Contacts - Modify (Update / Delete)")

    # Frames

    action_modify_frame1.grid(column=0, row=0, sticky="nsew")

    action_update_frame2 = Frame(action_modify_frame1, pady=10, padx=20, bg="#9DB0CF")
    action_update_frame2.grid(column=0, row=1)

    action_update_labelframe1 = LabelFrame(action_update_frame2, text="Search Contact", bg="#9DB0CF", pady=5)
    action_update_labelframe1.grid(column=0, row=0, pady=5)

    action_update_labelframe4 = Frame(action_update_frame2, bg="#9DB0CF", pady=5)
    action_update_labelframe4.grid(column=0, row=1, pady=5)

    action_update_labelframe2 = LabelFrame(action_update_frame2, text="Contact Details", bg="#9DB0CF", pady=5)
    action_update_labelframe2.grid(column=0, row=2, pady=5)

    action_update_labelframe3 = LabelFrame(action_update_frame2, text="Address", bg="#9DB0CF", pady=5)
    action_update_labelframe3.grid(column=0, row=3, pady=5)

    action_update_frame3 = Frame(action_update_frame2, bg="#9DB0CF", pady=11)
    action_update_frame3.grid(column=0, row=4)

    # Group List

    groups = ["Family", "Friends", "Neighbours", "Work", "Other", "Archived", ]

    select_family = cursor.execute("SELECT fullname FROM contacts WHERE grouped=(?) ORDER BY fullname ASC;",
                                   ("Family",))
    family_list = []

    for i in select_family:
        family_list.append(i[-1])

    select_friends = cursor.execute("SELECT fullname FROM contacts WHERE grouped=(?) ORDER BY fullname ASC;",
                                    ("Friends",))
    friends_list = []

    for i in select_friends:
        friends_list.append(i[-1])

    select_neighbours = cursor.execute("SELECT fullname FROM contacts WHERE grouped=(?) ORDER BY fullname ASC;",
                                       ("Neighbours",))
    neighbours_list = []

    for i in select_neighbours:
        neighbours_list.append(i[-1])

    select_work = cursor.execute("SELECT fullname FROM contacts WHERE grouped=(?) ORDER BY fullname ASC;", ("Work",))
    work_list = []

    for i in select_work:
        work_list.append(i[-1])

    select_other = cursor.execute("SELECT fullname FROM contacts WHERE grouped=(?) ORDER BY fullname ASC;", ("Other",))
    other_list = []

    for i in select_other:
        other_list.append(i[-1])

    select_archive = cursor.execute("SELECT fullname FROM contacts WHERE grouped=(?) ORDER BY fullname ASC;",
                                    ("Archived",))
    archive_list = []

    for i in select_archive:
        archive_list.append(i[-1])

    def group_list(e):
        if entry1.get() == "Family":
            entry2.config(value=family_list)
        if entry1.get() == "Friends":
            entry2.config(value=friends_list)
        if entry1.get() == "Neighbours":
            entry2.config(value=neighbours_list)
        if entry1.get() == "Work":
            entry2.config(value=work_list)
        if entry1.get() == "Other":
            entry2.config(value=other_list)
        if entry1.get() == "Archived":
            entry2.config(value=archive_list)

    # Entrybox - Group

    Label1 = Label(action_update_labelframe1, text="Group:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label1.grid(column=0, row=0)
    entry1 = ttk.Combobox(action_update_labelframe1, value=groups, width=44)
    entry1.grid(column=1, row=0, padx=20, pady=5)
    entry1.bind("<<ComboboxSelected>>", group_list, )

    # Entrybox - Contact

    Label2 = Label(action_update_labelframe1, text="Contact:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label2.grid(column=0, row=1)
    entry2 = ttk.Combobox(action_update_labelframe1, value=[""], width=44)
    entry2.grid(column=1, row=1, padx=20, pady=5)

    # Field - First Name

    Label3 = Label(action_update_labelframe2, text="First Name:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label3.grid(column=0, row=4)
    field1 = Entry(action_update_labelframe2, font="Arial 10", width=40)
    field1.grid(column=1, row=4, padx=20, pady=5)

    # Field - Last Name

    Label4 = Label(action_update_labelframe2, text="Last Name:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label4.grid(column=0, row=5)
    field2 = Entry(action_update_labelframe2, font="Arial 10", width=40)
    field2.grid(column=1, row=5, padx=20, pady=5)

    # Field - Number

    Label6 = Label(action_update_labelframe2, text="Number:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label6.grid(column=0, row=7)
    field4 = Entry(action_update_labelframe2, font="Arial 10", width=40)
    field4.grid(column=1, row=7, padx=20, pady=5)

    # Field - Mailbox

    Label7 = Label(action_update_labelframe2, text="Mailbox:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label7.grid(column=0, row=8)
    field5 = Entry(action_update_labelframe2, font="Arial 10", width=40)
    field5.grid(column=1, row=8, padx=20, pady=5)

    # Field - Birthday

    Label8 = Label(action_update_labelframe2, text="Birthday:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label8.grid(column=0, row=9)
    field6 = Entry(action_update_labelframe2, font="Arial 10", width=40)
    field6.grid(column=1, row=9, padx=20, pady=5)

    # Field - Street

    Label9 = Label(action_update_labelframe3, text="Street:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label9.grid(column=0, row=8)
    field7 = Entry(action_update_labelframe3, font="Arial 10", width=40)
    field7.grid(column=1, row=8, padx=20, pady=5)

    # Field - City/Town

    Label10 = Label(action_update_labelframe3, text="City/Town:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label10.grid(column=0, row=9)
    field8 = Entry(action_update_labelframe3, font="Arial 10", width=40)
    field8.grid(column=1, row=9, padx=20, pady=5)

    # Field - Postcode

    Label11 = Label(action_update_labelframe3, text="Postcode:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label11.grid(column=0, row=10)
    field9 = Entry(action_update_labelframe3, font="Arial 10", width=40)
    field9.grid(column=1, row=10, padx=20, pady=5)

    # Field - Group

    Label12 = Label(action_update_labelframe3, text="Group:", font="Arial 10", width=15, anchor="e", bg="#9DB0CF")
    Label12.grid(column=0, row=11)
    field10 = ttk.Combobox(action_update_labelframe3, value=groups, width=44)
    field10.grid(column=1, row=11, padx=20, pady=5)

    # Entrybox - Group

    def search():
        find = cursor.execute("select * from contacts where fullname=(?);", (entry2.get(),))
        records = find.fetchall()
        for i in records:
            field1.delete(0, END)
            field2.delete(0, END)
            field4.delete(0, END)
            field5.delete(0, END)
            field6.delete(0, END)
            field7.delete(0, END)
            field8.delete(0, END)
            field9.delete(0, END)
            field10.delete(0, END)

            value1 = i[0]
            value2 = i[1]
            value4 = i[3]
            value5 = i[4]
            value6 = i[5]
            value7 = i[6]
            value8 = i[7]
            value9 = i[8]
            value10 = i[9]

            field1.insert(0, value1)
            field2.insert(0, value2)
            field4.insert(0, value4)
            field5.insert(0, value5)
            field6.insert(0, value6)
            field7.insert(0, value7)
            field8.insert(0, value8)
            field9.insert(0, value9)
            field10.insert(0, value10)

    def update():
        mb1 = messagebox.askyesno("Contacts - Update", f"Are you sure you want to update {field1.get()} {field2.get()}?")
        if mb1 == 1:
            cursor.execute("DELETE FROM contacts WHERE fullname=(?);", (entry2.get(),))
            cursor.execute(f"INSERT INTO contacts values (?,?,?,?,?,?,?,?,?,?)", (
                field1.get(), field2.get(), f"{field1.get()} {field2.get()}", field4.get(), field5.get(), field6.get(),
                field7.get(), field8.get(), field9.get(), field10.get(),))
            connection.commit()
            messagebox.showinfo("Contacts - Update", f"Contact details for {field1.get()} {field2.get()} have now been updated!")
            entry1.delete(0, END)
            entry2.delete(0, END)
            field1.delete(0, END)
            field2.delete(0, END)
            field4.delete(0, END)
            field5.delete(0, END)
            field6.delete(0, END)
            field7.delete(0, END)
            field8.delete(0, END)
            field9.delete(0, END)
            field10.delete(0, END)

    def delete():
        mb1 = messagebox.askyesno("Contacts - Delete", f"Are you sure you want to delete {field1.get()} {field2.get()}?")
        if mb1 == 1:
            cursor.execute("DELETE FROM contacts WHERE first_name=(?) and last_name=(?) and grouped = (?);",
                           (field1.get(), field2.get(), field10.get(),))
            connection.commit()
            messagebox.showinfo("Contacts - Delete", f"{field1.get()} {field2.get()} has been deleted!")
            entry1.delete(0, END)
            entry2.delete(0, END)
            field1.delete(0, END)
            field2.delete(0, END)
            field4.delete(0, END)
            field5.delete(0, END)
            field6.delete(0, END)
            field7.delete(0, END)
            field8.delete(0, END)
            field9.delete(0, END)
            field10.delete(0, END)

    # Search Button

    BTN1_search = Button(action_update_labelframe4, text="Search", command=search, height=2, width=16, activebackground="#336d96", activeforeground="#FFFFFF")
    BTN1_search.grid(column=0, row=0, padx=10)
    BTN1_search.bind("<Enter>", on_enter)
    BTN1_search.bind("<Leave>", on_leave)

    # Update Button

    BTN2_update = Button(action_update_frame3, text="Update", command=update, height=2, width=16, activebackground="#336d96", activeforeground="#FFFFFF")
    BTN2_update.grid(column=1, row=0, padx=10)
    BTN2_update.bind("<Enter>", on_enter)
    BTN2_update.bind("<Leave>", on_leave)

    # Delete

    BTN3_delete = Button(action_update_frame3, text="Delete", command=delete, height=2, width=16, activebackground="#336d96", activeforeground="#FFFFFF")
    BTN3_delete.grid(column=2, row=0, padx=10)
    BTN3_delete.bind("<Enter>", on_enter)
    BTN3_delete.bind("<Leave>", on_leave)

    # Home Button

    BTN4_home = Button(action_update_frame3, text="Home", command=button_home, height=2, width=16, activebackground="#336d96", activeforeground="#FFFFFF")
    BTN4_home.grid(column=3, row=0, padx=10)
    BTN4_home.bind("<Enter>", on_enter)
    BTN4_home.bind("<Leave>", on_leave)

# Widgets

my_menu = Menu(root)
root.config(menu=my_menu)

# Menu Bar Options

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

action_menu = Menu(my_menu)
my_menu.add_cascade(label="Action", menu=action_menu)
action_menu.add_command(label="Add", command=menu_add)
action_menu.add_command(label="Modify", command=menu_modify)

frame1 = Frame(root, bg="#FFFFFF")

scrollbar = Scrollbar(frame1, orient=VERTICAL, )
tree = ttk.Treeview(frame1, selectmode=EXTENDED, yscrollcommand=scrollbar.set, height=15)
scrollbar.grid(row=0, column=1, sticky="ns")
scrollbar.config(command=tree.yview)

frame2 = Frame(root, bg="#FFFFFF")

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

action_add_frame1 = Frame(root, width=400, height=400, bg="#FFFFFF")
action_modify_frame1 = Frame(root, width=400, height=400, bg="#FFFFFF")


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
    tree.insert(parent="", index="end", iid=count, text="", values=(i[2], i[3], i[4], i[8], i[5],))
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
