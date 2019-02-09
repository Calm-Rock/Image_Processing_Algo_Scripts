'''
The reverse of array() transformation can be done using the PIL'
fromarray()
'''

pil_im = Image.fromarray(im)

'''
If we changed the dtype of the image by doing some operation like in
previous case im3 and im4, we need to convert back to uint8 before
creating PIL image
'''

pil_im = Image.fromarray(uint8(im))

#If you are not absolutely sure of the type of the input, you should
#do this as it is the safe choice

'''
> Note that NumPy will always change the array type to the “lowest” type
that can represent the data.

> Multiplication or division with floating point numbers will change an integer
type array to float.
'''
