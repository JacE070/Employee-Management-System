import mysql.connector
from os import system
import re
import tkinter
#making Connection
con = mysql.connector.connect (
host = " 127.0.0.1 " , user = " root " , password = "aa203909")
mycursor= con.cursor() #allows row-by-row processing of the result sets.
mycursor.execute('CREATE DATABASE Employee')

def check_employee_name(employee_name):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from empdata where Name=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_name,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rowa with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


# Function To Check if Employee With
# given Id Exist or not
def check_employee(employee_id):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from empdata where Id=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rowa with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

# Function to Add_Employee
def Add_Employ():
    print("{:>60}".format("-->>Add Employee Record<<--"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == True):
        print("Employee ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Name = input("Enter Employee Name: ")
    # checking If Employee Name is Exit Or Not
    if (check_employee_name(Name) == True):
        print("Employee Name Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ
    Email_Id = input("Enter Employee Email ID: ")
    if(re.fullmatch(regex, Email_Id)):
        print("Valid Email")
    else:
        print("Invalid Email")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Phone_no = input("Enter Employee Phone No.: ")
    if(Pattern.match(Phone_no)):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)
    # Instering Employee Details in
    # the Employee (empdata) Table
    sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()

    # Executing the sql Query
    c.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key To Continue..")
    menu()