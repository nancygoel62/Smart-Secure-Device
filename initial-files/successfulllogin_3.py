from Tkinter import *
import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()
import tkMessageBox

db=MySQLdb.connect("localhost","root","iamthriving","Mydatabase")
curs=db.cursor() 
root=Tk()
root.minsize()
var=IntVar()


def backfunc():
		root.destroy()
		import successfulllogin


def pas():
	if var.get() ==1:
		def backfunc1():
			       r1.destroy()
	        	       import successfulllogin_3

			       #root.destroy()
		def uchange():
                                if(e1.get()==e2.get()):
					v1=e1.get()
                                        curs.execute("update login set password= %s where username='user'",(v1))
					print e1.get()                                        
					tkMessageBox.showinfo("SUCCESS","PASSWORD CHANGED SUCCESSFULLY!")
					r1.destroy()
					db.commit()
					import successfulllogin_3

                                else:
                                        tkMessageBox.showinfo("FAIL!","invalid entry try again")
                                        e1.delete(0,END)
                                        e1.insert(0,"")
                                        e2.delete(0,END)
                                        e2.insert(0,"")
	
		root.destroy()
        	#tkMessageBox.showinfo("window","change user password")
		r1=Tk()
		l1=Label(r1,text="enter new password ")
		l1.grid(row=0,column=0)
		e1=Entry(r1,show="*")
		e1.grid(row=0, column=1)
		l2=Label(r1,text="verify new password ")
		l2.grid(row=1,column=0)
                e2=Entry(r1,show="*")
		e2.grid(row=1, column=1)
		b2=Button(r1,text="back",command=backfunc1)
		b2.grid(row=2,column=0)
		b=Button(r1,text="submit",command=uchange)
		b.grid(row=2,column=1)
		
		
	if var.get() ==2:
		root.destroy()
                #tkMessageBox.showinfo("window","change user password")
                r1=Tk()
                def adminchange():
                                if(e1.get()==e2.get()):
                                        curs.execute("update login set password= %s where username='admin'",(e1.get()))
                                        db.commit()
					tkMessageBox.showinfo("window","password changed")
					r1.destroy()
                                        import successfulllogin_3

                                else:
                                        tkMessageBox.showinfo("window","invalid entry try again")
                                        e1.delete(0,END)
                                        e1.insert(0,"")
                                        e2.delete(0,END)
                                        e2.insert(0,"")
		def backfunc1():
				r1.destroy()
				import successfulllogin

		l1=Label(r1,text="enter new password ")
		l1.grid(row=0,column=0)
                e1=Entry(r1,show="*")
		e1.grid(row=0, column=1)
                l2=Label(r1,text="verify new password ")
		l2.grid(row=1,column=0)
                e2=Entry(r1,show="*")
		e2.grid(row=1, column=1)
                b2=Button(r1,text="back",command=backfunc1)
		b2.grid(row=2,column=0)
		b=Button(r1,text="submit",command=adminchange)
		b.grid(row=3,column=1)
		
			
		
	if var.get() ==3:
                root.destry()
		
                r1=Tk()
		def phonechange():
                                if(e1.get()==e2.get()):
                                        curs.execute("update login set phone= %s where username='admin'",(e1.get()))
                                        db.commit()
                                        import successfulllogin_3

                                else:
                                        tkMessageBox.showinfo("window","invalid entry try again")
                                        e1.delete(0,END)
                                        e1.insert(0,"")
                                        e2.delete(0,END)
                                        e2.insert(0,"")
		def backfunc1():
                                r1.destroy()
                                import successfulllogin



                Label(r1,text="enter new phone no. ").grid(row=0,column=0)
                e1=Entry(r1).grid(row=0, column=1)
                Label(r1,text="verify new phone no. ").grid(row=1,column=0)
                e2=Entry(r1).grid(row=1, column=1)
	        b2=Button(r1,text="back",command=backfunc1).grid(row=2,column=0)

		b=Button(r1,text="submit",command=phonechange).grid(row=3,column=1)
		root.destroy()
		

w=Label(root,text="SETTINGS",fg="dark blue",font=("times",15,"bold")).grid(row=0)
r1=Radiobutton(root, text="Change User Password",variable=var,value=1,command=pas).grid(row=1,column=1)
#e1=Entry(root).grid(row=0,column=2)
r2=Radiobutton(root, text="Change Admin Password",variable=var,padx=20,value=2,command=pas).grid(row=2,column=1)
#e2=Entry(root).grid(row=1,column=2)
r3=Radiobutton(root, text="Change Phone No",variable=var,padx=20, value=3, command= pas).grid(row=4,column=1)
b5=Button(root,text="back",bg="grey",fg="dark blue",command=backfunc).grid(row=4,column=0)

root.mainloop()

