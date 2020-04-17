import cv2
import os
import numpy as np

cur_dir = os.path.dirname(__file__)

cur_dir = os.path.join(cur_dir,'Train_IMG')

Folder = ['A','H','I','M','T','U','V','W','X','Y']

for i in Folder:
	path = os.path.join(cur_dir,i)
	for x,img in enumerate(os.listdir(path)):
		image = cv2.imread(os.path.join(path,img),0)
		if image is None:
			continue
		image = cv2.flip(image,1)
		cv2.imwrite(os.path.join(path,"f{}.png".format(x)),image)