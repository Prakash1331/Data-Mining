# Importing the NumPy module
import numpy as np

# I. Create a List
my_list = [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]

# II. Iterate using a for loop
print("II. Iterating using a for loop:")
for item in my_list:
    print(item)

# III. Iterate using a for loop and range
print("\nIII. Iterating using a for loop and range:")
for i in range(len(my_list)):
    print(my_list[i])

# IV. List Comprehension
print("\nIV. List comprehension:")
squared_list = [x ** 2 for x in my_list]
print(squared_list)

# V. Enumerate
print("\nV. Enumerate:")
for index, value in enumerate(my_list):
    print(f"Index {index}: Value {value}")

# VI. Iter function and next function
print("\nVI. Iter function and next function:")
my_iterator = iter(my_list)
print(next(my_iterator))  # Get the first element
print(next(my_iterator))  # Get the second element

# VII. Map function
print("\nVII. Map function:")
doubled_list = list(map(lambda x: x * 2, my_list))
print(doubled_list)

# VIII. Using zip
print("\nVIII. Using zip:")
# Create another list for zipping
another_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
zipped_list = list(zip(my_list, another_list))
print(zipped_list)

# IX. Using NumPy Module
print("\nIX. Using NumPy Module:")
np_array = np.array(my_list)
print("NumPy Array:", np_array)
print("Array Mean:", np.mean(np_array))
print("Array Sum:", np.sum(np_array))
print("Array Standard Deviation:", np.std(np_array))
