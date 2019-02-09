'''
> Pickle  module helps us save some result or data for later use.
> Pickle takes a python object and converts it to a string representation.
 This is called pickling and the reverse is called unpickling.
> This string representation can easily be stored or transmitted.
'''

#Example

# save mean and principal components
f = open('font_pca_modes.pkl', 'wb')
pickle.dump(immean,f)
pickle.dump(V,f)
f.close()

# > several objects can be pickled to the same file.
# > There are several different protocols available for the .pkl files,
# and if unsure, it is best to "read and write binary"files (rb , wb).

#To load the data in some other Python session, just use the load() method like this:

# load mean and principal components
f = open('font_pca_modes.pkl', 'rb')
immean = pickle.load(f)
V = pickle.load(f)
f.close()
# Note that the order of the objects should be the same!

'''
with statement to handle file reading and writing.
This is a construct that was introduced in Python 2.5 that
automatically handles opening and closing of files
(even if errors occur while the iles are open). Here is what the saving
and loading above looks like using with():
'''
# open file and save
with open('font_pca_modes.pkl', 'wb') as f:
  pickle.dump(immean,f)
  pickle.dump(V,f)
  
  #and
  
# open file and load
with open('font_pca_modes.pkl', 'rb') as f:
  immean = pickle.load(f)
  V = pickle.load(f)

  '''
If your data does not contain complicated structures, for example
a list of points clicked in an image. To save an array x to file, use:
'''
savetxt('test.txt',x,'%i')
#The last parameter indicates that integer format should be used. Similarly,
#reading is done like this:

x = loadtxt('test.txt')
  
