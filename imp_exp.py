"""
Author: Kelvin Gooding
Created: 2023-08-08
Updated: 2023-08-08
Version: 1.0
"""

#!/usr/bin/env python3

# Modules

import mysql.connector
import csv
from datetime import datetime

# Custom Modules

import auth

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

    file = open(f'export/contacts_export_{datetime.today().strftime("%Y%m%d_%H%M%S")}.csv', 'w', newline="")
    writer = csv.writer(file)
    writer.writerow(headings)
    writer.writerows(contacts_data)
    file.close()

def import_data():

    # Select all data from the contacts table.
    
    with open('import/contacts_import.csv') as file:

        reader_obj = csv.reader(file)

        next(reader_obj)

        for row in reader_obj:
            c.execute(f'INSERT INTO contacts VALUES ("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}", "{row[9]}", CURRENT_TIMESTAMP)')
            conn.commit()
