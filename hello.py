import numpy as np 

data = [1,2,3,4,5]
arr = np.array(data)
#or
array = np.array([1,2,3,4,5])

print(arr)
print(arr.shape) # elements
print(arr.dtype) # type
print(arr.ndim) # size
# [1 2 3 4 5]
# (5,)
# int32
# 1

#to float
#array1 = np.array([1,2,3,4,5], dtype=np.float) # text output
#print(array1.dtype)

arr4 = np.arange(0,20,1.5) # work as range
print(arr4)

arr5 = np.linspace(0,2,10) # work some as range bur 
#from 1 to 2 10 numbers write
print(arr5)

arr6 = np.random.random((5,))
print(arr6)

# math operations
arr7 = np.array([1,2,3,4,5])
arr7 = np.sqrt(arr7)
print(arr7)

arr8 = np.sin(arr7)
print(arr8)

arr9 = np.cos(arr7)
print(arr9)
#.......

# adding numbers (+) in 2 arrays , smth like 
# that works other (multiply , substract, divide ...)
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,0])
c = np.add(a,b)
print(c)

# raise to a square
d = b ** 2
print(d)


arr10 = np.random.randint(-5,10,10)

print(arr10)
print(arr10.max())
print(arr10.min())
print(arr10.mean()) # average
print(arr10.sum())
print(arr10.std())
print(np.median(arr))

a = arr10 < 2
print(a)

#add,delete ,sort ...
array11 = np.array([-1,-23,1,2,3,4,5,56])
s = np.insert(array11,2,10)
print(s)

v = np.delete(array11,2)
print(v)

h = np.sort(array11)
print(h)

#
array12 = np.arange(1,10,1)
print(arr[arr < 2])
print(arr[(arr < 2 ) & (arr > 0)])

print(arr[(arr < 5) | (arr < 0)])


#MULTIDIMENSIONAL ARRAYS AND MATRIXES

matrix1 = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(matrix1)
print(matrix1.shape)
print(matrix1.size)
print(matrix1.ndim) # two-dimensional array

a = matrix1.reshape(1,9) #reshpe elem.
print(a)

matrix2 = np.array([(1,2,3),(4,5,6),(7,8,9)])
b =  np.resize(matrix2,(2,2)) #cuting
print(b)

matrix3 = np.arange(16).reshape(2,8)
print(matrix3)

#SPEcial matrix
k = np.zeros((2,3))
l = np.ones((3,3))
p = np.eye(5)
print(k)
print(l)
print(p)

d = np.full((3,3), 9)
print(d)

g = np.empty((3,2))
print(g)

#OPErations (work as in simple matrix)
# (* , - , + , /)


#AXIS; 0-line axis ; 1-column axis
array123 = np.array([[1,2,3],
					[4,5,6],
					[7,8,9]])
j = np.delete(array123,1,axis=0)
print(j)
h = np.delete(array123,1,axis=1)
print(h)

arrat = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(arrat.max)
print(arrat.max(axis=0)) # by line
print(arrat.max(axis=1)) # by column

arr1 = np.array([(1,2,3),(4,5,6),(7,8,9)])
arr2 = np.array([(10,11,12),(13,14,15),(16,17,18)])
ark = np.concatenate((arr1,arr2),axis=0) # to glue
print(ark)

l = np.append(ark , np.array([111,222,333]))
print(l)

print(ark[1,2]) # 2nd element 1st line
print(ark[:,2]) # [ 3  6  9 12 15 18]




# Somethin like that is numpy basic , and 
# functions ( we can work with files too )



