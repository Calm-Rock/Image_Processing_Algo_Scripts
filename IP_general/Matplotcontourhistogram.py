'''
Visualizing image contour can be very helpful.
To visualize it, we need grayscale images, because the contour need
to be taken on a single value for every co-ordinate [x,y]
'''

from pylab import *
from PIL import Image

im = array(Image.open('test.jpg').convert('L'))      #Convert to grayscale  and read
'''a grayscale or greyscale image is one in which the value of each pixel
is a single sample representing only an amount of light, that is, it carries
only intensity information.'''
imshow(im, cmap='gray')       #If we don't use cmap = 'gray', we will get a color map
show()

figure()     #Creates a new figure so that original image is not disturbed        #Don't use color
'''show()''' # This shows that we created a new empty figure
gray()
contour(im, origin='image')   #"Shows" contour with origin in upper left corner
# Instead of using gray(), we can use cmap = 'gray' in contour function

axis('equal')
axis('off')

'''
An image histogram is a plot showing the distribution of pixel values.
A number of bins is specified for the span of values and each bin gets a
count of how many pixels have values in the bin’s range.
'''
figure()
hist(im.flatten(),564)
'''
> To visualise the graylevel image histogram, we use the hist() function.
> The 2nd argument of the his function specifies teh number of bins to be used.
> hist() takes a 1-D array as input, so flatten() converts any array to 1-D array with values
taken row wise'''

show()
