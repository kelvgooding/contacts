import sqlite3
import os

user = os.getlogin()

connection = sqlite3.connect(fr"C:\Users\{user}\Dropbox\Programming\Databases\contacts.db")
cursor = connection.cursor()
print("Successfully Connected to SQLite3!\n")

cont = cursor.execute("SELECT * FROM contacts order by grouped ASC, first_name;")

for i in cont:
    print(f"Name: {i[0]} {i[1]}")
    print(f"Mobile: {i[3]}")
    print(f"Mailbox: {i[4]}")
    print(f"Postcode: {i[7]}")
    print(f"Group: {i[8]}")
    print()

total = cursor.execute("SELECT COUNT (*) FROM contacts;")
for i in total:
    print(f"Total: {i[0]} Contacts")

family = cursor.execute("SELECT COUNT (grouped) FROM contacts where grouped=(?)", ("Family",))
for i in family:
    print(f"Family: {i[0]} Contacts")

friends = cursor.execute("SELECT COUNT (grouped) FROM contacts where grouped=(?)", ("Friends",))
for i in friends:
    print(f"Friends: {i[0]} Contacts")

neighbours = cursor.execute("SELECT COUNT (grouped) FROM contacts where grouped=(?)", ("Neighbour",))
for i in neighbours:
    print(f"Neighbour: {i[0]} Contacts")

work = cursor.execute("SELECT COUNT (grouped) FROM contacts where grouped=(?)", ("Work",))
for i in work:
    print(f"Work: {i[0]} Contacts")

other = cursor.execute("SELECT COUNT (grouped) FROM contacts where grouped=(?)", ("Other",))
for i in other:
    print(f"Other: {i[0]} Contacts")

hidden = cursor.execute("SELECT COUNT (grouped) FROM contacts where grouped=(?)", ("Hidden",))
for i in hidden:
    print(f"Hidden: {i[0]} Contacts")










