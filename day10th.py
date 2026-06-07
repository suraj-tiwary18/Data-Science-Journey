# import numpy as np


#1D Aarry
# l = [1, 2, 3, 4, 5]
# print(l)

# arr = np.array(l)
# print(arr)
# print(l[0]) # [2, 3, 4] -> row
# print(l[0][0]) # [2, 3, 4] -> 1row -> first element -> 1


# #2D Array
# l = [[2, 3, 4], [5, 6, 7]]
# print(l)

# arr = np.array([[2, 3, 4], [5, 6, 7]])
# print(arr)
# print(arr[0]) # [2, 3, 4] -> 1row
# print(arr[0][0]) #[2, 3, 4] -> 1row -> first element -> 1


# #question
# arr = np.array([1, 2, 3], [4, 5, 6])
# arr[1][0] = 100
# print(arr)


#list
# l = [1, 2, 3]
# lm = l*2
# print(lm)

# #Array
# import numpy as np
# arr = np.array(l)
# arrM = arr*2
# print(arrM)

#comparsion
#list
# import time
# start = time.time()
# l = [i*2 for i in range(1000000)]
# print("list output :", time.time() - start)

# #array
# import numpy as np
# start = time.time()
# arr = np.array(1000000)*2
# print("array output:", time.time() - start)





#Zeros array 1d
# import numpy as np
# arr = np.zeros(5)
# print(arr)

# #zeros array 2d
# # import numpy as np
# arr1 = np.zeros((3,4))
# print(arr1)



# # ones array 1d
# import numpy as np
# arr = np.ones(5)
# print(arr)

# #ones array 2d
# arr1 = np.ones((3,4))
# print(arr1)


#question
# #question zero -> 2d -> 10
# import numpy as np
# arr = np.zeros((4, 5))+10
# print(arr)

# #question ones -> 2d -> 5
# arr1 = np.ones((4,5))*5
# print(arr1)


#FULL FOR 1D
# import numpy as np

# #for 1d
# arr = np.full((3),5)
# print(arr)

# #for 2d
# arr1 = np.full((2,3),5)
# print(arr1)


#question help of  zeros -> 2d -> 6
#question help of full -> 2d -> 1

# import numpy as np
# arr = np.zeros((3, 4))+6
# print(arr)

# arr1 = np.full((3, 4), 1)
# print(arr1)

#Random
#random for 1d
# import numpy as np
# arr = np.random.random(5)
# print(arr)

# #random for 2d
# arr1 = np.random.random((2, 3))
# print(arr1)



#arange for 1d
# import numpy as np
# arr = np.arange(5)
# print(arr)

# #arange for 1d || To convert into 2d -> reshape
# arr1 = np.arange(0, 10, 2)
# print(arr1)



# import numpy as np
# #vector 1d list
# l = [1, 2, 3]
# print(l)
# #vector 1d arrary
# arr = np.array([1,2,3])
# print(arr)

# # matrix 2d list
# l = [[1, 2, 3],[4, 5 ,6]]
# print(l)
# # matrix 2d array
# arr1 = np.array([[1,2,3],[4,5,6]])
# print(arr1)

# #tensor 3d list
# l = [[1,2],[3,4],[5,6],[7,8]]
# print(l)
# #tensor 3d array
# arr2 = np.array([[1,2],[3,4],[5,6],[7,8]])
# print(arr2)


#Array
import numpy as np
arr = np.arange(12).reshape(3,4)
print("shape", arr.shape)
print("dimension", np.ndim(arr))
print("size", np.size(arr))
print("datatype", arr.dtype)
