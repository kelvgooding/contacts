#!/usr/bin/python3

"""
Author: Kelv Gooding
Created: 2024-05-03
Updated: 2024-05-03
Version: 1.0
"""

# Modules

import os
import sqlite3
import csv
from modules import db_check

# Script

def import_data(db_filename, csv_filename, base_path, sql_filename, table_name):

    # check if db exists

    db_check.check_db(base_path, db_filename, sql_filename)

    # sqlite3 connection

    conn = sqlite3.connect(f'{os.path.join(base_path, db_filename)}')
    c = conn.cursor()

    # import data to db

    with open(f'{csv_filename}', 'r', encoding='unicode_escape') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            num_columns = len(row)
            placeholders = ', '.join(['?'] * num_columns)
            query = f'INSERT INTO {table_name} VALUES ({placeholders})'
            c.execute(query, row)
            conn.commit()
        os.remove(csv_filename)