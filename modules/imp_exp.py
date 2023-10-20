"""
Author: Kelvin Gooding
Created: 2023-08-08
Updated: 2023-10-14
Version: 1.1
"""

#!/usr/bin/env python3

# Modules

import mysql.connector
import csv
from datetime import datetime
import os
import platform
from . import auth

# Variables

username = os.environ.get('USER')
exp_filename = f'contacts_export_{datetime.today().strftime("%Y%m%d_%H%M%S")}.csv'
imp_filename = 'contacts_import.csv'

# MySQL Variables

conn = mysql.connector.connect(
    host=auth.mysql_db_auth["host"],
    user=auth.mysql_db_auth["user"],
    password=auth.mysql_db_auth["password"],
    database=auth.mysql_db_auth["database"],
    port=auth.mysql_db_auth["port"]
)

c = conn.cursor()

def export_data():

    # Headers should reflect the column names in the contacts table.

    headings = ['First Name', 'Last Name', 'Contact Number', 'Mailbox', 'Address', 'City/Town', 'Postcode', 'Birthday', 'Gender', 'Group', 'Added On']
    
    # Select all data from the contacts table.
    
    c.execute('SELECT * FROM contacts ORDER BY first_name ASC;')
    contacts_data = c.fetchall()

    if platform.system() == 'Windows':
        file = open(f'export/{exp_filename}', 'w', newline="")
    elif platform.system() == 'Linux':
        file = open(f'/home/{username}/apps/contacts/export/{exp_filename}', 'w', newline="")

    writer = csv.writer(file)
    writer.writerow(headings)
    writer.writerows(contacts_data)
    file.close()

def import_data():

    # Select all data from the contacts table.

    if platform.system() == 'Windows':
        with open(f'import\{imp_filename}') as file:
            reader_obj = csv.reader(file)
            next(reader_obj)
            for row in reader_obj:
                c.execute(f'INSERT INTO contacts VALUES ("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}", "{row[9]}", CURRENT_TIMESTAMP)')
                conn.commit()
        os.remove(f'import\{imp_filename}')
    elif platform.system() == 'Linux':
        with open(f'/home/{username}/apps/contacts/import/{imp_filename}') as file:
            reader_obj = csv.reader(file)
            next(reader_obj)
            for row in reader_obj:
                c.execute(f'INSERT INTO contacts VALUES ("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}", "{row[9]}", CURRENT_TIMESTAMP)')
                conn.commit()
        os.remove(f'/home/{username}/apps/contacts/import/{imp_filename}')