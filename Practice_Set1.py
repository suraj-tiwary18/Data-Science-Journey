# Data structure : [restaurant_id, 2021, 2022, 2023, 2024]

import numpy as np

sales_data = np.array([
    [1, 150000, 180000, 220000, 250000], #Paradise Biryani
    [2, 120000, 140000, 160000, 190000], #Beijing Bites
    [3, 200000, 230000, 260000, 300000], #Pizza Hub
    [4, 180000, 210000, 240000, 270000], #Burger Point
    [5, 160000, 185000, 205000, 230000], #Chai Point
])



# Question no. 1 -> Print the complete dataset
# print(sales_data)

# Question no. 2 -> Find the shape of the array
# print("Shape of the data set :- ")
# print(np.shape(sales_data))
# print(sales_data.shape)

# Question no. 3 -> Find the number of dimensions
# print("Dimension of the data set :- ")
# print(sales_data.ndim)

# Question no. 4 -> Find the total number of elements
# row * col = element of the set
# print(sales_data.size)

# Question no. 5 -> Print only Restaurant IDs
# print("Restaurant Id of the set :- ")
# print(sales_data[:,0])

# Question no. 6 -> Print 2021 sales data
# print("Sales data in 2021 :- ")
# print(sales_data[:, 1])

# Question no. 7 -> Print 2024 sales data
# print("Sales data in 2024 :- ")
# print(sales_data[:, 4])

# Question no. 8 -> Find the maximum sales value
# print(np.max(sales_data[:, 1:]))

# Question no. 9 -> Find the minimum sales value
# print(np.min(sales_data[:, 1:]))

# Question no. 10 -> Find total sales of all restaurants in 2021
# print(np.sum(sales_data[:, 1]))



# Question no. 11 -> Find average sales in 2024

#1st way:- 
# total_sum = np.sum(sales_data[:, 4])
# print("Average sales in 2024 :- ")
# print(total_sum/5)

#2nd way:- 
# print("Average sales in 2024 :- ")
# print(np.mean(sales_data[:, 4]))



# Question no. 12 -> Find total sales of each restaurant

#1st way :-
# print("Total sales of Paradise Biryani are :- ")
# print(np.sum(sales_data[0, 1:]))
# print("Total sales of Beijing Bites are :- ")
# print(np.sum(sales_data[1, 1:]))
# print("Total sales of Pizza Hub are :- ")
# print(np.sum(sales_data[2, 1:]))
# print("Total sales of Burger Point are :- ")
# print(np.sum(sales_data[3, 1:]))
# print("Total sales of Chai Point are :- ")
# print(np.sum(sales_data[4, 1:]))

#2nd way :- 
# print("Total sales of each resturent are :- ")
# print(np.sum(sales_data[:, 1:], axis = 1 ))



# Question no. 12 -> Find average sales of each restaurant

#1st way :-
# print("Average sales of Paradise Biryani are :- ")
# print(np.mean(sales_data[0, 1:]))
# print("Average sales of Beijing Bites are :- ")
# print(np.mean(sales_data[1, 1:]))
# print("Average sales of Pizza Hub are :- ")
# print(np.mean(sales_data[2, 1:]))
# print("Average sales of Burger Point are :- ")
# print(np.mean(sales_data[3, 1:]))
# print("Average sales of Chai Point are :- ")
# print(np.mean(sales_data[4, 1:]))

#2nd way :- 
# print("Average sales of each resturent are :- ")
# print(np.mean(sales_data[:, 1:], axis = 1 ))