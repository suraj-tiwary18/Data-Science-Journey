#Reshape array
import numpy as np
# arr = np.arange(12) # 12 -> 3*4 || 12 -> 4*3
# up_arr = np.reshape(arr, (3,4)) # 3 -> row || 4 -> cols
# print(up_arr)

# example -> 1 (2D)
# arr = np.arange(24)
# up_arr = np.reshape(arr, (12,2))
# print(up_arr)

# Example -> 2 (3D)
# arr = np.arange(24)
# up_arr = np.reshape(arr, (3,2,4))
# print(up_arr)



# Flatten Method
# Flatten creates copy then works, shallow copy

# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr = arr.flatten()
# print(up_arr)
# print(arr)

# Example -> 3 (3D)
# arr = np.arange(24).reshape(3,2,4)
# print(arr)
# up_arr = arr.flatten()  #it convert all 2d, 3d, 4d etc d in 1d 
# print(up_arr)
# print(arr)




#Ravel
# Ravel works on original array, Deep copy

# arr = np.arange(14).reshape(7,2)
# print(arr)
# up_arr = arr.ravel()
# print(up_arr)

# #example -> 4 (3d)
# arr = np.arange(24).reshape(2,3,4)
# print(arr)
# up_arr = arr.ravel()
# print(up_arr)


# example -> 5 (3D)
# arr = np.arange(48).reshape(3,4,4)
# print(arr)
# up_arr = arr.ravel()
# print(up_arr)


#Transpose
# It convert row and col into col into row  (this is only works on 2d,3d,4d,etc not in 1d)

# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr = arr.T
# print(up_arr)


#exaple -> 6 (3D)
# arr = np.arange(24).reshape(2,3,4)
# print(arr)
# up_arr = arr.T
# print(up_arr)



#Slicing
#For 1d

# arr = np.arange(11)
# print(arr)
# up_arr = arr[:3]
# print(up_arr)


#For 2d
# arr = np.arange(16).reshape(8,2)
# print(arr)
# up_arr = arr[:, -1]
# print(up_arr)
# print(arr)


# #For 3d
# arr = np.arange(24).reshape(3,4,2)
# #manually access
# print(arr[0,0,0],arr[2,3,1])



#LOOPING
#While loop

#while loop for 1d
# arr = np.arange(12)
# i = 0
# while i < len(arr):
#     print(arr[i] , end=" ")
#     i += 1


#while loop for 2d
# arr1 = np.arange(12).reshape(3,4)
# i = 0
# len_i = len(arr1)
# print(len_i)
# len_j = arr1[0]
# print(len_j)
# while i < len_i:
#     j = 0
#     while j < len_j:
#         print(arr1[i][j], end=" ")
#         j += 1
#     i += 1



#For loop

# for loop 1d array
# arr = np.arange(12)
# for i in arr:
#     print(i, end = " ")

# # for loop 2d array
# arr = np.arange(12).reshape(3,4)
# for i in arr:
#     for j in i:
#         print(j, end = " ")

# #for loop 3d array
# arr = np.arange(24).reshape(2,3,4)
# for i in arr:
#     for j in i:
#         for k in j:
#             print(k, end = " ")


