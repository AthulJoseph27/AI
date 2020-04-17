import cv2
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten,Dropout
from keras.layers import Conv2D, MaxPooling2D
import numpy as np
import os
import matplotlib.pyplot as plt
import random
import pickle

cur_path = os.path.dirname(__file__)#gets the current path


Folder = ["Dog","Cat"]

# d = 0
# c = 0
x_train = []
y_train = []
x_test = []
y_test = []
test_img = []

#*****************************  PRE-PRROCESSING ******************************************


for i in Folder:
	path = os.path.join(cur_path , i)#opens the folder Dogs in the current directory

	
	for img in os.listdir(path):#loading images inside the folder Dogs
		try:
			image = cv2.imread(os.path.join(path,img), 0)
		except Exception as e:
			pass

		if image is None:
			continue
		image = cv2.resize(image,(60,60))
		image_flip = cv2.flip(image , 1)
		x_train.append(image)
		x_train.append(image_flip)
		if i == 'Dog':
			y_train.append(0)
			y_train.append(0)
			# d+=1
		else:
			y_train.append(1)
			y_train.append(1)
			# c+=1

# print(d)
# print(c)





for i in range(0,100):
	x_test.append(x_train[0])
	x_train.pop(0)
	y_test.append((y_train[0]))
	y_train.pop(0)
	test_img.append(x_train[0])

for i in range(0,100):
	x_test.append(x_train[-1])
	x_train.pop(-1)
	y_test.append((y_train[-1]))
	y_train.pop(-1)
	test_img.append(-1)

temp = list(zip(x_train,y_train))
random.shuffle(temp)
x_train,y_train = zip(*temp)

temp = list(zip(x_test,y_test,test_img))
random.shuffle(temp)
x_test,y_test,test_img = zip(*temp)

x_train = np.array(x_train)
x_train = x_train/255

x_test = np.array(x_test).reshape(-1 , 60 , 60 , 1)



dbfile = open('TestingIMG','ab')
pickle.dump(test_img , dbfile)
dbfile.close()


dbfile = open('TestingData','ab')
pickle.dump(x_test , dbfile)
dbfile.close()

dbfile = open('TestingLabels','ab')
pickle.dump(y_test , dbfile)
dbfile.close()



