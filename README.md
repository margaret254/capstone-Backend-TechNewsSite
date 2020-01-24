# TechNews Site/BackEd

#### This is the application backend part, where an API is created and consumed in the frontend part.
#### By **Margaret254**&trade;

## Description
This is an app where users are fed with daily news in the industry of tech.
## Project live site
  This is the live .[ Click for the link](https://maggie254hood.herokuapp.com/)
 

## Setup/Installation requirements
1.Clone or download and unzip the repository from github,https://github.com/margaret254/capstone-Backend-TechNewsSite.git
2. Activate virtual environment using python3.6 as default handler virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

3. Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt
4. Create the Database
- psql
- CREATE DATABASE capstone;

4. Create .env file and paste p the following filling where appropriate:

-SECRET_KEY = '<Secret_key>'
-DBNAME = '<DBNAME>'
-USER = '<Username>'
-PASSWORD = '<password>'
-DEBUG = True
5. Run initial Migration
-python3.6 manage.py makemigrations instagram
-python3.6 manage.py migrate
6. Run the app
-python3.6 manage.py runserver
-Open terminal on localhost:8000



## Technologies Used
* PYTHON 3.6
* DJANGO FRAMEWORK
* BOOTSTRAP
* CSS
* POSTGRES

## Prerequisite
* PYTHON 3.6
* DJANGO FRAMEWORK
* PYTHON VIRTULENV
* POSTGRESS
## Support and contact details
contact me @ maggiemwas91@gmail.com
### License
The project is under[MIT license](/blob/master/LICENSE)
Copyright &copy; 2019.All rigths reserved