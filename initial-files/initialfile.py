#!/usr/bin/python
#local database at mysql
#table name-login
#database-Mydatabase Password-iamthriving
from Tkinter import *
import tkMessageBox
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import datetime
from datetime import date
import time
 

#database connections
db=MySQLdb.connect("localhost","root","iamthriving","Mydatabase")
curs=db.cursor()


root=Tk()
#initialising the size of window
root.minsize(200,200)

#function for current date and time time 
def time_data():
	dt=datetime.datetime.now()
	clock.config(text=dt.strftime("%A, %d. %B %Y %I:%M%p"))
	clock.grid(row=1,column=1)
	root.after(1000,time_data) #updates after 1 second
		
#function for validating user's input
def action():
        curs.execute("select password from login where password = %s ",e2.get())
        rows=curs.fetchall()
#if will be executed if the entered password is correct
        if (rows):
                print rows
		tkMessageBox.showinfo("WELCOME", "AUTHORIZED ENTRY!")
		#destroy the current window		
		root.destroy()
		#importing the another file successfulllogin.py from the same directory
		import successfulllogin
#will be executed when password is wrong
        else:
                print " invalid entry"
		e2.delete(0,END)
		e2.insert(0,"")
		tkMessageBox.showinfo("window", "WRONG PASSWORD!")
		#calling the another file in backend named invalidlogin.py for capturing image and send email and phone call		
		import invalidlogin
		print "invalidlogin imported"
clock=Label(root, text="",fg='blue',font=('times',15,'bold'))
clock.config(text=datetime.datetime.now())

#labels in Tkinter
w1=Label(root,text="WELCOME").grid(row=2,column=1)

w2=Label(root,text="Enter Password").grid(row=3,column=1)
#hide the password using *
e2=Entry(root,show="*")
e2.grid(row=5,column=1)

Button(root, text='login', command=action).grid(row=6, column=1)


time_data()
root.mainloop()
db.commit()
