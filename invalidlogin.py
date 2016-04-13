from Tkinter import *
import tkMessageBox 
import serial 
import time 
import datetime
import smtplib
import pymysql
pymysql.install_as_MySQLdb()
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import MySQLdb


port = serial.Serial("/dev/ttyAMA0", 9600, timeout=3.0) 
db=MySQLdb.connect("localhost","root","iamthriving","Mydatabase")
curs=db.cursor()

print "\n\nWrong password, UNAUTHORIZED ENTRY...\nProcessing..\n"
try:
	  

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	camera=picamera.PiCamera()
	print "Capturing photo in 3 seconds\n"
	print "3"
	time.sleep(1)
	print "2"
	time.sleep(1)
	print "1"
	time.sleep(1)
	string=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
	imagename="images/"+string+".jpg"
	print imagename
	camera.capture(imagename)
	camera.vflip=True
	camera.hflip=True
	camera.brightness=70
	print "captured"
	curs.execute("select email from login where username='admin'")
	rows=curs.fetchall()

	print "Mailing captured Image to the Owner...\n"
	f=open(imagename,"rb")
	img=MIMEImage(f.read())
	f.close()
	msg=MIMEMultipart()
	msg.attach(img)
	smtpUser = "stp6group6@gmail.com"
	smtpPass = "groupsix"
	for row in rows:
		toAdd= row[0]
	fromAdd = smtpUser
	msg['Subject']='UNAUTHORIZED ACCESS'
	msg['From']=smtpUser
	msg['To']=toAdd
	
	header = "To: " + toAdd + "\n" + "From: " + fromAdd + "\n"
	body= "Someome is trying to unlock GENSMART, here is the image.."
	text=MIMEText(body)
	msg.attach(text)
	
	s= smtplib.SMTP('smtp.gmail.com',587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(smtpUser,smtpPass)
	#s.sendmail(fromAdd,toAdd,header + "\n\n" + body)
	s.sendmail(fromAdd,toAdd,msg.as_string())
	s.quit()

	print "Mailed Successfully..\n\nCalling to the owner....\n\n"
	curs.execute("select phone from login where username='admin'")
	rowp=curs.fetchall()
	port.write('AT\r\n')		
	rcv = port.read(20) 
	while True: 
		rcv = port.read(20) 
		print rcv
		time.sleep(4)  
		#if keyin== "y": 
		if rcv== "BUSY":
			print "try again"
	#		port.close()
	#		break
		else:
			for row in rowp:
				keyin = row[0] 
			print keyin
			keyin2 = 'ATD '+keyin+';\r\n' 
			print"Dialing : " + keyin2 
			port.write(keyin2)
		break
		#x=1 
		#for x in range(0,9): 
		#	rcv= port.read(50) 
		#	print rcv
		#	x+=1 
		#else : 
			#if keyin == "n": 
				#rcv= port.read(50) 
				#print rcv
				#time.sleep(2) 
			#if rcv=='RING':			
				#print 'ring' 
				#port.write('ATH \r\n') 
	##FOR TEXT MESSAGING
	time.sleep(4)
	
except: 
	port.close() 
