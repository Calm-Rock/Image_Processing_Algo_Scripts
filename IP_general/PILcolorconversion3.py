''' convert() operator is used for color conversion
'''

from PIL import Image

pil_im = Image.open('empire.jpg').convert('L')

# L converts to gray scale
