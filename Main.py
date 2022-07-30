import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import Preprocess as pre
import LogisticRegression as LR
import RandomForest as RF
import SVMLinearKernel as SVMLK
import SVMGaussianKernel as SVMGK
import Predict as PR
import recordingaudio as ras

bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"


def Home():
	global window
	def clear():
	    print("Clear1")
	    txt.delete(0, 'end')    
	    txt1.delete(0, 'end')
	    txt2.delete(0, 'end')
	    txt3.delete(0, 'end')
  



	window = tk.Tk()
	window.title("Child Depression Prediction")

 
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	

	message1 = tk.Label(window, text="Child Depression Prediction" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=20)

	lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=100, y=200)
	
	txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=400, y=215)

	lbl1 = tk.Label(window, text="Select Dataset(CSV)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=100, y=270)
	
	txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=400, y=275)

	lbl3 = tk.Label(window, text="Enter file name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl3.place(x=100, y=330)
	
	txt3 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt3.place(x=400, y=335)
	lbl2 = tk.Label(window, text="Select Audio File",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl2.place(x=100, y=385)
	
	txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt2.place(x=400, y=390)


	def browse():
		path=filedialog.askdirectory()
		print(path)
		txt.delete(0, 'end')
		txt.insert('end',path)
		if path !="":
			print(path)
		else:
			tm.showinfo("Input error", "Select DataSet Folder")	

	def browse1():
		path=filedialog.askopenfilename()
		print(path)
		txt1.delete(0, 'end')
		txt1.insert('end',path)
		if path !="":
			print(path)
		else:
			tm.showinfo("Input error", "Select Datset")	

	def browse2():
		path=filedialog.askopenfilename()
		print(path)
		txt2.delete(0, 'end')
		txt2.insert('end',path)
		if path !="":
			print(path)
		else:
			tm.showinfo("Input error", "Select Audio File")
	def recaudio():
                fname=txt3.get()
                if fname !="":
                        ras.process(fname)
                        tm.showinfo("Success", "Audio file stored in D drive")
                else:
                        tm.showinfo("Input error", "Enter audio file name")
                        
                        
                        

	def preproc():
		sym=txt.get()
		if sym != "" :
			pre.process(sym)
			print("preprocess")
			tm.showinfo("Input", "Preprocess Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset")

	def LRprocess():
		sym=txt1.get()
		if sym != "":
			LR.process(sym)
			tm.showinfo("Input", "Logistic Regression Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset File")

	def RFprocess():
		sym=txt1.get()
		if sym != "":
			RF.process(sym)
			tm.showinfo("Input", "Random Forest Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset File")

	def SVMLKprocess():
		sym=txt1.get()
		if sym != "":
			SVMLK.process(sym)
			tm.showinfo("Input", "SVM Linear Kernel Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset File")

	def SVMGKprocess():
		sym=txt1.get()
		if sym != "":
			SVMGK.process(sym)
			tm.showinfo("Input", "SVM Gaussian Kernel Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset File")

	def Predictprocess():
		sym=txt2.get()
		if sym != "":
			result=PR.process(sym)
			tm.showinfo("Input", "Prediction : " +str(result))
		else:
			tm.showinfo("Input error", "Select Audio File")

	browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse.place(x=650, y=200)

	browse1 = tk.Button(window, text="Browse", command=browse1  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse1.place(x=650, y=270)

	browse2 = tk.Button(window, text="Browse", command=browse2  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse2.place(x=650, y=385)
	rec = tk.Button(window, text="Record Audio", command=recaudio  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	rec.place(x=650, y=330)

	clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
	clearButton.place(x=950, y=200)
	 
	proc = tk.Button(window, text="Preprocess", command=preproc  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	proc.place(x=10, y=600)
	

	LRbutton = tk.Button(window, text="LogisticRegression", command=LRprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	LRbutton.place(x=180, y=600)


	RFbutton = tk.Button(window, text="RandomForest", command=RFprocess  ,fg=fgcolor   ,bg=bgcolor1 ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	RFbutton.place(x=355, y=600)

	SVMbutton = tk.Button(window, text="SVMLinearKernel", command=SVMLKprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	SVMbutton.place(x=525, y=600)

	SVM1button = tk.Button(window, text="SVMGaussianKernel", command=SVMGKprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=16  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	SVM1button.place(x=700, y=600)

	PRbutton = tk.Button(window, text="Predict", command=Predictprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	PRbutton.place(x=900, y=600)

	quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=1070, y=600)

	window.mainloop()
Home()

