import numpy as np

print(np.__version__)

arr = np.array(33)  # 0-D array
print(type(arr))
print(arr.dtype)
arr1 = np.array([1, 2, 3, 4, 5], dtype='i')  # 1-D array
# We can set the dimension with the help of ndmin
# 2-D array
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], ndmin=2)

print(f"0-D array : {arr}")
print(f"1-D array : {arr1[0]}")
print(f"2-D array : {arr2[1, 3]}")
print(f"Dimension of arr : {arr.ndim}")
print(f"Dimension of arr1 : {arr1.ndim}")
print(f"Dimension of arr2 : {arr2.ndim}")

print(arr1[::-1])
print(arr2[1, ::-1])
print(arr2[:, 2])
print(arr2[:, ::-1])

arr3 = np.array(['1', '2', '3'], dtype='U')
print(arr3)
arr4 = arr3.astype('i')
print(arr4)

copy_arr = arr1.copy()  # Copy of an array
view_arr = arr1.view()  # View of an array
print(copy_arr.base)
print(view_arr.base)

print(arr2.size)  # Gives the total size of the array
print(arr2.shape)  # Gives the tuple of integers indicating the size of array in each dimension.

str_arr = np.array(['a', 'b', 'c'])
print(str_arr.dtype.name)

even_num = np.arange(2,20,2)  # creates a array between the given range
print(even_num)

arr_3d = np.arange(12).reshape(3,2,2)
print(arr_3d.ndim)
print(arr_3d.base)  # Reshape gives view of original array

print(arr_3d.reshape(-1)) # Converting multidimesional array to one D array.

