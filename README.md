Project Structure

1. ReflectingImages.py
This script is designed to build a reflection matrix based on an orthonormal basis derived from a given basis. The key function build_reflection_matrix(bearBasis) constructs the transformation matrix used to reflect an image, in this case, a bear, along a specified basis.

Key Features:
Uses the Gram-Schmidt process to obtain an orthonormal basis.
Constructs and applies a reflection matrix to an image.
Visualizes both the original and reflected images using matplotlib.

3. GramSchmidtProcess.py
This script contains the implementation of the Gram-Schmidt process, which is used to orthogonalize a set of vectors in a matrix.

Key Functions:
gsBasis4(A): Performs the Gram-Schmidt process on 4 basis vectors.
gsBasis(A): Generalized function for performing Gram-Schmidt on any set of vectors.
dimensions(A): Computes the dimension of the space spanned by the given set of vectors.

4. IdentifyingSpecialMatrices.py
This script identifies whether a given matrix is singular by transforming it into its echelon form.

Key Functions:
isSingular(A): Determines if the matrix is singular by attempting to convert it into an echelon form.
fixRowZero, fixRowOne, fixRowTwo, fixRowThree: Helper functions that assist in the echelon form transformation.

5. PageRank.py
This script implements the PageRank algorithm, which is used to rank web pages based on their importance. It includes an implementation of the power iteration method to find the dominant eigenvector of a matrix, which corresponds to the PageRank of each page.

Key Features:
Implements the PageRank algorithm with damping to ensure convergence.
Compares the PageRank method with eigenvector computation.
Visualizes the PageRank results using bar charts.

Dependencies
This project relies on several Python libraries, including:
numpy: For numerical computations and matrix operations.
matplotlib: For plotting and visualizing images and data.
Custom modules like bearNecessities and PageRankFunctions (ensure these are available in your environment).

To install these dependencies, run:
pip install numpy matplotlib

Usage:
Clone the repository to your local machine.
Install the required dependencies using the command provided above.
Run each script individually using Python.

For example:
python ReflectingImages.py
