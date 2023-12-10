# CONTACTS

## Description

Repository: https://github.com/kelvgooding/contacts

Contacts is a web app, which is used to store contact details of Family, Friends, Neighbours etc. The data is stored in an mysql database. This application has been dockerised, and the image can be used for this application.

## System Requirements

- Linux

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

## Dependencies

### Software:

- Python

### Modules:

- from flask import Flask, render_template, request
- from modules import db_check
- from modules import imp_exp
- import os

## Stakeholders

PM: Kelvin Gooding | kelv.gooding@outlook.com<br>
Design: Kelvin Gooding | kelv.gooding@outlook.com<br>
Dev: Kelvin Gooding | kelv.gooding@outlook.com<br>
QA: Kelvin Gooding | kelv.gooding@outlook.com<br>
Support: Kelvin Gooding | kelv.gooding@outlook.com

## Contribution

Issue Tracker: https://github.com/kelvgooding/contacts/issues<br>
Contact: Kelvin Gooding | kelv.gooding@outlook.com
