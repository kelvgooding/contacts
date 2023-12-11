# CONTACTS

## Description

Repository: https://github.com/kelvgooding/contacts

Contacts is a web app, which is used to store contact details of Family, Friends, Neighbours etc. The data is stored in an local SQLite3 database, which is created for the first time when the application is launched.

## OS Compatibility

- Linux
- Windows

## Dependencies

### Linux Packages

- python3
- python3-pip
- docker.io

### Python Modules

- from flask import Flask, render_template, request, flash
- from datetime import datetime
- from modules import db_check
- from modules import imp_exp
- from modules import dir_check
- import os

## Installation

To download this web application, run the following commands on your linux environment:

Downloading the repository from GitHub:
```
cd ~
git clone https://github.com/kelvgooding/contacts.git
```

Installating the requirements.txt file to ensure the correct packages are available and installed:

```
cd ~/contacts
pip3 install -r requirements.txt
```

Running the application:

```
cd ~/contacts
python3 ~/contacts/app.py >> ~/app_contacts_`date +\%Y\%m\%d`.log 2>&1 &
```

The log file will contain the URL for the application, along with each request that is made.

## Stakeholders

PM: Kelvin Gooding | kelv.gooding@outlook.com<br>
Design: Kelvin Gooding | kelv.gooding@outlook.com<br>
Dev: Kelvin Gooding | kelv.gooding@outlook.com<br>
QA: Kelvin Gooding | kelv.gooding@outlook.com<br>
Support: Kelvin Gooding | kelv.gooding@outlook.com

## Contribution

Issue Tracker: https://github.com/kelvgooding/contacts/issues<br>
Contact: Kelvin Gooding | kelv.gooding@outlook.com
