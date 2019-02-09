'''
To interact with an application and to annotate (add notes to
(a text or diagram) giving explanation or comment.) data, PyLab comes
with a simple function "ginput()" to do so.
'''
import numpy as np
from PIL import Image
from pylab import *

im = array(Image.open('empire.jpg'))
imshow(im) # plots the image
#print ('Please click 5 points')

a = ginput(5)# Waits for the user to click 5 times in the image region.
# ginput(n = -1, timeout = 10, show_clicks = True )
#n = -ve takes infinite inputs until closed manually
#timeout is the amount for which the window remains open, default is 30, 0 or -ve will never timeout
# show_click = True will show a cross mark on every poin we clicked.

print ('You Clicked', a)

#savefig('foo.png') #saves your plot.
#print (a)
savetxt('qwenew.txt',a,'%i') # %i converts it to integer values
show() #Saves your clicked value in whichever format you want it to.
#Co-ordinates (x,y) are saved in a list.

show()
