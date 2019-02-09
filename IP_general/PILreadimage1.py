'''
> PIL(Pillow for 3.x) stands for Python Imaging Library
> It provides basic image operaations like resizing, rotating etc.
> With PIL, you can read images from most formats and write to
   the most common ones.'''


from PIL import Image
#To read an image image
pil_im = Image.open('empire.jpg') #The return value pil_im is a PIL 'image object'

#To show the image
pil_im.show()
#.show() is needed to show an image
#Image.open() just reads the image.


