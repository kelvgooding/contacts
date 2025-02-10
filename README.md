# CONTACTS

## Description

Repository: https://github.com/kelvgooding/contacts

Contacts is a web app, which is used to store contact details of Family, Friends, Neighbours etc. The data is stored in an local SQLite3 database, which is created for the first time when the application is launched.

## Running app using Docker

Clone the repository:

```
git@github.com:kelvgooding/contacts.git
```

Navigate to the cloned repository directory

Run the following command to build the Docker image

```
sudo docker build -t contacts .
```

Run the following command to create and start the container:

```
sudo docker run -itd -p 3003:3003 -v /mnt/volumes/contacts:/data --name contacts contacts
```

This can now be accessed via web browser - http://localhost:3003