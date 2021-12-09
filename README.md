# Contacts

Contacts is an application which is used to store contact details of Family, Friends, Neighbours etc. This data is stored in an SQLite3 database, which is then called when clicking on one of the filter buttons at the bottom of the application.

The contact information shown in the examples below is not real data.

## Application Overview

This is the main any only window for Contacts. This consists of a treeview table, with five columns named: Name, Mobile, Mailbox, Postcode and Birthday. 

* The Name column combines the forename and surname of an indivudal.
* The Mobile column stores the indivual's contact number - using the area code at the start, and is split into sections for ease of reading.
* The Mailbox column stores the email address for the individual.
* The Postcode column will store the Postcode for the individual.
* The Birthday column will store the Birthday for the individual. This is in a format of DD/MM, excluding the year.

By default, when the application is launched, this will show all contacts in the database. Each button is a filter, and this will change what is viewed in the treeview table, depending on what group was entertered for the individual.

The buttons will change colour when the mouse is hovered over this. This feature was added to make it easier for the user to identify which filter button is about to be clicked.

![Screenshot 2021-12-08 16 43 17](https://user-images.githubusercontent.com/82043281/145309431-7f9469d0-8142-4805-bb6d-04c99e0fb547.png)

## Unfiltered - All

This filter will show all contacts stored in the contacts database.

![Screenshot 2021-12-08 16 43 21](https://user-images.githubusercontent.com/82043281/145309432-59c94114-7a1a-4834-adfe-5d3718c9f5d9.png)

## Filtered - Family

This filter will show contacts stored in the contacts database in the group Family.

![Screenshot 2021-12-08 16 43 25](https://user-images.githubusercontent.com/82043281/145309433-516e0074-f9fd-4ad2-aadc-0202f0a3b8f6.png)

## Filtered - Friends

This filter will show contacts stored in the contacts database in the group Friends.

![Screenshot 2021-12-08 16 43 29](https://user-images.githubusercontent.com/82043281/145309434-e2a36e5f-f98e-4b94-aaaa-aab41db73272.png)

## Filtered - Neighbours

This filter will show contacts stored in the contacts database in the group Neighbours.

![Screenshot 2021-12-08 16 43 32](https://user-images.githubusercontent.com/82043281/145309436-b2f65295-74e1-4638-b4c5-7cfdf3c9e4e7.png)

## Filtered - Work

This filter will show contacts stored in the contacts database in the group Work.

![Screenshot 2021-12-08 16 43 35](https://user-images.githubusercontent.com/82043281/145309438-bb5bf68a-19a4-4240-a6c3-b826d106a992.png)

## Filtered - Other

This filter will show contacts stored in the contacts database in the group Other.

![Screenshot 2021-12-08 16 43 40](https://user-images.githubusercontent.com/82043281/145309439-9eb035ef-4161-4e8b-babe-e0581f9a24af.png)

## Filtered - Archived

This filter will show contacts stored in the contacts database in the group Archived. This is aimed to store contacts which are no longer used.

![Screenshot 2021-12-08 16 43 43](https://user-images.githubusercontent.com/82043281/145309441-b3ce7c53-7336-45a3-aa43-faed6606727e.png)
