import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import random
import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten,Dropout
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
import random
import pickle

def mean(*args):
	s=0
	count=0
	for i in args:
		s = s+i
		count+=1
	return (s/count)


cur_dir = os.path.dirname(__file__)

bg_path = os.path.join(cur_dir,'Blank.png')


path = os.path.join(cur_dir,"T2")




image = cv2.imread(os.path.join(path,'G.png'),0)
bg = cv2.imread(bg_path)
x,y = image.shape
bg = cv2.resize(bg,(y,x))
ret,thresh = cv2.threshold(image,127,255,0)
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


in_char = []
temp = contours
area = cv2.contourArea(contours[0])
index_area = 0
for i in range(len(contours)):
	if cv2.contourArea(contours[i]) > area:
		area = cv2.contourArea(contours[i])
		index_area = i

contours.pop(index_area)

for i in range(len(contours)):
	if((i+1)<len(contours)):
		if(cv2.pointPolygonTest(contours[i], tuple(contours[i+1][0][0]), False) > 0):
			in_char.append(contours[i+1])
			temp.pop(i+1)

contours = temp

for i in range(len(contours)):
	for j in range(len(contours)-1):
		small_0 = min(list(contours[j][0]))
		small_1 = min(list(contours[j+1][0]))
 
		if small_0[0] > small_1[0]:
			temp = contours[j]
			contours[j] = contours[j+1]
			contours[j+1] = temp


for i in range(len(contours)):
	for j in range(len(contours)-1):
		small_0 = max(list(contours[j][0]))
		small_1 = max(list(contours[j+1][0]))
		if small_0[1] > (small_1[1]+20):
			temp = contours[j]
			contours[j] = contours[j+1]
			contours[j+1] = temp



			

for i in range(len(contours)):
	if((i+1)<len(contours)):
		cv2.drawContours(bg, contours, i, color = (0,0,0), thickness=cv2.FILLED)
		for k in range(len(in_char)):
			if(cv2.pointPolygonTest(contours[i], tuple(in_char[k][0][0]), False) > 0):
				cv2.drawContours(bg, contours, i, color = (0,0,0), thickness=cv2.FILLED)
				cv2.drawContours(bg, in_char, k, color = (255,255,255), thickness=cv2.FILLED)
				
				
	else:
		cv2.drawContours(bg, contours, i, color = (0,0,0), thickness=cv2.FILLED)
	
	top_left = contours[i][0][0]
	bottom_right = contours[i][0][-1]
	for x in range(len(contours[i])):
		if (bottom_right[0] < contours[i][x][0][0]) or (bottom_right[1] < contours[i][x][0][1]):
			bottom_right = contours[i][x][0]

	top_left[0]-= 40
	top_left[1]-= 40
	bottom_right[0] += 40
	bottom_right[1] += 40

	y,x = image.shape


	if top_left[0] < 0:
		top_left[0] = 0
	if top_left[1] < 0:
		top_left[1] = 0

	if top_left[0] > x:
		top_left[0] = x-1
	if top_left[1] > y:
		top_left[1] = y-1

	if bottom_right[0] > x:
		bottom_right[0] = x-1
	if bottom_right[1] > y:
		bottom_right[1] = y-1

	if bottom_right in top_left:
		continue


	bg_extract = bg[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
	
	#bg = cv2.rectangle(bg, tuple(top_left), tuple(bottom_right), (0,255,0), 3)

	while True:
		cv2.imshow("Orginal",image)
		cv2.imshow("Cropped",bg_extract)
		plt.imsave(os.path.join(os.path.join(cur_dir,"Prediction"),'p{}.png'.format(i)),bg_extract)
		k = cv2.waitKey(5)
		if k == 27:
			bg = cv2.imread(bg_path)
			x,y = image.shape
			bg = cv2.resize(bg,(y,x))
			break

cv2.destroyAllWindows()

x_test = []
cur_dir = os.path.dirname(__file__)

path = os.path.join(cur_dir,'Prediction')

pictures = os.listdir(path)

pictures.sort()

for img in pictures :
	image = cv2.imread(os.path.join(path,img),0)
	if image is None:
		continue
	image = cv2.resize(image,(28,28))
	x_test.append(image)

y_test = x_test

x_test = np.array(x_test)

x_test = np.array(x_test).reshape(-1 , 28 , 28 , 1).astype('float32')
x_test = x_test/255

model = keras.models.load_model("A_Z.h5")

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

prediction1 = model.predict(x_test)

model = keras.models.load_model("A_Z2.h5")

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

prediction2 = model.predict(x_test)

model = keras.models.load_model("A_Z3.h5")

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

prediction3 = model.predict(x_test)

model = keras.models.load_model("A_Z4.h5")

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

prediction4 = model.predict(x_test)

model = keras.models.load_model("A_Z5.h5")

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

prediction5 = model.predict(x_test)

model = keras.models.load_model("A_Z.h5")

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

prediction6 = model.predict(x_test)

temp = []
prediction = []


for i in range(len(prediction1)):
	temp = []
	for j in range(len(prediction1[i])):
		temp.append(mean(prediction1[i][j],prediction2[i][j],prediction3[i][j],prediction4[i][j],prediction5[i][j],prediction6[i][j]))
	prediction.append(temp)


s=""

for i in range(len(x_test)):
	plt.grid(False)
	plt.imshow(y_test[i], cmap='gray')
	p = np.argmax(prediction[i])
	prob = prediction[i][p]
	plt.title("Prediction : "+chr(p+65)+"  ( "+("%.2f"%(prob*100))+" % )")
	plt.show()

for i in range(len(x_test)):
	p = np.argmax(prediction[i])
	prob = prediction[i][p]
	if prob > 0.8:
		s+=chr(p+65)
	else:
		s+='?'
print(s)

for img in pictures:
	os.remove(os.path.join(os.path.join(cur_dir,"Prediction"),img))
