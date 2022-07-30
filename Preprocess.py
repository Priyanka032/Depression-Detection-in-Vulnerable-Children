import os
import pandas as pd
import numpy as np
import csv
from pydub import AudioSegment 
import librosa
import glob


SAMPLE_RATE = 44100
#returns mfcc features with mean and standard deviation along time
def get_mfcc(name, path):
    b, _ = librosa.core.load(path + name, sr = SAMPLE_RATE)
    assert _ == SAMPLE_RATE
    try:
        gmm = librosa.feature.mfcc(b, sr = SAMPLE_RATE, n_mfcc=20)
        print("MFCC")
        print(gmm)
        print("-------")
        
        return pd.Series(np.hstack((np.mean(gmm, axis=1), np.std(gmm, axis=1))))
    except:
        print('bad file')
        return pd.Series([0]*40)
def get_spc(name, path):
    b, _ = librosa.core.load(path + name, sr = SAMPLE_RATE)
    assert _ == SAMPLE_RATE
    try:
        spectral_centroids = librosa.feature.spectral_centroid(b, sr=SAMPLE_RATE)[0]
        print("SPC")
        print(spectral_centroids)
        print("-------------")
        return pd.Series(np.hstack((np.mean(spectral_centroids, axis=1), np.std(spectral_centroids, axis=1))))
    except:
        print('bad file')
        return pd.Series([0]*40)

def get_Spectrogram(name, path):
    x, _ = librosa.core.load(path + name,sr=SAMPLE_RATE)
    
    try:
        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))
        print("Spectrogram")
        print(Xdb)
        print("-----------------")
        return pd.Series(np.hstack((np.mean(Xdb, axis=1), np.std(Xdb, axis=1))))
    except:
        print('bad file')
        return pd.Series([0]*40)
def get_zero(name, path):
    x, _ = librosa.core.load(path + name,sr=SAMPLE_RATE)
    n0 = 9000
    n1 = 9100
    
    try:
        zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)
        print("zero_crossing")
        print(sum(zero_crossings))
        print("-----------------")
        return pd.Series(np.hstack((np.mean(zero_crossings, axis=1), np.std(zero_crossings, axis=1))))
    except:
        print('bad file')
        return pd.Series([0]*40)


def processStressed(path):
	mfcc=[]
	name=[]
	clas=[]
	sample=[]
	for i in range(1,2):
	    cl=0
	    for file in glob.glob(path+"/*.wav".format(i)):
	        name.append(file.split('\\')[-1].split('.')[0])
	        filename=file.split('\\')[-1].split('.')[0]+".wav"
	        s=get_mfcc(filename, path+'/')
	        
	        
	        
	        #print(s.tolist())
	        mfcc.append(s.tolist())
	        
	        
	print("length of mfcc:",len(mfcc))
	full=[]
	for i in range(0,len(mfcc)):
		#print(mfcc[i])
		d=[]
		for j in mfcc[i]:
			#print(j)
			d.append(j)
		d.append(1)
		#d.append(name[i])
		
		full.append(d)
	print(full)
	with open('StressedMFCC.csv', 'w',newline='') as myfile:
	    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	    for x in full:
	        wr.writerow(x)

def processNormal(path):
	mfcc=[]
	name=[]
	clas=[]
	sample=[]
	for i in range(1,2):
	    cl=0
	    for file in glob.glob(path+"/*.wav".format(i)):
	        name.append(file.split('\\')[-1].split('.')[0])
	        filename=file.split('\\')[-1].split('.')[0]+".wav"
	        s=get_mfcc(filename, path+'/')
	        
	        
	        
	        #print(s.tolist())
	        mfcc.append(s.tolist())
	        
	        
	        
	print("length of mfcc:",len(mfcc))
	full=[]
	for i in range(0,len(mfcc)):
		#print(mfcc[i])
		d=[]
		for j in mfcc[i]:
			#print(j)
			d.append(j)
		d.append(0)
		#d.append(name[i])
		
		full.append(d)
	print(full)
	with open('NormalMFCC.csv', 'w',newline='') as myfile:
	    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	    for x in full:
	        wr.writerow(x)

def process(path):
    #path="\\data"
    print("path==",path)
    processNormal(path+"/Normal")
    processStressed(path+"/Stressed")
    reader = csv.reader(open("NormalMFCC.csv"))
    reader1 = csv.reader(open("StressedMFCC.csv"))
    f = open("dataset.csv", "w",newline='')
    writer = csv.writer(f)

    for row in reader:
        writer.writerow(row)
    for row in reader1:
        writer.writerow(row)
    f.close()

