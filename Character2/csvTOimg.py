import numpy as np
import csv
from PIL import Image    
import matplotlib.pyplot as plt
import os

counter = dict()
cur_path = os.path.dirname(__file__)


k = 0
with open('Data.csv') as csv_file:
	csv_reader = csv.reader(csv_file)
	next(csv_reader)

	for row in csv_reader:
		k+=1
		pixels = row[:-1] # without label
		pixels = np.array(pixels, dtype='float')
		pixels = pixels.reshape((28, 28))

		label = row[-1]



		if label not in counter:
			counter[label] = 0
		counter[label] += 1

		
		if k > 74445 and k <= 81663:
			path = os.path.join(cur_path,'H')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 81663 and k <= 82783:
			path = os.path.join(cur_path,'I')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 82783 and k <= 91276:
			path = os.path.join(cur_path,'J')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k >91276 and k <= 96879:
			path = os.path.join(cur_path,'K')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 96879 and k <= 108465:
			path = os.path.join(cur_path,'L')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 108465 and k <= 120801:
			path = os.path.join(cur_path,'M')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 120801 and k <= 139811:
			path = os.path.join(cur_path,'N')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 139811 and k <= 197636:
			path = os.path.join(cur_path,'O')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 197636 and k <= 216977:
			path = os.path.join(cur_path,'P')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 216977 and k <= 222789:
			path = os.path.join(cur_path,'Q')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 222789 and k <= 234355:
			path = os.path.join(cur_path,'R')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 234355 and k <= 282744:
			path = os.path.join(cur_path,'S')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 282744 and k <= 305269:
			path = os.path.join(cur_path,'T')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 305269 and k <= 334277:
			path = os.path.join(cur_path,'U')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 334277 and k <= 338459:
			path = os.path.join(cur_path,'V')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 338459 and k <= 349245:
			path = os.path.join(cur_path,'W')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 349245 and k <= 355517:
			path = os.path.join(cur_path,'X')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 355517 and k <= 366376:
			path = os.path.join(cur_path,'Y')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)
		elif k > 366376:
			path = os.path.join(cur_path,'Z')
			filename = '{}{}.png'.format(label, counter[label])
			path = os.path.join(path,filename)
			plt.imsave(path, pixels)


