import numpy as np
import numpy.linalg as la

verySmallNumber = 1e-14 # That's 1×10⁻¹⁴ = 0.00000000000001

# first function will perform the Gram-Schmidt procedure for 4 basis vectors.
# take this list of vectors as the columns of a matrix, A.
# then go through the vectors one at a time and set them to be orthogonal
# to all the vectors that came before it. Before normalising.
def gsBasis4(A) :
    B = np.array(A, dtype=np.float32) # Make B as a copy of A, since we're going to alter it's values.
    # All that needs is to normalise it. Divide by its modulus, or norm.
    B[:, 0] = B[:, 0] / la.norm(B[:, 0])
    # For the first column, subtract any overlap with our new zeroth vector.
    B[:, 1] = B[:, 1] - B[:, 1] @ B[:, 0] * B[:, 0]
    # If there's anything left after that subtraction, then B[:, 1] is linearly independant of B[:, 0]
    # If this is the case, we can normalise it. Otherwise set that vector to zero.
    if la.norm(B[:, 1]) > verySmallNumber :
        B[:, 1] = B[:, 1] / la.norm(B[:, 1])
    else :
        B[:, 1] = np.zeros_like(B[:, 1])
    B[:, 2] = B[:, 2] - B[:, 2] @ B[:, 0] * B[:, 0]
    B[:, 2] = B[:, 2] - B[:, 2] @ B[:, 1] * B[:, 1]
    if la.norm(B[:, 2]) > verySmallNumber :
        B[:, 2] = B[:, 2] / la.norm(B[:, 2])
    else :
        B[:, 2] = np.zeros_like(B[:, 2])
    B[:, 3] = B[:, 3] - B[:, 3] @ B[:, 0] * B[:, 0]
    B[:, 3] = B[:, 3] - B[:, 3] @ B[:, 1] * B[:, 1]
    B[:, 3] = B[:, 3] - B[:, 3] @ B[:, 2] * B[:, 2]
    if la.norm(B[:, 3]) > verySmallNumber :
        B[:, 3] = B[:, 3] / la.norm(B[:, 3])
    else :
        B[:, 3] = np.zeros_like(B[:, 3])
    return B

# We'll use a for-loop here to iterate the process for each vector.
def gsBasis(A) :
    B = np.array(A, dtype=np.float32) # Make B as a copy of A, since we're going to alter it's values.
    # Loop over all vectors, starting with zero, label them with i
    for i in range(B.shape[1]) :
        # Inside that loop, loop over all previous vectors, j, to subtract.
        for j in range(i) :
            B[:, i] = B[:, i] - B[:, i] @ B[:, j] * B[:, j]
        # normalisation test for B[:, i]
        if la.norm(B[:, i]) > verySmallNumber :
            B[:, i] = B[:, i] / la.norm(B[:, i])
        else :
            B[:, i] = np.zeros_like(B[:, i])
    return B


def dimensions(A) :
    return np.sum(la.norm(gsBasis(A), axis=0))

V = np.array([[1,0,2,6],
              [0,1,8,2],
              [2,8,3,1],
              [1,-6,2,3]], dtype=np.float32)
gsBasis4(V)

U = gsBasis4(V)
gsBasis4(U)
gsBasis(V)

A = np.array([[3,2,3],
              [2,5,-1],
              [2,4,8],
              [12,2,1]], dtype=np.float32)
gsBasis(A)
dimensions(A)

B = np.array([[6,2,1,7,5],
              [2,8,5,-4,1],
              [1,-6,3,2,8]], dtype=np.float32)
gsBasis(B)
dimensions(B)


C = np.array([[1,0,2],
              [0,1,-3],
              [1,0,2]], dtype=np.float32)
gsBasis(C)
dimensions(C)