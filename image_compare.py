from PIL import Image
from PIL import ImageChops
import math



def compare(file1, file2):
	image1 = Image.open(file1).convert('L') # load image as grayscale
	image2 = Image.open(file2).convert('L')
	diff = ImageChops.difference(image1, image2) # compute absolute difference
	h = diff.histogram() # organize the data into a list
	sq = (value*(idx**2) for idx, value in enumerate(h))  # list comprehension -- note 256 different intensities (value)
	sum_of_squares = sum(sq)
	rms = math.sqrt(sum_of_squares/float(image1.size[0] * image1.size[1])) # compute root mean square
	return rms




file1 = 'images/image_1.png'
file2 = 'images/true1.png'
file3 = 'images/true3.png'

print compare(file1,file2) # it works!
print compare(file1,file1)
print compare(file3,file1)
print compare(file1,file3)  #symmetry
x = compare(file1,file2) + compare(file2,file3)  #subadditivity
print x