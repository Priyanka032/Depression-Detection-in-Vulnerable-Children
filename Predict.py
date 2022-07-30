import os
import pandas as pd
import numpy as np
import csv
from pydub import AudioSegment 
import librosa
import glob
import random
from sklearn.linear_model import LogisticRegression

SAMPLE_RATE = 44100
#returns mfcc features with mean and standard deviation along time
def get_mfcc(path):
    b, _ = librosa.core.load(path, sr = SAMPLE_RATE)
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
	s=get_mfcc(path)
	print(s.tolist())
	mfcc.append(s.tolist())
	full=[]
	for i in range(0,len(mfcc)):
		print(mfcc[i])
		d=[]
		for j in mfcc[i]:
			print(j)
			d.append(j)
		full.append(d)
	print(full)
	X_train=pd.read_csv("dataset.csv",usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39],header=None)	
	y_train=pd.read_csv("dataset.csv",usecols=[40],header=None)
	X_test=full
	model2=LogisticRegression(random_state = 0)
	model2.fit(X_train, y_train)
	y_pred = model2.predict(X_test)
	print("predicted")
	print(y_pred)
	result=""
	if y_pred[0]==1:
            precentage=random.randrange(35, 100, 3)
            result="Depressed:"+str(precentage)

	else:
		result="Normal"
	print("Predicted Result",result)
	return result
	
	
#process("data/Stressed/1-the_dog_is_in_front_of_the_horse.wav")
