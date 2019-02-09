''' resize() along with a tuple is used for resizing images.
'''

from PIL import Image

pil_im = Image.open('empire.jpg')

out = pil_im.resize((128,128))

''' to rotate an image, use rotate()
'''

out1 = pil_im.rotate(45).show()
#It rotates counterclockwise, for clockwise, use -ve values.
