from PIL import Image
from PIL import ImageChops
 
def compare_images(path_one, path_two):
    """
    Compares to images and saves a diff image, if there
    is a difference
 
    @param: path_one: The path to the first image
    @param: path_two: The path to the second image
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
 
    diff = ImageChops.difference(image_one, image_two)
    diff.show()
   
 
if __name__ == '__main__':
    compare_images('images/fry1.jpg',
                   'images/fry2.jpg')