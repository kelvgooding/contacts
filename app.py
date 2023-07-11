#!/usr/bin/env python3

from flask import Flask, render_template, request, flash
import sqlite3

# Flask Variables

app = Flask(__name__)

# Sqlite3 Variables

connection = sqlite3.connect("contacts.db", check_same_thread=False)
cursor = connection.cursor()

@app.route("/", methods=["POST", "GET"])
def index():

    # Headers should reflect the column names in the contacts table.

    headings = ['First Name', 'Last Name', 'Contact Number', 'Mailbox', 'Address', 'City/Town', 'Postcode', 'Birthday', 'Gender', 'Group']
    
    # Select all data from the contacts table.
    
    cursor.execute('SELECT * FROM CONTACTS WHERE GRP NOT LIKE "ARCHIVED" ORDER BY FIRST_NAME ASC')
    contacts_data = cursor.fetchall()

    # Select all data from the contact table using the filter dropdown value in the WHERE statement.

    if request.method == "POST":
        cursor.execute('SELECT * FROM CONTACTS WHERE GRP=(?) ORDER BY FIRST_NAME ASC', (request.form.get('dropdownbox'),))
        contacts_data = cursor.fetchall()
        return render_template('index.html', headings=headings, contacts_data=contacts_data)

    return render_template('index.html', headings=headings, contacts_data=contacts_data)

@app.route("/new_contact", methods=["POST", "GET"])
def new_contact():

    # Values will be taken from each input box and pushed into the contacts table.

    if request.method == "POST":
        cursor.execute(f"INSERT INTO contacts VALUES ('{request.form.get('first_name')}', '{request.form.get('last_name')}', '{request.form.get('number')}', '{request.form.get('mailbox')}', '{request.form.get('address')}', '{request.form.get('town')}', '{request.form.get('postcode')}', '{request.form.get('birthday')}', '{request.form.get('gender')}', '{request.form.get('group')}')")
        connection.commit()

    return render_template('new_contact.html')

@app.route("/delete_contact", methods=["POST", "GET"])
def delete_contact():

    # Select all data from the contacts table.

    cursor.execute('SELECT FIRST_NAME, LAST_NAME FROM CONTACTS ORDER BY FIRST_NAME ASC;')
    all_contacts = cursor.fetchall()

    # The value will be taken from the contacts table in the first name column and delete the row.

    if request.method == "POST":
        cursor.execute(f"DELETE FROM CONTACTS WHERE FIRST_NAME=(?)", (request.form.get('dropdownbox'),))
        connection.commit()

    return render_template('delete_contact.html', all_contacts=all_contacts)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=3010)
