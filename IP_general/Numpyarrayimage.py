'''
> NumPy is a scientific computing package.
> NumPy arrays are used for representing vectors, matrices, images etc
> Array objects lets you do matrix multiplication, transposition, vector
multiplication, solving equation systems and normalization which are needed
to do things like aligning images, wraping images, classifying images,
grouping images etc.

> Arrays in NumPy are multi-dimensional and can represent vectors,
matrices, and images.
> An array is much like a list (or list of lists) but is restricted to having all
elements of the same type.
Unless specified on creation, the type will automatically be set depending
on the data.
'''

from PIL import Image
from pylab import *
import numpy as np

im = array(Image.open('test.jpg'))
print(im.shape,im.dtype)
# The im.shape gives detail about shape of image array (rows, column, color channel)
#im.dtype gives data type of that array.
#Images are generally encoded with, unsigned 8-bit integers (uint8) so this gives the array the type uint8

im = array(Image.open('empire.jpg').convert('L'),'f')
print(im.shape,im.dtype)
#The f argument is short command for setting the type to floating point.
#The grayscale image won't have any color channel information.

