import numpy as np

# function will go through the matrix replacing each row in order turning it into echelon form.
# If at any point it fails because it can't put a 1 in the leading diagonal,
# return the value True, otherwise, we will return False.


def isSingular(A) :
    B = np.array(A, dtype=np.float32) # Make B as a copy of A, since we're going to alter it's values.

    try:
        fixRowZero(B)
        fixRowOne(B)
        fixRowTwo(B)
        fixRowThree(B)
    except MatrixIsSingular:
        return True
    
    return False

# This next line defines our error flag. For when things go wrong if the matrix is singular.
class MatrixIsSingular(Exception): pass
# For Row Zero, all required is the first element is equal to 1.
# divide the row by the value of A[0, 0].
# if A[0, 0] equals 0 it can be problematic, so first test for that,
# if this is true, add one of the lower rows to the first one before the division.
# repeat the test going down each lower row until we can do the division.
def fixRowZero(A) :

    if A[0,0] == 0 :
        A[0] = A[0] + A[1]

    if A[0,0] == 0 :
        A[0] = A[0] + A[2]

    if A[0,0] == 0 :
        A[0] = A[0] + A[3]

    if A[0,0] == 0 :
        raise MatrixIsSingular()
    A[0] = A[0] / A[0,0]
    return A

# set the sub-diagonal elements to zero, i.e. A[1,0].
# Next we want the diagonal element to be equal to one.
# divide the row by the value of A[1, 1].
# Again, we need to test if this is zero.
# If so, add a lower row and repeat setting the sub-diagonal elements to zero.

def fixRowOne(A) :

    A[1] = A[1] - A[1,0] * A[0]

    if A[1,1] == 0 :
        A[1] = A[1] + A[2]
        A[1] = A[1] - A[1,0] * A[0]

    if A[1,1] == 0 :
        A[1] = A[1] + A[3]
        A[1] = A[1] - A[1,0] * A[0]

    if A[1,1] == 0 :
        raise MatrixIsSingular()
    A[1] = A[1] / A[1,1]

    return A
def fixRowTwo(A) :
    A[2] = A[2] - A[2,0] * A[0]
    A[2] = A[2] - A[2,1] * A[1]
    # Next we'll test that the diagonal element is not zero.
    if A[2,2] == 0 :
        A[2] = A[2] + A[3]
        A[2] = A[2] - A[2,0] * A[0]
        A[2] = A[2] - A[2,1] * A[1] 
    if A[2,2] == 0 :
        raise MatrixIsSingular()
    # set the diagonal element to one by dividing the whole row by that element.
    A[2] = A[2] / A[2,2]
    return A

def fixRowThree(A) :
    A[3] = A[3] - A[3,0] * A[0]
    A[3] = A[3] - A[3,1] * A[1]
    A[3] = A[3] - A[3,2] * A[2]

    if A[3,3] == 0 :
        raise MatrixIsSingular()

    # Transform the row to set the diagonal element to one.
    A[3] = A[3] / A[3,3]
    return A

A = np.array([
        [2, 0, 0, 0],
        [0, 3, 0, 0],
        [0, 0, 4, 4],
        [0, 0, 5, 5]
    ], dtype=np.float32)
isSingular(A)

A = np.array([
        [0, 7, -5, 3],
        [2, 8, 0, 4],
        [3, 12, 0, 5],
        [1, 3, 1, 3]
    ], dtype=np.float32)

fixRowZero(A)
fixRowOne(A)
fixRowTwo(A)
fixRowThree(A)