
from matplotlib import pyplot as plt
import numpy as np
import numpy.linalg as la
from readonly.PageRankFunctions import *
import numpy as np
import numpy.linalg as la
from readonly.PageRankFunctions import *
np.set_printoptions(suppress=True)

L = np.array([[0,   1/2, 1/3, 0, 0,   0 ],
              [1/3, 0,   0,   0, 1/2, 0 ],
              [1/3, 1/2, 0,   1, 0,   1/2 ],
              [1/3, 0,   1/3, 0, 1/2, 1/2 ],
              [0,   0,   0,   0, 0,   0 ],
              [0,   0,   1/3, 0, 0,   0 ]])


eVals, eVecs = la.eig(L) # Gets the eigenvalues and vectors
order = np.absolute(eVals).argsort()[::-1] # Orders them by their eigenvalues
eVals = eVals[order]
eVecs = eVecs[:,order]

r = eVecs[:, 0] # Sets r to be the principal eigenvector
100 * np.real(r / np.sum(r)) # Make this eigenvector sum to one, then multiply by 100 Procrastinating Pats


r = 100 * np.ones(6) / 6 # Sets up this vector (6 entries of 1/6 × 100 each)
r # Shows it's value

r = L @ r # Apply matrix L to r
r # Show it's value
#Re-run the cell multiple times to get the correct answer

r = 100 * np.ones(6) / 6 # Sets up this vector (6 entries of 1/6 × 100 each)
for i in np.arange(100) : # Repeat 100 times
    r = L @ r
r

r = 100 * np.ones(6) / 6 # Sets up this vector (6 entries of 1/6 × 100 each)
lastR = r
r = L @ r
i = 0
while la.norm(lastR - r) > 0.01 :
    lastR = r
    r = L @ r
    i += 1
print(str(i) + " iterations to convergence.")
r



# Call this one L2, to distinguish it from the previous L.
L2 = np.array([[0,   1/2, 1/3, 0, 0,   0, 0 ],
              [1/3, 0,   0,   0, 1/2, 0, 0 ],
              [1/3, 1/2, 0,   1, 0,   1/2, 0 ],
              [1/3, 0,   1/3, 0, 1/2, 1/2, 0 ],
              [0,   0,   0,   0, 0,   0, 0 ],
              [0,   0,   1/3, 0, 0,   0, 0 ],
              [0,   0,   0,   0, 0,   0, 1 ]])


r = 100 * np.ones(7) / 7 # Sets up this vector (6 entries of 1/6 × 100 each)
lastR = r
r = L2 @ r
i = 0
while la.norm(lastR - r) > 0.01 :
    lastR = r
    r = L2 @ r
    i += 1
print(str(i) + " iterations to convergence.")
r


d = 0.5 
M = d * L2 + (1-d)/7 * np.ones([7, 7]) # np.ones() is the J matrix, with ones for each entry.

r = 100 * np.ones(7) / 7 # Sets up this vector (6 entries of 1/6 × 100 each)
lastR = r
r = M @ r
i = 0
while la.norm(lastR - r) > 0.01 :
    lastR = r
    r = M @ r
    i += 1
print(str(i) + " iterations to convergence.")
r


np.set_printoptions(suppress=True)


def pageRank(linkMatrix, d) :
    n = linkMatrix.shape[0]                                         
    M = (d * linkMatrix) + ((1-d) /n * np.ones([n, n]) )
    r = 100 * np.ones(n) / n
    lastR = r
    r = M @ r
    i = 0

    while la.norm(lastR - r) > 0.01 :
        lastR = r
        r = M @ r
        i += 1
    return r

# generate internets of different sizes.
generate_internet(5)

# Testing PageRank method against the built in "eig" method.
L = generate_internet(10)

pageRank(L, 1)

eVals, eVecs = la.eig(L) # Gets the eigenvalues and vectors
order = np.absolute(eVals).argsort()[::-1] # Orders them by their eigenvalues
eVals = eVals[order]
eVecs = eVecs[:,order]

r = eVecs[:, 0]
100 * np.real(r / np.sum(r))

r = pageRank(generate_internet(100), 0.9)
plt.bar(range(r.shape[0]), r)
