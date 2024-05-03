#!/usr/bin/python3

"""
Author: Kelv Gooding
Created: 2023-10-25
Updated: 2024-05-03
Version: 1.1
"""

# Modules

import sqlite3
import csv
from datetime import datetime
import os

# Script

def export_data(base_path, export_path, db_filename, db_table_name):

    # sqlite3 connection

    conn = sqlite3.connect(os.path.join(base_path, db_filename))
    c = conn.cursor()

   # obtain data from database

    c.execute(f"SELECT name FROM pragma_table_info('{db_filename}')")
    heading = c.fetchall()

    # obtain header from database

    c.execute(f'SELECT * FROM {db_table_name}')
    data = c.fetchall()

    # export header and data into .csv file

    export_filename = f'export_{datetime.today().strftime("%Y%m%d")}.csv'
    file = open(f'{os.path.join(export_path, export_filename)}', 'w', newline="")
    writer = csv.writer(file)
    writer.writerow(heading)
    writer.writerows(data)
    file.close()