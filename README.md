# [MY-TIE.CLUB](http://www.my-tie.club)

E-Commerce web-application with full CRUD functionality. Back-End was made using Python-
Flask, PostgreSQL/SQLAlchemy; Front-End - HTML, CSS, Bootstrap, Jinja2, Javascript. 
Users are able to View products, Register Account, Login, Shop by categories and by sizes, Create orders, View/Edit/Delete previous orders; Additionally Admin role has ability to Add/Update/Delete Products, See all orders, Manage Users through custom made Admin Panel etc.

![](http://artem-yerep.com/static/img/mytieclub-n.gif)

### Installation

As regular Flask app using PipEnv or Venv 

All dependencies are in pipfile or 
```
pipenv install -r requirements.txt
```

Database location in config.py pointed to .env file 


To create db run in python shell :
    
```
from app import db
db.create_all()
```
