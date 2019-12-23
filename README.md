# REST API using django and DRF for managing the users data

## User has the following attributes

* ID
* First Name
* Last Name
* Company Name
* Age
* City
* State
* Zip
* Email
* Web

## The application has the following endpoints

* /api/users – GET – To list the users<br>
  Also, supports some query parameters:-

- page – a number for pagination
- limit – no. of items to be returned, default limit is 5
- name – search user by name as a substring in First Name or Last Name (Note, use substring matching algorithm/pattern to match the name). It should be case-insensitive.
- Sort – name of attribute, the items to be sorted. By default it returns items in ascending order if this parameter exist, and if the value of parameter is prefixed with ‘-’ character, then it should return items in descending order
* /api/users – POST – To create a new user
* /api/users/{id} – GET – To get the details of a user with specific id
* /api/users/{id} – PUT – To update the details of a user
* /api/users/{id} – DELETE – To delete the user

## Software

Django 1.11.8

Python 3.6.3

Django Rest Framework 3.7.3

## Step by step guide to run this project

* Download and extract the zip file.
* Open this folder inside VScode
* Open terminal and setup virtual enviroment by following steps

              python -m venv myenv
              myenv\Scripts\activate
              
* Install django and djangorestframework by following command

              pip install django==1.11.8 djangorestframework==3.7.3
* Now run the following command to runserver

              python manage.py runserver
