import cv2
import os
import matplotlib.pyplot as plt 
import random
import numpy as np
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten,Dropout
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
import random
import pickle


cur_dir = os.path.dirname(__file__)
# cur_dir = os.path.join(cur_dir,'Train_IMG')

# Folder = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# x_train = []
# y_train = []

# for x,i in enumerate(Folder):
# 	path = os.path.join(cur_dir,i)
# 	for img in os.listdir(path):
# 		image = cv2.imread(os.path.join(path,img),0)

# 		if image is None:
# 			continue
# 		image = cv2.resize(image,(28,28))

# 		x_train.append(image)
# 		y_train.append(x)

# temp = list(zip(x_train,y_train))
# random.shuffle(temp)
# x_train,y_train = zip(*temp)

# for i in range(35,75):
# 	plt.grid(False)
# 	plt.imshow(x_train[i],cmap='gray')
# 	plt.title(chr(y_train[i]+65))
# 	plt.show()

# dbfile = open('TrainingData','ab')
# pickle.dump(x_train,dbfile)
# dbfile.close()

# dbfile = open('TrainingLabels','ab')
# pickle.dump(y_train,dbfile)
# dbfile.close()







dbfile = open('TrainingData','rb')
x_train = np.array(pickle.load(dbfile))
dbfile.close()

dbfile = open('TrainingLabels','rb')
y_train = np.array(pickle.load(dbfile))
dbfile.close()

# for i in range(15):
# 	plt.grid(False)
# 	plt.imshow(x_train[i],cmap='gray')
# 	print(chr(y_train[i]+65))
# 	plt.show()

x_train = np.array(x_train).reshape(-1, 28 , 28, 1).astype('float32')
x_train/= 255


model = Sequential()
model.add(Conv2D(32, (5, 5), input_shape=(28, 28, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(26, activation='softmax'))

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

# cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,save_weights_only=True,verbose=1)
# model.load_weights(checkpoint)

model.fit(x_train , y_train , batch_size = 200, epochs = 1, validation_split = 0.1)

model.save("A_Z5.h5")

model.summary()







#TESTING MODEL

# x_test = []
# cur_dir = os.path.dirname(__file__)

# path = os.path.join(cur_dir,'Test_imgs')


# for img in os.listdir(path):
# 	image = cv2.imread(os.path.join(path,img),0)
# 	if image is None:
# 		continue
# 	image = cv2.resize(image,(28,28))
# 	x_test.append(image)

# y_test = x_test

# x_test = np.array(x_test)

# x_test = np.array(x_test).reshape(-1 , 28 , 28 , 1).astype('float32')
# x_test = x_test/255

# model = keras.models.load_model("A_Z3.h5")

# model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

# prediction = model.predict(x_test)

# for i in range(len(x_test)):
# 	plt.grid(False)
# 	plt.imshow(y_test[i], cmap='gray')
# 	p = np.argmax(prediction[i])
# 	prob = prediction[i][p]
# 	plt.title("Prediction : "+chr(p+65)+"  ( "+("%.2f"%(prob*100))+" % )")
# 	plt.show()






