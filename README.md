# Django REST Framework API

The following project was to develop a REST API with Django REST Framework.

## Required Functionalities
* The required functionalities include being registering and logging in of users with JWT Authentication.
* The user must be able to see all of thier booked advisors. *[ A GET request]*
* New appointments can be booked with an advisor by providing a specified time. *[ POST request ]*
* Separate endpoint exists for the Admin to add new Advisors to the Database.
### Note: An in-depth potrayal of the requirements can be found [here](https://docs.google.com/document/d/1R7OkSB82mnuwW3GonKSZdaiW2nSyeSO8UmcM9nJD-ik/edit?usp=sharing)

## API Endpoints

Note: The API is deployed to heroku and the base url is [https://haany-advisor-api.herokuapp.com/](https://haany-advisor-api.herokuapp.com/).
1.  /admin/advisor/ -- POST
2.  /user/register/  -- POST
3.  /user/login/ -- POST
4.  /user/\<user-id\>/advisor/booking/ -- GET
5.  /user/\<user-id\>/advisor/<advisor-id>/ -- POST
6.  /user/\<user-id\>/advisor/ -- GET

  * For better understanding of the endpoints and their working please refer to this [document](https://docs.google.com/document/d/1R7OkSB82mnuwW3GonKSZdaiW2nSyeSO8UmcM9nJD-ik/edit?usp=sharing)

## Steps to Run
* Change directory to the Project Root Folder
`cd advisor_api`
* Run the following commands one by one
``` 
>>> python manage.py makemigrations
>>> python manage.py migrate
>>> python managage.py runserver
```
