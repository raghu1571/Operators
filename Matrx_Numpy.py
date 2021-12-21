from numpy import *
arr1= array([
             [1,2,3,4],
             [5,6,7,8]

            ])
arr2= arr1.flatten()
print(arr1)
print(arr1.ndim) #dimension
print(arr1.shape) #no of rows and columns
print(arr1.size) # size of array
print(arr2)

print("***********************")

arr3= array([
                [1,4,6,8,9,3],
                [2,5,7,11,13,15]

            ])
arr4= arr3.reshape(2,2,3)#two two dimensional arrays each one have two one dimensional arrays and each array contain 3 values
print(arr4)

print("***********************")

m= matrix('1,2,3;4,5,6;7,8,9')
print(m)
print(diagonal(m))