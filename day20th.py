#Question no. -> 1
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([1,2,3,4])
# y1 = [10,20,30,40]
# y2 = [20,40,60,80]
# y3 = [30,60,90,120]

# w = 0.90
# plt.bar(x - w/3,y1, label="google", width=w/3)
# plt.bar(x,y2, label="microsoft", width=w/3)
# plt.bar(x + w/3,y3, label="apple", width=w/3)

# plt.xlabel("Years")
# plt.ylabel("Revenue")
# plt.title("Revenue Growth of Top Tech Companies (2020-2025)")

# plt.legend()
# plt.show()



# Histogram
# import matplotlib.pyplot as plt
# marks = [40,55,60,70,75,90,33,50]

# plt.hist(marks,bins=4,color="green")
# plt.show()



# Pie Chart
# import matplotlib.pyplot as plt
# fruits = ["apple", "banana", "orange", "watermelon"]
# count = [40,30,15,70]
# colors = ["red", "yellow", "orange", "green"]
# plt.pie(count, labels=fruits, colors=colors)
# plt.show()


# Pie Chart percentage
# import matplotlib.pyplot as plt
# fruits = ["apple", "banana", "orange", "watermelon"]
# count = [40,30,15,70]
# colors = ["red", "yellow", "orange", "green"]
# plt.pie(count, labels=fruits, colors=colors, startangle=90, autopct="%1.1f%%")
# plt.show()


# # Subplot
# import matplotlib.pyplot as plt 

# #first chart
# x = [1,2,3,4,5]
# y = [10,20,30,40,55]
# plt.subplot(2,2,1) #row,cols,position
# plt.plot(x,y)
# plt.xlabel("x axis")
# plt.ylabel("y axis")

# #second chart
# x1 = ["apple", "banana", "orange", "mango"]
# y1 = [40,30,15,70]
# plt.subplot(2,2,2) #row,cols,position
# plt.pie(y1, labels=x1, startangle=90) 
# plt.xlabel("x1 axis")
# plt.ylabel("y1 axis")

# #third chart
# x2 = ["google", "microsoft", "apple", "amazon"]
# y2 = [5,10,15,20]
# plt.subplot(2,2,3)
# plt.bar(x2,y2)


# #fourth chart
# marks = [20,25,30,35,40,45,50,60]
# plt.subplot(2,2,4)
# plt.hist(marks,bins=5,color="red")

# plt.tight_layout()
# plt.show()