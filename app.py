#!/usr/bin/python3

"""
Author: Kelv Gooding
Created: 2022-06-29
Updated: 2024-10-03
Version: 2.1
"""

# Modules

from flask import Flask, render_template, request, flash
from modules import db_check
from modules import import_data
from modules import export_data
from modules import dir_check
import os

# General Variables

base_path = os.path.dirname(os.path.abspath(__file__))
print(base_path)
app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
print(app_name)
db_filename = 'contacts.db'
print(db_filename)
sql_script = os.path.join(base_path, 'scripts/sql/create_tables.sql')
print(sql_script)

# SQLite3 Variables

db_check.check_db(base_path, f'{db_filename}', f'{sql_script}')
conn = db_check.sqlite3.connect(os.path.join(base_path, db_filename), check_same_thread=False)
c = conn.cursor()

# Flask Variables

app = Flask(__name__)
app.secret_key = os.urandom(32)

# Generate import and export directories

dir_check.check_dir(base_path, 'export')
dir_check.check_dir(base_path, 'import')

# Script

@app.route("/", methods=["POST", "GET"])
def index():

    # Headers should reflect the column names in the contacts table.

    headings = ['First Name', 'Last Name', 'Contact Number', 'Mailbox', 'Address', 'City/Town', 'Postcode', 'Birthday', 'Gender', 'Group', 'Added On']

    # Select all data from the contacts table.

    c.execute('SELECT * FROM contacts WHERE GRP NOT LIKE "ARCHIVED" ORDER BY FIRST_NAME ASC')
    contacts_data = c.fetchall()

    c.execute('SELECT COUNT(*) FROM contacts WHERE GRP NOT LIKE "ARCHIVED" ORDER BY FIRST_NAME ASC')
    contacts_count = c.fetchall()

    # Select all data from the contact table using the filter dropdown value in the WHERE statement.

    if request.method == "POST":
        c.execute(f'SELECT * FROM contacts WHERE GRP=("{(request.form.get("dropdownbox"))}") ORDER BY FIRST_NAME ASC;')
        contacts_data = c.fetchall()
        c.execute(f'SELECT COUNT(*) FROM contacts WHERE GRP=("{(request.form.get("dropdownbox"))}") ORDER BY FIRST_NAME ASC;')
        contacts_count = c.fetchall()
        return render_template('index.html', headings=headings, contacts_data=contacts_data, contacts_count=contacts_count)

    return render_template('index.html', headings=headings, contacts_data=contacts_data, contacts_count=contacts_count)

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
        export_data.export_data('./', 'export', 'contacts.db', 'contacts')
        flash('Export has been completed successfully!')

    if 'import_btn' in request.form and request.method == "POST":
        import_file = (os.popen('ls -t import | head -n1').read().strip())
        import_data.import_data(f'contacts.db', os.path.join('import/', str(import_file)), './', f'sql/create_tables.sql', 'contacts')
        flash('Import has been completed successfully!')

    return render_template('import_export.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=3003)
