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
        print(gmm)
        spectral_centroids = librosa.feature.spectral_centroid(b, sr=SAMPLE_RATE)[0]
        print("-------------")
        print(spectral_centroids)
        return pd.Series(np.hstack((np.mean(gmm, axis=1), np.std(gmm, axis=1))))
    except:
        print('bad file')
        return pd.Series([0]*40)

def process(path):
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
	        mfcc.append(s.tolist())
	full=[]
	for i in range(0,len(mfcc)):
		print(mfcc[i])
		d=[]
		for j in mfcc[i]:
			print(j)
			d.append(j)
		d.append(0)
		d.append(name[i])
		
		full.append(d)
	print(full)
	with open('NormalMFCC.csv', 'w',newline='') as myfile:
	    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	    for x in full:
	        wr.writerow(x)

process("Normal")
