import numpy as np

#Sort
# 1D 
# arr = np.array([10,40,30,60,90,7,5])
# print(arr)
# arr_s = np.sort(arr)
# print(arr_s)

#2D
# axis = 0 -> cols
# axis = 1 -> rows
# arr1 = np.array([[5,60,20],[40,90,41]])
# print(arr1)
# arr1_s = np.sort(arr1)
# print(arr1_s) # default row

#example -> 1
# arr = np.array([[4,2,8],[8,5,6]])
# print(arr)
# # arr_s = np.sort(arr) # for axis = 0, for row
# arr_s = np.sort(arr, axis = 1) # for axis = 1, for cols
# print(arr_s)

#example -> 2
#by default sorting -> ascending | decending

# arr = np.array([[2,9,5],[7,3,1]])
# print(arr)
# arr_s = np.sort(arr)[:,::-1] #  reverse sort
# print(arr_s)


#Filter
#1D 
# arr = np.array([10,20,30,40,6,3,4,2])
# print(arr)
# arr_f = arr[arr < 40]
# print(arr_f)

#example
# arr = np.array([2,5,7,4,1,6,3,9,])
# print(arr)
# arr_even = arr[arr % 2 == 0] #for even
# print("Even Array :- ", arr_even)
# arr_odd = arr[arr % 2 != 0] #for odd
# print("Odd Array :- ", arr_odd)


#Fancy indexing
#1D
# arr = np.array([10,20,3,4,90,100])
# print(arr)
# arr_f = arr[[0, 2]]
# print(arr_f)

#pending
#2D
# arr = np.array([[4,5,6],[3,9,5]])
# print(arr)
# arr_f = arr[[]]
# print(arr_f)




#np.where
#1D
# arr = np.array([10,3,4,80,30,40,9])
# print(arr)
# arr_w = np.where(arr > 40, "True", "False")
# print(arr_w)

#example
# arr = np.array([10,3,4,80,30,40,9])
# print(arr)
# arr_w = np.where(arr > 40, arr+2, arr-2) # condition : True : False
# print(arr_w)

#example
# arr = np.array([30,45,67,23,57,90])
# print(arr)
# arr_w = np.where(arr % 2 == 0, 100, arr)
# print(arr_w)


#CONCATENATE
#1D
# arr = np.array([10,20,30])
# arr1 = np.array([1,2,4])
# arr_arr1 = np.concatenate((arr,arr1), axis=0)
# print(arr_arr1)

#2D
# arr = np.array([[1,2,3],[4,5,6]])
# arr1 = np.array([[7,8,9],[4,8,5]])
# arr_arr1 = np.concatenate((arr,arr1), axis=0)
# print(arr_arr1)





# Statistical Functions :-

import numpy as np
arr = np.array([10,15,20,25,30,35,40,45,50,55,60,65,70])

print("1. SUM :- ")
print(np.sum(arr))
print("\n")
print("2. MEAN :-")
print(np.mean(arr))
print("\n")
print("3. MEDIAN :-")
print(np.median(arr))
print("\n")
print("4. MIN :-")
print(np.min(arr))
print("\n")
print("5. MAX :-")
print(np.max(arr))
print("\n")
print("6. VAR :-")
print(np.var(arr))
print("\n")
print("7. STD :-")
print(np.std(arr))
print("\n")
print("8. PROD :-")
print(np.prod(arr))
print("\n")
print("9. CUMSUM :-")
print(np.cumsum(arr))
print("\n")
print("10. CUMPROD :-")
print(np.cumprod(arr))
print("\n")
print("11. ARGMIN :-")
print(np.argmin(arr))
print("\n")
print("12. ARGMAX :-")
print(np.argmax(arr))
print("\n")

arr_abs = np.array([20,-10,-70,30,-20,-60,-40])
print("13. ABS :-")
print(np.abs(arr_abs))
print("\n")

arr_unique = np.array([10,20,30,30,40,50,50,20,70])
print("14. UNIQUE :-")
print(np.unique(arr_unique))
print("\n")

print("15. PERCENTILE :-")
print(np.percentile(arr,50))
print("\n")
print("16. QUANTILE :-")
print(np.quantile(arr, 0.5))
print("\n")
print("17. PTP :-")
print(np.ptp(arr))
print("\n")
print("18. ANY :-")
print(np.any(arr))