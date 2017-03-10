import PIL
from PIL import Image
from matplotlib import pyplot as plt
from PIL import ImageChops

i = Image.open('images/image_1.png').convert('L')
#i = Image.open('images/fry.jpg').convert('L') 
i.show()
h = i.histogram()

N = 256

plt.hist(h,N,[0,N])
plt.show()










# file1 = 'images/image_1.png'
# file2 = 'images/true1.png'
# file3 = 'images/true3.png'

# image1 = Image.open(file1).convert('L') # load image as grayscale
# image2 = Image.open(file2).convert('L')
# image3 = Image.open(file3).convert('L')

# diff1 = ImageChops.difference(image1,image2) # compute absolute difference
# diff2 = ImageChops.difference(image1,image3) # compute absolute difference


# h1 = diff1.histogram()
# h2 = diff2.histogram()

# N = 15

# plt.hist(h1,N,[0,N]); plt.show(block=False) 
# plt.hist(h2,N,[0,N]); plt.show()