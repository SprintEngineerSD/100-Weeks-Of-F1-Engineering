import numpy as np

#array = np.array([1,2,3,4])
#array *= 2
#print(array)

#MULTIDIMENSIONAL ARRAYS
#array = np.array([[["A","B","C"], ["D","E","F"],["G","H","I"]],
 #               [["A","B","C"], ["D","E","F"],["G","S","I"]],
  #                   [["A","B","C"], ["D","S","F"],["G","N","I"]]])

#word = array[0,0,0] + array[1,2,1] + array[2,1,1]
#print(word)
#print(array.ndim)

#Slicing
#[start:end:step]


#array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]])
#print(array[1:,0::2])

#Arithmetic in numpy

#Scalar
#array = np.array([1,2,3])
#print(array+1)
#print(array-2)
#print(array*3)
#print(array/4)
#print(array**5)

#vectorized math
#array = np.array([1,2,3])
#print(np.sqrt(array))
#print(np.round(array))
#print(np.floor(array))
#print(np.ceil(array))
#print(np.pi)
#print("/n")
#print(np.pi * array **2)

#Element Wise Arithmetic
#array1 = np.array([1,2,3])
#array2 = np.array([4,5,6])
#print(array1+array2)
#print(array1-array2)
#print(array1*array2)
#print(array1/array2)
#print(array1**array2)

#comparison operators
scores = np.array([91,55,100,73,82,64])

scores[scores < 60] = 0
scores[scores >= 60] = 1

print(scores)


