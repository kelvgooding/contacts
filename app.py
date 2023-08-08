"""
Author: Kelvin Gooding
Created: 2022-06-29
Updated: 2023-08-08
Version: 1.2
"""

#!/usr/bin/env python3

# Modules

from flask import Flask, render_template, request
import mysql.connector

# Custom Modules

import auth
import imp_exp

# MySQL Variables

conn = mysql.connector.connect(
    host=auth.mysql_db_auth["host"],
    user=auth.mysql_db_auth["user"],
    password=auth.mysql_db_auth["password"],
    database=auth.mysql_db_auth["database"],
    port=auth.mysql_db_auth["port"]
)

c = conn.cursor()

# Flask Variables

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():

    # Headers should reflect the column names in the contacts table.

    headings = ['First Name', 'Last Name', 'Contact Number', 'Mailbox', 'Address', 'City/Town', 'Postcode', 'Birthday', 'Gender', 'Group', 'Added On']
    
    # Select all data from the contacts table.
    
    c.execute('SELECT * FROM contacts WHERE GRP NOT LIKE "ARCHIVED" ORDER BY FIRST_NAME ASC')
    contacts_data = c.fetchall()

    # Select all data from the contact table using the filter dropdown value in the WHERE statement.

    if request.method == "POST":
        c.execute(f'SELECT * FROM contacts WHERE GRP=("{(request.form.get("dropdownbox"))}") ORDER BY FIRST_NAME ASC;')
        contacts_data = c.fetchall()
        return render_template('index.html', headings=headings, contacts_data=contacts_data)

    return render_template('index.html', headings=headings, contacts_data=contacts_data)


@app.route("/new_contact", methods=["POST", "GET"])
def new_contact():

    # Values will be taken from each input box and pushed into the contacts table.

    if request.method == "POST":
        c.execute(f"INSERT INTO contacts VALUES ('{request.form.get('first_name')}', '{request.form.get('last_name')}', '{request.form.get('area_code')} {request.form.get('number')}', '{request.form.get('mailbox')}', '{request.form.get('address')}', '{request.form.get('town')}', '{request.form.get('postcode')}', '{request.form.get('birthday')}', '{request.form.get('gender')}', '{request.form.get('group')}', CURRENT_TIMESTAMP)")
        conn.commit()

    return render_template('new_contact.html')

@app.route("/delete_contact", methods=["POST", "GET"])
def delete_contact():

    # Select all data from the contacts table.

    c.execute('SELECT FIRST_NAME, LAST_NAME FROM contacts ORDER BY FIRST_NAME ASC;')
    all_contacts = c.fetchall()

    # The value will be taken from the contacts table in the first name column and delete the row.

    if request.method == "POST":
        c.execute(f'DELETE FROM contacts WHERE FIRST_NAME=("{(request.form.get("dropdownbox"))}")')
        conn.commit()

    return render_template('delete_contact.html', all_contacts=all_contacts)

@app.route("/import_export", methods=["POST", "GET"])
def import_export():
        
    if 'export_btn' in request.form and request.method == "POST":
        imp_exp.export_data()

    if 'import_btn' in request.form and request.method == "POST":
        imp_exp.import_data()

    return render_template('import_export.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=3003)
