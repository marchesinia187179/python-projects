import numpy as np
from numpy import random

x = [1,2,3,4]
y = [5,6,7,8]
z = np.add(x, y)
print(z)

print("\n")

x = random.randint(1,10,5)
y = random.randint(1,10,5)
print(x)
print(y)
print(np.add(x,y))
print(np.subtract(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))
print(np.power(x,y))
print(np.mod(x,y))
print(np.remainder(x,y))
print(np.divmod(x,y))
print(np.absolute(x))

print("\n")

arr = np.trunc([-3.1666, 3.6667])
print(arr)

print("\n")

arr = np.around(-3.1666, 2)
print(arr)

print("\n")

arr = np.floor([-3.1666, 3.6667])
print(arr)

print("\n")

arr = np.ceil([-3.1666, 3.6667])
print(arr)

print("\n")

arr = np.arange(1,11)
print(arr)
print(np.log2(arr))
print(np.log10(arr))
print(np.log(arr))

print("\n")

x = random.randint(0,10,3)
y = random.randint(0,10,3)
print(x)
print(y)
print(np.add(x,y))
print(np.sum([x,y]))
print(np.sum([x,y], axis=1))
print(np.cumsum(x))

print("\n")

arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)

print("\n")

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x)
x = np.prod([arr1, arr2], axis=1)
print(x)

print("\n")

arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)

print("\n")

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)
newarr = np.diff(arr, n=2)
print(newarr)

print("\n")

print(np.lcm(4,6))
print(np.lcm.reduce([4,6,24]))
print(np.lcm.reduce(np.arange(1,11)))

print("\n")

print(np.gcd(4,6))
print(np.gcd.reduce([4,6,24]))
print(np.gcd.reduce(np.arange(1,11)))

print("\n")

print(np.sin(np.pi/2))
print(np.sin([np.pi/2, np.pi/4, np.pi, 0]))
print(np.deg2rad([90,45,180,0]))
print(np.rad2deg(np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])))
print(np.arcsin(1.0))
print(np.arcsin([1,-1,0.1]))
print(np.hypot(2,2))

print("\n")

print(np.sinh(np.pi/2))
print(np.cosh(np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])))
print(np.arcsinh(1.0))
print(np.arctanh(np.array([0.1, 0.2, 0.5])))

print("\n")

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)

print("\n")

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)
newarr = np.setdiff1d(arr1, arr2, assume_unique=True)
print(newarr)
newarr = np.setxor1d(arr1, arr2, assume_unique=True)
print(newarr)