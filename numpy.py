import numpy as np  # alias -> np
# creating array 
# single dimension array
arr = np.array([1,2,3,4,5])
# checking dimensions of array -> using ndim 
print(arr.ndim)
arr2 = np.array([])
print(arr2.ndim)
arr = np.array([[]])
print(arr.ndim)
arr = np.array([[[]]])
print(arr.ndim)
# multidimensional array
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
#checking the shape of array
print(arr.shape)
arr.shape = (3,2)
print(arr)

# arange function
arr = np.arange(1,10)
print(arr)
arr = np.arange(1,10,2)# like range(start: stop : step)
print(arr)

# zeros function- array full of zeroes
arr = np.zeros(5)
print(arr)
# to generate 2 dimensions
arr = np.zeros([2,3])
print(arr)

# ones function- array full of ones
arr = np.ones([3,5])
print(arr)

#full function - array full of any value
arr = np.full(5,2)
print(arr)
arr1 = np.full([3,2],6)
print(arr1)

#uninitializied array
arr = np.empty([4,5])
print(arr)

# initializing array with random numbers
n1 = np.random.rand(10)
# return float btw 0 to 1 
print(n1)
n2 = np.random.rand(2,3) # to create multidimensional array
print(n2)
n1 = np.random.randint(1,100,5) # initialize with integers btw ranges 
print(n1)
#initialize array with random floats of standard normal deviation
# standard normal deviation -> mean = 0 and std = 1
n3 = np.random.randn(2,3)
print(n3)

# joining numpy arrays 

# vstack method -> joins vertically
n1 = np.array([10,20,30])
n2 = np.array([40,50,60])
print(np.vstack((n1,n2))) # it takes only one positional arguments
print(np.vstack((n2,n1)))
n1 = np.array([[1,2,3],[4,5,6]])
n2 = np.array([[7,8,9],[10,11,12]])
print(np.vstack((n1,n2)))

# hstack method
print(np.hstack((n1,n2)))# joins horizontally
print(np.hstack((n2,n1)))

# column_stack() -> joins column vise
print(np.column_stack((n1,n2)))
print(np.column_stack((n2,n1)))

# numpy intersection using intersect1d method
# return common elements in arguments -  array
n1 = np.array([10,20,30,40,50,60])
n2 = np.array([50,60,70,80,90])
print(np.intersect1d(n1,n2))

# setdiff1d method - takes two positional arguments and return unique elements of first argument
print(np.setdiff1d(n1,n2))
print(np.setdiff1d(n2,n1))

# numpy datatypes and typecasting
# dtype method to check data type of array
# astype function for typecasting
arr = np.array([10,20,30])
print(type(arr), arr.dtype)
arr = np.array(['string', 67, 56.0])
print(arr)
# new_arr = arr.astype(np.float64) # value error - as string cannot be convert into float or int
# print(new_arr)
print(arr.dtype)
arr = np.array([10,203,37.5])
print(arr)
print(arr.dtype)

new_arr = arr.astype(np.int64)
print(new_arr)

# size method - return size of an  array
print(new_arr.size)
arr = np.array([10,20,30,40,50,60])
# reshape function to change shape of an array
reshaped = arr.reshape(2,3)
print(reshaped)
print(reshaped.size)

# converting array to 1d array - ravel, flatten functions
ravel = reshaped.ravel()
print(ravel)
ravel[0]  = 100 # any changes made in ravel will also be reflected in reshaped -> returns a view
print(reshaped)
flatten = reshaped.flatten()
print(flatten)
flatten[0] = 200 # any changes made to flatten will not be reflected in reshaped - it returns photocopy
print(reshaped)

# numpy mathematical operations
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # removes fractional part i.e return quotient
print(a%b) # returns remainder
print(a**2)

# universal functions
print(np.sqrt(b))
angles = np.array([0,30,45,90])
print(np.sin(angles))

# indexing and slicing
arr = np.array([10,20,30,40,50,60])
print( arr[1:4])
print(arr[-1: -4: -1])
print(arr[-1: -4]) # it will return empty array 
    
matrix = np.array([[1,2, 3],[4,5,6],[7,8,9]])
print(matrix)
print(matrix[0:2, 0: 3])
print(matrix[0:2,:])
print(matrix[:,:])
print(matrix[1:,1:])

# np.take() - build in function for indexing and slicing
arr = np.array([10,20,30,40,50,60])
indexes = [3,4,1]
print(np.take(arr,indexes))

# iterating with nditer()
arr = np.array([[1,2],[3,4],[5,6]])
for item in np.nditer(arr):
    print(item, end = " ")
print()

# ndenumerate() -> both return indexes and values
for ind, item in np.ndenumerate(arr):
    print(ind,item)
    
# view and copy
# view - changes will reflect on  original array
arr = np.array([1,2,3,4,5])
print(arr)
view = arr[2:]
print(view)
view[0] = 200
print(arr)
# copy using copy() - changes will not reflect on original array
copy = arr[2:].copy()
print(copy)
copy[0] = 2
print(arr)

# transpose of matrix using transpose()
print(matrix)
print(matrix.transpose())

# concatenation
a = np.array([1,2])
print(a)
b = np.array([3,4])
print(b)
combine = np.concatenate((a,b))
print(combine)

# Splitting arrays
arr1 = np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.split(arr1,2))
print(np.split(arr1,1))
# print(np.split(arr1,3)) # raise value error -> splitting must be uniform

# repeat () - repeating individual arrays elements 
n1 = np.array([1,2,3])
print(np.repeat(n1,2))
print(np.repeat(n1,3))

# tile() - repeating whole array
print(np.tile(n1,2))
print(np.tile(n1,5))

# Aggregrate functions
arr = np.array([10,20, 30])
print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))
print(max(arr))
print(min(arr))

print(matrix)
print(np.sum(matrix))
# axis = 0-> rows,1 -> column
print(np.sum(matrix, axis = 0))
print(np.sum(matrix, axis = 1))

# cumulative operations - running total and running product
arr = np.array([1,2,3])
print(np.cumsum(arr))
print(np.cumprod(arr))

# conditional operations
# where
result = np.where(arr< 2,"low" ," high")
print(result)

# argwhere -> return index of element based on condition
arr = np.array([10,20,30,40])
result = np.argwhere(arr>20)
print(result)

# logical and
mask = np.logical_and(arr>10,arr<40)
print(mask)
print(arr[mask])
# logical_or
mask = np.logical_or(arr>10 ,arr<40)

print(arr[mask])

# nonzero()-> return index of non zero element
arr = [1,0,2,0,3]
print(np.nonzero(arr))

# Broadcasting
image = np.array([[100,150],[200,250]])
brightness = image + 50
print(brightness)

# vectorization
# np.vectorize() - convert a regular function to be applied on array

def square(n):
    return n*n
vfunc = np.vectorize(square)
print(arr)
print(vfunc(arr))

# dealing with missing values
# np.nan -> to show null value
# np.isnan() -> to check null value
a = np.array([5,7,np.nan,5])
print(a)
print(np.isnan(a))

# np.inf and -np.inf -> positive and negative infinity
# isinf -> check infinity
# isfinite -> check finite
b = np.array([2,3,4,np.nan,np.inf,6])
print(b)
print(np.isfinite(b))
print(np.isinf(b))

print(np.logical_or(np.isnan(b),np.isinf(b))





