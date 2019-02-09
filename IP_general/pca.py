def pca(X):
  """  Principal Component Analysis
    input: X, matrix with training data stored as flattened arrays in rows
    return: projection matrix (with important dimensions first), variance
    and mean."""

  # get dimensions
  num_data,dim = X.shape

  # center data
  mean_X = X.mean(axis=0)
  X = X - mean_X

  if dim>num_data:
    # PCA - compact trick used
    M = dot(X,X.T) # covariance matrix
    e,EV = linalg.eigh(M) # eigenvalues and eigenvectors
    tmp = dot(X.T,EV).T # this is the compact trick
    V = tmp[::-1] # reverse since last eigenvectors are the ones we want
    S = sqrt(e)[::-1] # reverse since eigenvalues are in increasing order
    for i in range(V.shape[1]):
      V[:,i] /= S
  else:
    # PCA - SVD used
    U,S,V = linalg.svd(X)
    V = V[:num_data] # only makes sense to return the first num_data

  # return the projection matrix, the variance and the
  mean
  return V,S,mean_X


'''
EXPLATION
This function first centers the data by subtracting the mean in each
dimension. Then the eigenvectors corresponding to the largest eigenvalues
of the covariance matrix are computed, either using a compact trick or
using SVD. Here we used the function range(), which takes an integer n
and returns a list of integers 0 . . . (n – 1).

We switch from SVD to use a trick with computing eigenvectors of the
(smaller) covariance matrix XXT if the number of data points is less than
the dimension of the vectors.

The rows of the matrix V are orthogonal and contain the coordinate
directions in order of descending variance of the training data.

NOTE:The first principal component will have highest variance and the
variance will go on decreasing.
'''
