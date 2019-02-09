''' crop() is used to crop a region from image.
'''
from PIL import Image


pil_im = Image.open('test.jpg')
box = (100,100,800,800) #The tuple represents (left, upper, right, lower) co-ordinates
region = pil_im.crop(box)

#PIL uses a coordinate system with (0,0) in upper left corner.

'''paste() helps in placing back the image.
'''
#This code rotates the cropped image and pastes it on the original image.
region = region.rotate(180)
pil_im.paste(region,box)
# pil_im.show()      #this shows the image
pil_im.save("C:\\Users\\lenovo\\Desktop\\Awesomeness\\newimage.png")


