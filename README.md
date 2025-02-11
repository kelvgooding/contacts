# CONTACTS

## Description

Contacts is a web app, which is used to store contact details of Family, Friends, Neighbours etc. The data is stored in an local SQLite3 database, which is created for the first time when the application is launched.

## Running app using Docker

Clone the repository:

```
mkdir ~/repos
cd ~/repos
git@github.com:kelvgooding/contacts.git
```

Run the following command to build the Docker image

```
sudo docker build -t contacts .
```

Run the following start a container:

```
sudo docker run -itd -p 3003:3003 -v /mnt/usb/volumes/contacts:/data --name contacts contacts
```

This should now be accessible via a web browser - ```http://localhost:3003```
