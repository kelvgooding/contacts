# CONTACTS

## Description

Repository: https://github.com/kelvgooding/contacts

Contacts is a web app, which is used to store contact details of Family, Friends, Neighbours etc. The data is stored in an local SQLite3 database, which is created for the first time when the application is launched.

## Setup

Update Linux OS and ensure the Docker package is installed:

```
sudo apt update -y
sudo install docker
```

Clone the repo from GitHub:

```
mkdir ~/apps
cd ~/apps
git clone git@github.com:kelvgooding/contacts.git
```

To create the Docker image and run the container, run the following command:

```
cd ~/apps/contacts
docker-compose -f docker-compose.yml up -d
```

Any files which are required to be peristent, such as sqlite3 database files are kept in:

```
/var/lib/docker/volumes
```

## Contribution

| Role      | Name            | Email                        |
|-----------|-----------------|------------------------------|
| Design    | Kelvin Gooding  | kelv.gooding@outlook.com     |
| Developer | Kelvin Gooding  | kelv.gooding@outlook.com     |
| Support   | Kelvin Gooding  | kelv.gooding@outlook.com     |
