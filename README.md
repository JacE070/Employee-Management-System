# Employee Management System
## Description
Employee management system is a Python software. Tkinter API is used for GUI and mysql.connector API is used for connection to MySQL database and command executions. This project uses pipenv to create virtual development environment.

## Features
It provides functions to store, update, and delete employee records in the local MySQL database. 
- Add, update, and delete employee records to local MySQL database
### To Do:
- Optimize UI
- Have a function to store  configuration file in local directory
- Transplant to Website, allowing users to use remote database provided

## Technology:
Project is built with:
- Python version: 3.9.12
- MySQL version: 8.0.29
- mysql-connector-python version: 8.0.30
- pipenv version: 2022.7.4
## Installation
### Attention
This project assumes that you have installed MySQL locally. If you don't, go to [HERE](https://dev.mysql.com/downloads/windows/installer/8.0.html) to download the MySQL installer.
### Clone the project
```
git clone https://github.com/JacE070/Employee-Management-System.git
cd Employee-Management-System
```
### Install Pipenv
```
pip install pipenv
```
### Install dependencies & activate virtualenv
```
pipenv shell # Activate virtualenv
pipenv install mysql-connector-python
```
### Configure and initialize MySQL database connection and creation
In these two lines, replace counterpart parameters with your MySQL connection setting.
```
mysqlConnector = mysql.connector.connect(
    host="localhost", user="root", password="pwd")
```
### Running
Simply run this command.
```
python main.py
```
## Sources
This software is inspired by and developed on the existed shell version by [Vatsal Rakholiya](https://copyassignment.com/employee-management-system-project-in-python/)

