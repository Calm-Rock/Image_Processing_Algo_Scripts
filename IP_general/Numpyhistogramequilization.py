'''
Histogram equilization
 > This transform flattens the graylevel histogram of an image so that all
 intensities are as equally common as possible.

> This is often a good way to normalize image intensity before further
processing and also a way to increase image contrast.

>  The transform function is, in this case, a cumulative distribution function
   "(cdf) of the pixel values in the image " (normalized to map the range
   of pixel values to the desired range).
'''

#For code and applications, see the imtools.py file.
