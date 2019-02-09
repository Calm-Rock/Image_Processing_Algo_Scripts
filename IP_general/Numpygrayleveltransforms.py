'''
> We can perform any mathematical operation on images after reading them
   on numpy array.
> For example, we can transform the graylevel of the image.

> Take any function f that maps the interval 0 . . . 255 (or, if you like, 0 . . . 1)
to itself (meaning that the output has the same range as the input).
'''
from scipy import misc
from PIL import Image
from numpy import *
from pylab import *
im = array(Image.open('empire.jpg').convert('L'))

im2 = 255 - im #invert image

im3 = (100.0/255) * im + 100  #Clamp to interval 100...200

im4 = 255.0 * (im/255)**2   #Squared#Lowers the value of darker pixels
# A pixel value of 122.5 qill become 255/4 and hence lowered by great amount.

a = im.min()
b = im.max()  #Similarly for im2,im3 and im4.
print (a, b)

print(im4.dtype)
figure()
imshow(im2, cmap = 'gray')
#imshow(im4, cmap = 'gray')
axis('off')
'''savefig('foo.png')''' #Use this to save the image too, put this above show()

show()   #Use matplotlib to show the image

'''misc.imsave('outfile.png', im2)''' #Use this to save image array as image.


