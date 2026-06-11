# import pandas as pd

# d = {
#     "name": ["vishal", "virat", "vineet"],
#     "salary": [100,200,300]
# }
# df = pd.DataFrame(data=d)

#Operations on Column

# df["holiday"] = df["salary"] / 100
# df["decrement"] = [10,20,30]

# #Delet Column
# df.drop(["salary", "name"], axis=1, inplace=True)
# print(df)





#Operations on Row
# print(df.loc[2,"name"])
# print(df.iloc[2,0])

#get single row data
# print(df.iloc[1])
# print(df.loc[1])

#Get Multi rows
# print(df.iloc[0:3])
# print(df.loc[0:3, ["name"]])
# print(df.iloc[0:3])

# sub data get
# df1 = df.iloc[0:2, [0]] #row -> 0,1 and cols -> 0 | name
# print(df1)

# df2 = df.loc[0:2, ["name"]]
# print(df2)



# Question no. - > 1
# import pandas as pd

# data = {
#     "Emp_ID": [101, 102, 103, 104, 105, 106],
#     "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
#     "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
#     "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
#     "Experience": [2, 3, 5, 4, 1, 3]
# }

# df = pd.DataFrame(data)
# print(df)

#Operation on Column
# print(df.)




