from flask_socketio import SocketIO, send, join_room
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os
from flask import send_file

from PIL import Image, ImageTk
import pandas as pd
import sqlite3

import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import Preprocess as pre
import pdfdemo as pdfgen
import LogisticRegression as LR
import RandomForest as RF
import SVMLinearKernel as SVMLK
import SVMGaussianKernel as SVMGK
import Predict as PR
import recordingaudio as ras
import appendingpdf as ap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
#loading login page or main chat page
def index():
	if not session.get('logged_in'):
		return render_template("login.html")
	else:
		return render_template('home1.html')

@app.route('/main')
def about_page():
	path=request.form['datasetfolder']
	print(path)
	return render_template('home1.html')


@app.route('/registerpage',methods=['POST'])
def reg_page():
    return render_template("register.html")

@app.route('/loginpage',methods=['POST'])
def log_page():
    return render_template("login.html")

    
@app.route('/featureextraction',methods=['POST'])
def reg1_page():
	filename = os.path.join(app.root_path)
	path=filename+"/data"
	print("path===es",path)
	pre.process(path)
	print("Feature Extraction...")
	return render_template("home.html",message="Preprocess_Done")

	
@app.route('/lr',methods=['POST'])
def log_regression():
	path=request.form['csv']
	print(path)
	LR.process(path)
	print("Logistic Regression...")
	return render_template("home.html",message="Logistic_Regression_Done")


@app.route('/rf',methods=['POST'])
def random_forest():
	path=request.form['csv']
	print(path)
	RF.process(path)
	print("Random Forest...")
	return render_template("home.html",message="Random_Forest_Done")

@app.route('/svmlr',methods=['POST'])
def svm_lr():
	path=request.form['csv']
	print(path)
	SVMLK.process(path)
	print("SVM Linear Kernel...")
	return render_template("home.html",message="SVM_Linear_Kernal_Done")
	
@app.route('/svmgk',methods=['POST'])
def svm_gr():
	path=request.form['csv']
	print(path)
	SVMGK.process(path)
	print("SVM Linear Kernel...")
	return render_template("home.html",message="SVM_Gaussion_Kernal_Done")

@app.route('/reco',methods=['POST'])
def voice_rec():
	path=request.form['fname']
	print(path)
	ras.process(path)
	print("Recording...")
	return render_template("home.html",message="Recording_Done")
@app.route('/download', methods=['POST'])
def download_file():
	path=""
	uname= session['patname']
	print("uname==",uname)
	path=str(uname)+"final.pdf"
	return send_file(path, as_attachment=True)


@app.route('/predict',methods=['POST'])
def predict():
	uname= session['patname']  
	path=request.form['af']
	print(path)
	msg="You have diagnoised with "
	result=PR.process(path)
	res=result.split(":")
	print("resssssssss",res[0])
	#session["prec"]=res[1]
	if res[0] == "Normal":
		msg+="Healthy"
	else:
		msg=msg+res[1]+" % Depression"
	ap.process(uname,uname,msg)


	
	print("Prediction...")
	return render_template("home.html",message=res)



@app.route('/Back')
def back():
    return render_template("home.html")
    
    
   
@app.route('/register',methods=['POST'])
def reg():
	name=request.form['name']
	username=request.form['username']
	password=request.form['password']
	email=request.form['emailid']
	mobile=request.form['mobile']
	conn= sqlite3.connect("Database")
	cmd="SELECT * FROM login WHERE username='"+username+"'"
	print(cmd)
	cursor=conn.execute(cmd)
	isRecordExist=0
	for row in cursor:
		isRecordExist=1
	if(isRecordExist==1):
	        print("Username Already Exists")
	        return render_template("usernameexist.html")
	else:
		print("insert")
		cmd="INSERT INTO login Values('"+str(name)+"','"+str(username)+"','"+str(password)+"','"+str(email)+"','"+str(mobile)+"')"
		print(cmd)
		print("Inserted Successfully")
		conn.execute(cmd)
		conn.commit()
		conn.close() 
		return render_template("inserted.html")



@app.route('/patreg',methods=['GET','POST'])
def patreg():
	
	#if request.method == 'POST':
		#pid=request.form.get('pid')
		#pname=request.form.get('pname')
		#age=request.form.get('age')
		#gender.request.form.get('g1')
		#return redirect(url_for('reportpage',pid=pid, pname=pname, age=age))
	#return render_template("home.html")
	
	
	
	pid=request.form['pid']
	pname=request.form['pname']
	age=request.form['age']
	gender=request.form['g1']
	session['patname'] = request.form['pname']
	pdfgen.process(pid,pname,age,gender)
	return render_template("home.html")


	
#-----------------------report trial-----------------------------------------


@app.route('/reportpage',methods=['GET','POST'])
def reportpage():
	if request.method=="POST":
		pid = request.form['pid']
		pname = request.form['pname']
		age = request.form['age']
		percent=request.form['percent']
		#gender = request.form('g1',None)
		return render_template("trial.html" ,pid=pid, pname=pname, age=age , percent=percent)



#----------------------------------------------------------------	
	
@app.route('/login',methods=['POST'])
def log_in():
	#complete login if name is not an empty string or doesnt corss with any names currently used across sessions
	if request.form['username'] != None and request.form['username'] != "" and request.form['password'] != None and request.form['password'] != "":
		username=request.form['username']
		password=request.form['password']
		conn= sqlite3.connect("Database")
		cmd="SELECT username,password FROM login WHERE username='"+username+"' and password='"+password+"'"
		print(cmd)
		cursor=conn.execute(cmd)
		isRecordExist=0
		for row in cursor:
			isRecordExist=1
		if(isRecordExist==1):
			session['logged_in'] = True
			# cross check names and see if name exists in current session
			session['username'] = request.form['username']
			return redirect(url_for('index'))

	return redirect(url_for('index'))
	
@app.route("/logout",methods=['POST'])
def log_out():
    session.clear()
    return render_template("login.html")

# /////////socket io config ///////////////
#when message is recieved from the client    
@socketio.on('message')
def handleMessage(msg):
    print("Message recieved: " + msg)
 
# socket-io error handling
@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    pass


  
  
if __name__ == '__main__':
    socketio.run(app,debug=True,host='127.0.0.1', port=4000)
