import numpy as np

arr = np.array([1, 2, 3, 4])
print(f"arr:\n{arr}\ntype: {type(arr)}\n")

arr = np.array(42)
print(f"{arr.ndim}-D arr:\n{arr}\n")

arr = np.array([1,2,3])
print(f"{arr.ndim}-D arr:\n{arr}\n")

arr = np.array([[1,2,3],[4,5,6]])
print(f"{arr.ndim}-D arr:\n{arr}\n")

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(f"{arr.ndim}-D arr:\n{arr}\n")

arr = np.array([1,2,3], ndmin=5)
print(f"{arr.ndim}-D arr:\n{arr}\n")

arr = np.array([1,2,3,4,5])
print(f"the first element is: {arr[0]}")
print(f"the sum between the second and the fourth element is: {arr[1] + arr[3]}\n")

arr = np.array([[1,2,3],[4,5,6]])
print(f"{arr.ndim}-D arr:\n{arr}\n")
print(f"the first element of the second row is: {arr[1,0]}\n")

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(f"{arr.ndim}-D arr:\n{arr}\n")
print(f"{arr[1,0,1]}\n")

arr = np.array([1,2,3,4,5,6,7])
print(f"slice from the second and the fourth number: {arr[1:4]}")
print(f"slice from the second number and the end of the array: {arr[1:]}")
print(f"slice from the beginning and the fourth number (not included): {arr[:4]}")
print(f"slice from the index 3 from the end to index 1 from the end: {arr[-3:-1]}")
print(f"slice from the second to the fifth number every two number: {arr[1:5:2]}\n")

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"{arr.ndim}-D arr:\n{arr}\n")
print(arr[1, 1:4])
print(arr[0:2, 2])
print(arr[0:2, 1:4])

print("\n")

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

print("\n")

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

print("\n")

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

print("\n")

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

print("\n")

arr = np.array([1.1, 2.6, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

print("\n")

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

print("\n")

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

print("\n")

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

print("\n")

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(f"x: {x.base}")
print(f"y: {y.base}")

print("\n")

arr = np.array([[1, 2, 3, 4, 5]])
print(arr.shape)

print("\n")

arr = np.array([1,2,3,4], ndmin=5)
print(arr)
print(arr.shape)

print("\n")

arr = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])
print(arr.shape)
newarr = arr.reshape(4, 3)
print(newarr)
print(newarr.shape)

print("\n")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.reshape(2,3,2))

print("\n")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)

print("\n")

arr = np.array([1,2,3,4], ndmin=1)
print(arr)
arr = arr.reshape(2, -1)
print(arr)

print("\n")

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

for x in arr:
  for y in x:
    print(y)

print("\n")

arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in np.nditer(arr):
  print(x)

print("\n")

arr = np.array([1,2,3])
for x in np.nditer(arr.astype('S')):
  print(x)

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

print("\n")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)

print("\n")

arr = np.array([1,2,3])
for i, x in np.ndenumerate(arr):
    print(i, x)

print("\n")

arr = np.array(['a', 'b', 'c'])
for x in arr:
  print('Hello ' + x)

print("\n")

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(np.concatenate((arr1, arr2)))

print("\n")

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.concatenate((arr1, arr2), axis=1))
print(np.hstack((arr1, arr2)))

print("\n")

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.concatenate((arr1, arr2), axis=0))
print(np.vstack((arr1, arr2)))

print("\n")

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.dstack((arr1, arr2)))

print("\n")

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

print("\n")

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

print("\n")

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(arr)
newarr = np.array_split(arr, 3)
print(newarr)

print("\n")

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

print("\n")

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.hstack((arr1, arr2)))
arr = np.array([1,2,3,4,5,6,7,8])
print(np.hsplit(arr, 2))

print("\n")

arr = np.array([1,2,3,4])
print(np.where(arr == 4))
print(np.searchsorted(arr, 4))
print(np.searchsorted(arr, 4, side='right'))

print("\n")

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

print("\n")

arr = np.array([1,2,3,4])
print(np.searchsorted(arr, -2))

print("\n")

arr = np.array([4,2,8,3,7])
print(np.sort(arr))

print("\n")

arr = np.array([True, False, True])
print(np.sort(arr))

print("\n")

arr = np.array([[3,20],[8,1]])
print(np.sort(arr))

print("\n")

arr = np.array([41,42,43,44])
x = [True, False, True, False]
print(arr[x])

print("\n")

arr = np.array([41,42,43,44])
filter = arr > 42
print(arr)
print(filter)
print(arr[filter])

filter = arr%2 == 0
print(arr[filter])
