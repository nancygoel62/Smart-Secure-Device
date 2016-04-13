#!/usr/bin/python
from Tkinter import *
import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import tkMessageBox
#import RPi.GPIO as GPIO	
import datetime


root=Tk()
root.minsize(300,300)

def time_data():
		clock.config(text=datetime.datetime.now())
		clock.grid(row=0)
		root.after(1000,time_data)

def lock():
	tkMessageBox.showinfo("window", "YOUR DEVICE IS LOCKED SUCESSFULLY")
	root.destroy()

def set():
	root.destroy()
	import successfulllogin_2

clock=Label(root,text="",fg='red',font=('times',15,'bold'))
clock.config(text=datetime.datetime.now())
w1=Label(root,text="UNLOCKED",fg="dark green").grid(row=1)
Button(root, text='Settings',fg="dark blue",bg="grey",command=set,font=("times",15,"bold")).grid(row=3, column=0)
Button(root, text='Lock',fg="dark blue",bg="grey",command=lock,font=("times",15,"bold")).grid(row=3, column=2)

time_data()	
root.mainloop()

