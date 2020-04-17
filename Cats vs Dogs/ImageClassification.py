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

#*****************************  PRE-PRROCESSING ******************************************


# for i in Folder:
# 	path = os.path.join(cur_path , i)#opens the folder Dogs in the current directory

	
# 	for img in os.listdir(path):#loading images inside the folder Dogs
# 		try:
# 			image = cv2.imread(os.path.join(path,img), 0)
# 		except Exception as e:
# 			pass

# 		if image is None:
# 			continue
# 		image = cv2.resize(image,(70,70))
# 		image_flip = cv2.flip(image , 1)
# 		x_train.append(image)
# 		x_train.append(image_flip)
# 		if i == 'Dog':
# 			y_train.append(0)
# 			y_train.append(0)
# 			# d+=1
# 		else:
# 			y_train.append(1)
# 			y_train.append(1)
# 			# c+=1

# # print(d)
# # print(c)








# temp = list(zip(x_train,y_train))
# random.shuffle(temp)
# x_train,y_train = zip(*temp)

# x_train = np.array(x_train)
# x_train = x_train/255

# x_train = np.array(x_train).reshape(-1 , 70 , 70 , 1)



# dbfile = open('TrainingData','ab')
# pickle.dump(x_train , dbfile)
# dbfile.close()

# dbfile = open('TrainingLabels','ab')
# pickle.dump(y_train , dbfile)
# dbfile.close()



#*****************************  PRE-PRROCESSING ******************************************

#*****************************  TRAINING MODEL ******************************************

dbfile = open('TrainingData','rb')
x_train = np.array(pickle.load(dbfile))
dbfile.close()

dbfile = open('TrainingLabels','rb')
y_train = np.array(pickle.load(dbfile))
dbfile.close()

dbfile = open('TestingData','rb')
x_test = np.array(pickle.load(dbfile))
dbfile.close()

dbfile = open('TestingLabels','rb')
y_test = np.array(pickle.load(dbfile))
dbfile.close()


model = Sequential()



model.add(Conv2D(16, (3,3), activation = 'relu',input_shape = (70, 70, 1)))
model.add(Conv2D(16, (3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Conv2D(16, (3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(2,activation = 'softmax'))

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(x_train , y_train , batch_size = 16, epochs = 15, validation_split = 0.1 )

model.save("I_C.h5")

model.summary()

# test_loss,test_acc = model.evaluate(x_test,y_test)

# print("Accuracy",test_acc*100," %")

# prediction = model.predict(x_test)

# for i in range(25,30):
# 	plt.grid(False)
# 	plt.imshow(x_test[i],cmap='gray')
# 	plt.xlabel("Actual   :"+Folder[y_test[i]])
# 	plt.title("Prediction   :"+Folder[np.argmax(prediction[i])])
#	plt.show()

# TESTING MODEL

# model = keras.models.load_model("ImageClassification.model")

# model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

# dbfile = open('TestingData','rb')
# x_test = np.array(pickle.load(dbfile))
# dbfile.close()


# dbfile = open('TestingLabels','rb')
# y_test = np.array(pickle.load(dbfile))
# dbfile.close()


# prediction = model.predict([x_test])

# for i in range(25,30):
# 	print("Actual   :",Folder[y_test[i]])
# 	print("Prediction   :",Folder[np.argmax(prediction[i])])


# path = os.path.join(cur_path , "Test_imgs")#opens the folder Dogs in the current directory


# for img in os.listdir(path):#loading images inside the folder Dogs
# 	try:
# 		image = cv2.imread(os.path.join(path,img), 0)
# 	except Exception as e:
# 		pass

# 	if image is None:
# 		continue
# 	image = cv2.resize(image,(70,70))

# 	x_test.append(image)
# 	y_test.append(image)

# x_test = np.array(x_test)
# x_test = x_test/255
# x_test = np.array(x_test).reshape(-1 , 70 , 70 , 1)

# prediction = model.predict([x_test])

# for i in range(len(x_test)):
# 	plt.grid(False)
# 	plt.imshow(y_test[i],cmap='gray')
# 	plt.title("Prediction   :"+Folder[np.argmax(prediction[i])])
# 	plt.show()





