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
#scores = np.array([91,55,100,73,82,64])

#scores[scores < 60] = 0
#scores[scores >= 60] = 1

#print(scores)

#Boradcasting

#array1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
#array2 = np.array([[1],[2],[3],[4]])
#print(array1.shape)
#print(array2.shape
#print(array1 * array2)
#array3 = np.array([[1], [2], [3], [4],[5],[6],[7],[8],[9],[10]])
#array4 = np.array([[1,2,3,4,5,6,7,8,9,10]])
#print(array3.shape)
#print(array4.shape)
#print(array3 *array4)

#Aggregate = summarizes data and typically returns a single value
#array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#print(np.sum(array))
#print(np.mean(array))
#print(np.std(array)) #standrad deviation
#print(np.var(array)) #variance
#print(np.min(array))
#print(np.max(array))
#print(np.argmin(array)) #argument Minimum value; shows index value
#print(np.argmax(array))
#print(np.sum(array, axis=0)) #sums all columns
#print(np.sum(array, axis=1)) #sums all rows


#Filtering = Refers to the process of selecting elements
#           from an array that match a given condition

ages = np.array([[21,17,19,20,16,30,18,65],[39,22,15,99,18,19,20,21]])
#teenagers = ages[ages < 18]
#seniors = ages[ages >= 65]
#evens = ages[ages %2 == 0]
#odds = ages[ages %2 != 0]
#print(odds)
adults = np.where(ages >= 18, ages, 0) #this retains the original shape of array

print(adults)



