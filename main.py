'''
 # @ Author: Junping Luo
 # @ Create Time: 2022-08-02 14:35:40
 # @ Description: GUI version of Employee Management System Using Python by copyassignment.com
 '''


import email
from os import system
import re
from time import sleep
from tkinter import messagebox
import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk

# TODO Implement Generated Configuration File
mysqlConnector = mysql.connector.connect(
    host="localhost", user="root", password="halohalo")

mycursor = mysqlConnector.cursor()

# make a regular expression for validating an Email
emailPattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# for validating an Phone Number
phonePattern = r"(0|91)?[7-9][0-9]{9}"
idPattern = r"[0-9]+"
namePattern = r"[a-zA-Z]+ [a-zA-Z]+"


def init():
    try:
        # if DB not exist, create one
        mycursor.execute("CREATE DATABASE Employee")
        mycursor.execute("USE Employee")
    except:
        mycursor.execute("USE Employee")
    # Create Table
    try:
        mycursor.execute(
            "CREATE TABLE empdata ( Id INT(11) PRIMARY KEY , Name VARCHAR(1800), Emial_Id TEXT(1800),Phone_no BIGINT( 11 ), Address TEXT(1000), Post TEXT(1000), Salary BIGINT(20))")
    except:
        # Table is created, do nothing
        pass


def execSQL(cmd: str):
    try:
        mycursor.execute(cmd)
        return True
    except:
        return False


def doesEmployeeExist(employee_name, employee_id):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from empdata where Name=%s and Id=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = mysqlConnector.cursor(buffered=True)
    data = (employee_name, employee_id)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rowa with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


class AddEmployeeWindow(tk.Toplevel):
    def __init__(self, parent):
        # Entries:
        # ID, Name, Email, Phone, Address, Post, Salary
        super().__init__(parent)
        self.geometry('500x500')
        self.title('Employee Management System')
        id, fname, lname, email, phone, address, zipcode, salary = tk.StringVar(), tk.StringVar(
        ), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
        idLabel = Label(self, text="ID").grid(row=0, column=0)
        FnameLabel = Label(self, text="First Name").grid(row=1, column=0)
        LnameLabel = Label(self, text="Last Name").grid(row=2, column=0)
        emailLabel = Label(self, text="Email").grid(row=3, column=0)
        phoneLabel = Label(self, text="Phone Number").grid(row=4, column=0)
        addressLabel = Label(self, text="Address").grid(row=5, column=0)
        zipcodeLabel = Label(self, text='Zip Code').grid(row=6, column=0)
        salaryLabel = Label(self, text='Salary').grid(row=7, column=0)
        idEntry = Entry(self, textvariable=id).grid(row=0, column=1)
        FnameEntry = Entry(self, textvariable=fname).grid(row=1, column=1)
        LnameEntry = Entry(self, textvariable=lname).grid(row=2, column=1)
        emailEntry = Entry(self, textvariable=email).grid(row=3, column=1)
        phoneEntry = Entry(self, textvariable=phone).grid(row=4, column=1)
        addressEntry = Entry(self, textvariable=address).grid(row=5, column=1)
        zipcodeEntry = Entry(self, textvariable=zipcode).grid(row=6, column=1)
        salaryEntry = Entry(self, textvariable=salary).grid(row=7, column=1)
        # TODO Finish Functionality of the Submit button

        def Submit():
            name = f'{fname.get()} {lname.get()}'
            if doesEmployeeExist(name, id.get()):
                messagebox.showinfo(message="Employee exists.")
            elif not re.fullmatch(emailPattern, email.get()):
                messagebox.showinfo(message="Invalid Email Address")
            elif not re.fullmatch(phonePattern, phone.get()):
                print(phone.get())
                messagebox.showinfo(message="Invalid Phone Number")
            else:
                data = (int(id.get()), name, email.get(), phone.get(),
                        address.get(), zipcode.get(), salary.get())
                sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(sql, data)
                mysqlConnector.commit()
                messagebox.showinfo(message="Successfully Add A Employee!")
                self.destroy()
        btn = ttk.Button(self, text="Submit",
                         command=Submit).grid(row=8, column=0)
        # ttk.Button(self,
        #         text='Close',
        #         command=self.destroy).pack(expand=True)


class DisplayWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Employee Management System')

        ttk.Button(self,
                   text='Close',
                   command=self.destroy).pack(expand=True)


class UpdateWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Employee Management System')

        ttk.Button(self,
                   text='Close',
                   command=self.destroy).pack(expand=True)


class PromoteWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Employee Management System')

        ttk.Button(self,
                   text='Close',
                   command=self.destroy).pack(expand=True)


class RemoveWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Employee Management System')

        ttk.Button(self,
                   text='Close',
                   command=self.destroy).pack(expand=True)


class SearchWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Employee Management System')

        ttk.Button(self,
                   text='Close',
                   command=self.destroy).pack(expand=True)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.windows_dic = {
            'A': AddEmployeeWindow, 'D': DisplayWindow, 'U': UpdateWindow,
            'P': PromoteWindow, 'R': RemoveWindow, 'S': SearchWindow
        }
        self.geometry('500x300')
        self.title('Employee Management System')

        # place a button on the root window
        ttk.Button(self,
                   text='Add Employee Record',
                   command=lambda: self.open_new_window('A')).pack(expand=True)
        ttk.Button(self,
                   text='Display Records',
                   command=lambda: self.open_new_window('D')).pack(expand=True)
        ttk.Button(self,
                   text='Update Employee Record',
                   command=lambda: self.open_new_window('U')).pack(expand=True)
        ttk.Button(self,
                   text='Promote Employee',
                   command=lambda: self.open_new_window('P')).pack(expand=True)
        ttk.Button(self,
                   text='Remove Employee Record',
                   command=lambda: self.open_new_window('R')).pack(expand=True)
        ttk.Button(self,
                   text='Search Employee Record',
                   command=lambda: self.open_new_window('S')).pack(expand=True)
        ttk.Button(self,
                   text='Quit System',
                   command=lambda: self.destroy()).pack(expand=True)

    def open_new_window(self, win: str):
        new_window = self.windows_dic[win](self)
        new_window.grab_set()


if __name__ == "__main__":
    init()
    app = App()
    app.mainloop()
