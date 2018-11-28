# Created on Nov 27 2018
# @shadow236

import numpy as np

# a, generate 1D array that consist of 5 integers
a1 = np.array([2, 4, 6, 8, 10])
print("Numbers in a1 are stored using data type", a1.dtype)

# b, change data type to float with 32 bit
a1 = np.float32(a1)
print("Numbers in a1 are now stored using data type", a1.dtype)

# c, generate a 2D array of size 3x2. Output number of dimensions, rows and columns
a2 = np.array([[1, 2], [3, 4], [5, 6]])
print("a2=", a2)
print("number of dimensions of a2:", a2.ndim)
print("number of rows of a2:", np.size(a2, 0))
print("number of columns of a2:", np.size(a2, 1))

# d, how much bytes are used to store a single array element of a2 and
# how much bytes are used in total
print("nr of bytes needed to store one a2 array elements:", a2[0].nbytes)
print("nr of bytes needed to store all a2 array elements:", a2.nbytes)

# e, Generate the following 3D array a3.  Also output the number of dimensions of a3
# and the size of each dimension
a3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])
print("a3=", a3)
print("number of dimensions of a3:", a3.ndim)
print("number of slices of a3:", np.size(a3, 0))
print("number of rows of a3:", np.size(a3, 1))
print("number of columns of a3:", np.size(a3, 2))

"""
Exercise 03 - Accessing array elements
"""

# a, get and output the value of the element of a3 in the second slice, third row, fourth column
print("Value of that element is", a3[1, 2, 3])

# b, change the value of that element to 42 and output the value again by retrieving the value
# at that position from array a3
a3[1, 2, 3] = 42
print("Value of that element now", a3[1, 2, 3])

# c, store the first slice from the 3D array a3 in a new 2D array a4 and output it
a4 = a3[0, :, :]
print("a4=", a4)

# d, now retrieve from a4 the third column as a 1D array a5 and output it
a5 = a4[:, 2]
print("a5=", a5)

# e, retrieve from a4 the second row as a 1D array a6 and output it
a6 = a4[1, :]
print("a6=", a6)

# f, retrieve from a4 the following 2x2 sub-matrix
a7 = a4[1:3, 1:3]
print("a7=", a7)

"""
Exercise 04 - Reshaping array
"""

# a, generate the following 1D array A. Then reshape it to a 2D array B with 2 rows and 5 columns
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
B = A.reshape(2, 5)
print("A=", A)
print("B=", B)

# c, reshape the 2D array B to a 2D array C with 5 rows and 2 columns
C = B.reshape(5, 2)
print("C=", C)
