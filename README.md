# login-app
this app use Flask , Flask_bootstrap, flask_wtf to make alog in service

## Introduction
This is a python module that uses information of users in  userData:



### Functions in tray.py:
* **login():** Connects to the login page identfay user using database and compare hashed password .
* **logout():** redirect to the index page and log the user out.
* **signup():** create new user in the database.
* **dashboard():** the secure page user hae to be loggedin to access.

## Instructions
* To run this module succesfully make sure that you install:

*[python](https://www.python.org/downloads/)

*[flask_bootstrap](https://pythonhosted.org/Flask-Bootstrap/)

*[Postgresql](https://www.postgresql.org/download/)

*[newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

* or use 'pip install --user (liberary name )'
*in shell comand
## Recommended setup
* Install [vagrant](https://www.vagrantup.com/downloads.html) and [virtualbox](https://www.virtualbox.org/wiki/Downloads) 
* Clone the repository to your local machine:
  git clone [https://github.com/ebishbishy10/log-_analysis-udacity-project.git]
* Start the virtual machine
  From your terminal, inside the project directory, run the command `vagrant up`. This will cause Vagrant to download the Linux           operating   system and install it.
  When vagrant up is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your     newly installed Linux VM!
       directory, which is shared with your virtual machine.
* Setup Database
  To setup the database use the following command:
  `python database_setup.py;`
* Run Module
  `python tray.py`
