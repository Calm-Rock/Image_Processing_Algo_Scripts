'''This file contains generally useful routeins'''

#This function creates a list of filenames of all images in the folder

import os

def get_imlist(path):
  """  Returns a list of filenames for
    all jpg images in a directory. """

  return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.png')]

get_imlist("C:\\Users\\lenovo\\Desktop\\Awesomeness\\Dream")

# Use \\ while defining the path.
#Avoide naming folders with spaces.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#The following code will load an image from a file image.png and will display it as grayscale.
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

fname = 'image.png'
image = Image.open(fname).convert("L")
arr = np.asarray(image)
#Instead, we can use arr = array(Image.open('filename').convert("L")) , this doesn't need numpy
plt.imshow(arr, cmap='gray')
plt.show()
#If you want to display the inverse grayscale, switch the cmap to cmap='gray_r'.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Simple image resizing using PIL image object conversion
def imresize(im,sz):
  """  Resize an image array using PIL. """
  pil_im = Image.fromarray(uint8(im))

  return array(pil_im.resize(sz))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#This code uses histogram equilibrium.

def histeq(im,nbr_bins=256):
  """  Histogram equalization of a grayscale image. """

  # get image histogram
  imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
  cdf = imhist.cumsum() # cumulative distribution function
  cdf = 255 * cdf / cdf[-1] # normalize

  # use linear interpolation of cdf to find new pixel values
  im2 = interp(im.flatten(),bins[:-1],cdf)
  return im2.reshape(im.shape), cdf

#To run is, use the below code inthe file you want to run
'''from PIL import Image
from numpy import *
import run as ru
from pylab import *

im = array(Image.open('filename').convert('L'))
im2,cdf = ru.histeq(im)
#print(cdf)
imshow(im2,cmap='gray')#To show the image

figure()
hist(im2.flatten(),128) #Shows histogram
show()
'''

#Averaging images

def compute_average(imlist):
  """  Compute the average of a list of images. """

  # open first image and make into array of type float
  averageim = array(Image.open(imlist[0]), 'f')

  for imname in imlist[1:]:
    try:
      averageim += array(Image.open(imname))#Adding the images to the frist image
    except:
      print imname + '...skipped'  #Prints this when image can't be opened.
  averageim /= len(imlist)   #Dividing by number of images

  # return average as uint8
  return array(averageim, 'uint8')
