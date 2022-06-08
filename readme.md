
# Library Management System using Django

This repository contains a project in Python Django framework implemented in MVT i.e. Model View Template aritectural pattern, as followed in Django projects.

## Prerequisites

docker-compose >= 3.8

## Environment

Before starting the containers add the following key value pairs for database credentials

MYSQL_DATABASE=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_ROOT_PASSWORD=
MYSQL_DATABASE_HOST=
MYSQL_DATABASE_PORT=3306

## Usage

docker-compose build
docker-compose up

## Process Flow when app starts

### Database

1. Builds MySQL database image from mysql/mysql-server:8.0
2. Database gets initialised via a shell script creating the root user and database as mentioned in .env file

### Backend

1. Builds the image with required dependencies 
2. Copies the project folder to /usr/src/app/
3. Installs the python packages as mentioned in requirements.txt
4. Copies the 'entrypoint.sh' executable file that applies database migrations, seeds data to the database which has the superuser created and then starts the development server.


## APPLICATION DOCS

### Overview

- A library management system using Django where an admin can
perform CRUD ( create, read, update and delete) operations like adding a book, viewing all books, updating a book and deleting a book.

- A non admin user can only view the books and only perform GET operations only

- Sign-in can only be performed with email-ID and password as the authentication backend has been modified

### Details

Admin-login - The Admin can log in based on email and password

Create an entry for books - Once the admin is signed in she can perform this operation by clicking on 'Add book' button

Retrieve all the books - All users can see list of the books registered in the system

Update a book - Once the admin is signed in she can perform this operation by clicking on a book from the book list view and change its properties

Delete a book - Once the admin is signed in she can perform this operation by clicking on a book from the book list view and delete it

### Admin Credentials

Email - admin@django.com
Password - password

### Database

Database - MySQL Server 8.0
Driver - django.db.backends.mysql


### Screenshots

1. Site landing page
![Site landing page](https://github.com/swapnilj01/LMS-Django/blob/main/screenshots/1.png?raw=true)


2. Books list view
![Books list view](https://github.com/swapnilj01/LMS-Django/blob/main/screenshots/2.png?raw=true)


3. Login Page
![Login Page](https://github.com/swapnilj01/LMS-Django/blob/main/screenshots/3.png?raw=true)


4. Landing page if Admin logs in
![Landing page if Admin logs in](https://github.com/swapnilj01/LMS-Django/blob/main/screenshots/4.png?raw=true)


5. Adding a book
![Adding a book](https://github.com/swapnilj01/LMS-Django/blob/main/screenshots/5.png?raw=true)


6. Adding a student
![Adding a student](https://github.com/swapnilj01/LMS-Django/blob/main/screenshots/6.png?raw=true)