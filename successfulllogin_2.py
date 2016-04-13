#!/usr/bin/python
from Tkinter import *
import pymysql
pymysql.install_as_MySQLdb()
import tkMessageBox
import MySQLdb

db=MySQLdb.connect("localhost","root","iamthriving","Mydatabase")
curs=db.cursor()


root=Tk()
root.minsize(300,300)
def action():
        curs.execute("select * from login where username= %s and password = %s ",(e1.get(),e2.get() ))
        rows=curs.fetchall()
        if (rows):
               root.destroy()
	       import successfulllogin_3


        else:
	       e1.delete(0,END)
	       e1.insert(0,"")
	       e2.delete(0,END)
	       e2.insert(0,"")
               tkMessageBox.showinfo("admin", "WRONG PASSWORD! TRY AGAIN")
	       
   
w0=Label(root,text="ADMIN LOGIN!",fg="dark blue",font=("times",15,"bold")).grid(row=0)
w1=Label(root,text=" ADMIN").grid(row=1)
e1=Entry(root)
e1.grid(row=1,column=1)
w2=Label(root,text="password").grid(row=2)

#e1=Entry(root)
e2=Entry(root,show="*")

#e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
Button(root, text='login', command=action).grid(row=3, column=1)


root.mainloop()

