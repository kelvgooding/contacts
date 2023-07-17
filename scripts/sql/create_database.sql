/* create database */

CREATE DATABASE contacts;

/* switch to database */

USE contacts;

/* create database table */

CREATE TABLE contacts (
first_name VARCHAR(255),
last_name VARCHAR(255),
number VARCHAR(15),
mailbox VARCHAR(255),
address VARCHAR(255),
town VARCHAR(255),
postcode VARCHAR(10),
birthday VARCHAR(10),
gender VARCHAR(1),
grp VARCHAR(255) 
);

/* view table columns */

SHOW COLUMNS FROM contacts;

/* view table data */

SELECT * FROM contacts;