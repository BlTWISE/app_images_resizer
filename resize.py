import PIL
from PIL import Image

imageSizes = [167, 152, 76, 29, 20, 180, 120, 80, 87, 58, 60, 40, 1024]


img = Image.open('1024x1024.png') #Open base image

for imgSize in imageSizes: #Iterate through different sizes
    img2 = img.copy() #Create copy of base image
    img2.thumbnail((imgSize,imgSize), PIL.Image.ANTIALIAS) #Make base image smaller while keeping 1:1 aspect ratio
    img2.save(str(imgSize) + 'x' + str(imgSize) + '.png', quality = 100) #Save the image and name it according to its size
