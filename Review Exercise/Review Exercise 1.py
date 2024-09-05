# Define matrices
A = [[3.7827, 3.3454, 3.2341], [2.2122, 3.5678, 3.9087], [1.1234, 2.8934, 5.9087]]
B = [[3.1234, 3.0987, 3.1234], [2.1111, 3.2222, 3.3333], [1.0987, 1.3456, 5.1234]]
C = [[3.1243, 3.0989, 3.1256], [2.6721, 3.6785, 3.9017], [1.1254, 2.8956, 5.9187]]

# Matrix addition
def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Matrix subtraction
def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Element-wise multiplication
def multiply_matrices(A, B):
    return [[A[i][j] * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Performing operations
sum_AB = add_matrices(A, B)
diff_AB = subtract_matrices(A, B)
prod_AB = multiply_matrices(A, B)

print("Sum of A and B:")
for row in sum_AB:
    print(row)

print("\nDifference of A and B:")
for row in diff_AB:
    print(row)

print("\nProduct of A and B:")
for row in prod_AB:
    print(row)

import numpy as np

# Define matrices using NumPy arrays
A = np.array([[3.7827, 3.3454, 3.2341], [2.2122, 3.5678, 3.9087], [1.1234, 2.8934, 5.9087]])
B = np.array([[3.1234, 3.0987, 3.1234], [2.1111, 3.2222, 3.3333], [1.0987, 1.3456, 5.1234]])
C = np.array([[3.1243, 3.0989, 3.1256], [2.6721, 3.6785, 3.9017], [1.1254, 2.8956, 5.9187]])

# Matrix addition
sum_AB = A + B

# Matrix subtraction
diff_AB = A - B

# Element-wise multiplication
prod_AB = A * B

print("Sum of A and B:")
print(sum_AB)

print("\nDifference of A and B:")
print(diff_AB)

print("\nProduct of A and B:")
print(prod_AB)
