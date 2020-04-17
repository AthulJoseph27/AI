import numpy as np
from PIL import Image    
import matplotlib.pyplot as plt
import os
import cv2

cur_dir = os.path.dirname(__file__)
cur_dir = os.path.join(cur_dir,'Train_IMG')

Folder = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in Folder:
	path = os.path.join(cur_dir,i)
	for x,img in enumerate(os.listdir(path)):
		image = cv2.imread(os.path.join(path,img),0)
		if image is None:
			continue
		image = 255-image
		cv2.imwrite(os.path.join(path,"{}i.png".format(x)) , image)


