# CONTACTS

## Description
Repository: https://github.com/kelvgooding/contacts

Contacts is a web app, which is used to store contact details of Family, Friends, Neighbours etc. The data is stored in an mysql database. This application has been dockerised, and the image can be used for this application.

## Prerequisites
### System Requirements
•	Linux
<br>

### auth.py
This application requires user credentials. This file is representative of any personal details which you would like to keep private.<br>
Within the main script, auth.py will be referenced, and the variables will be found in this file.
The auth.py file will be left blank by default. Therefore, this information must be entered before using this application.<br>

### Database Credentials

```
mysql_db_auth = {
    "user": "",
    "password": "",
    "host": "",
    "port": "",
    "database": "",
}
```

### Dependencies
#### Software:
•	Python

#### Files:
•	auth.py
<br>
•	imp_exp.py

#### Modules:
•	from flask import Flask, render_template, request
<br>
•	mysql.connector
<br>
•	auth
<br>
•	imp_exp

## Stakeholders
PM: Kelvin Gooding | kelv.gooding@outlook.com
<br>
Design: Kelvin Gooding | kelv.gooding@outlook.com
<br>
Dev: Kelvin Gooding | kelv.gooding@outlook.com
<br>
QA: Kelvin Gooding | kelv.gooding@outlook.com
<br>
Support: Kelvin Gooding | kelv.gooding@outlook.com

## Contribution
Issue Tracker: https://github.com/kelvgooding/contacts/issues
<br>
Contact: Kelvin Gooding | kelv.gooding@outlook.com
