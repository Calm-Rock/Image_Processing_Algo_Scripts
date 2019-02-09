'''
> PIL(Pillow for 3.x) stands for Python Imaging Library
> It provides basic image operaations like resizing, rotating etc.
> With PIL, you can read images from most formats and write to
   the most common ones.'''

#To read an image image
from PIL import Image

pil_im = Image.open('empire.jpg')

pil_im.show()
#.show() is needed to show an image
#Image.open() just reads the image.


