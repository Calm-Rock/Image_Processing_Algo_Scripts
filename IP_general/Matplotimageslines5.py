'''
>Matplotlib is used for plotting graphs, points, curves etc on images.
>Basically you can draw on image with this library.
>PyLab interface is the set of functions that allows the users to creat plots.

>Note that PyLab uses a coordinate origin at the top left corner as is common for images.
'''

from PIL import Image
from pylab import *

im = array(Image.open('empire.jpg')) #Reads the image to array

imshow(im)#plots the image, not show the image

x = [100,100,400,400]   #The x and y values shows the (x,y) values of 4 points
y = [200,500,200,500]

plot(x,y,'r*') # 'r*' is a formatting style while plotting, there are many such styles available
#The default one is a 'blue solid line'

plot(x[:2], y[:2])#Line plot connecting the first two points, wiht the default blue solid line

'''axis('off')''' # Removes the axis.
'''axis([1000,0,1000,0])''' # The axis() command above takes a list of [xmin, xmax, ymin, ymax]

title('Plotting: "empire.jpg"')#Adds title

show()#shows plot
'''The show() command starts the figure GUI and raises the figure windows.
This GUI loop blocks your scripts and they are paused until the last figure
window is closed. You should call show() only once per script, usually at the
end.'''
