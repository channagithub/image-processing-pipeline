# Image Loading Code used for these examples
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from GPSPhoto import gpsphoto

class image_augmentation():
	def __init__(self, img):
    	self.img = img
    
    def flip_img(self):
	    # Flipping images with Numpy
		flipped_img = np.fliplr(self.img)

	def shift_left(self, HEIGHT = 1, WIDTH = 2):
		for i in range(HEIGHT, 1, -1):
			for j in range(WIDTH):
				if (i < HEIGHT-20):
					self.img[j][i] = self.img[j][i-20]
				elif (i < HEIGHT-1):
					self.img[j][i] = 0

	def shift_right(self, HEIGHT = 1, WIDTH = 2):
		for j in range(WIDTH):
			for i in range(HEIGHT):
				if (i < HEIGHT-20):
					self.img[j][i] = self.img[j][i+20]

	def shift_down(self, HEIGHT = 1, WIDTH = 2):
		for j in range(WIDTH, 1, -1):
			for i in range(278):
				if (j < 144 and j > 20):
					self.img[j][i] = self.img[j-20][i]

	def add_noise(self, WIDTH = 1, HEIGHT = 1, DEPTH = 1):
		noise = np.random.randint(5, size = (164, 278, 4), dtype = 'uint8')

		for i in range(WIDTH):
			for j in range(HEIGHT):
				for k in range(DEPTH):
					if (self.img[i][j][k] != 255):
						self.img[i][j][k] += noise[i][j][k]

	def get_geo_location(self):
		# Get the data from image file and return a dictionary
		data = gpsphoto.getGPSData(self.img)
		return (data['Latitude'], data['Longitude'])

    def show_img(self):
        temp_img = Image.open(self.img)
		temp_img = np.array(temp_img)
		plt.imshow(temp_img)
		plt.show()

		