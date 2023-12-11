#!/usr/bin/python3

"""
Author: Kelv Gooding
Created: 2023-08-08
Updated: 2023-12-10
Version: 1.2.1
"""

# Modules

import sqlite3
import csv
import os
import platform
import glob

# Variables

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Script

def export_data(headings, table_name, db_filename, exp_filename):

    conn = sqlite3.connect(os.path.join(base_path, db_filename), check_same_thread=False)
    c = conn.cursor()

    # Select all data from the contacts table.
    
    c.execute(f'SELECT * FROM {table_name} ORDER BY first_name ASC;')
    contacts_data = c.fetchall()

    # Write db data to .csv file

    file = open(f'{base_path}/export/{exp_filename}', 'w', newline="")
    writer = csv.writer(file)
    writer.writerow(headings)
    writer.writerows(contacts_data)
    file.close()

def import_data(db_filename):

    conn = sqlite3.connect(os.path.join(base_path, db_filename), check_same_thread=False)
    c = conn.cursor()

    # Select all data from the contacts table.

    imp_filename = glob.glob(f"{base_path}/import/*.csv")
    with open(imp_filename) as file:
        reader_obj = csv.reader(file)
        next(reader_obj)
        for row in reader_obj:
            c.execute(f'INSERT INTO contacts VALUES ("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}", "{row[9]}", CURRENT_TIMESTAMP)')
            conn.commit()
    os.remove(imp_filename)
