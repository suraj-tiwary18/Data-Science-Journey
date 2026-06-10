import pandas as pd
url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/main/file2.json"
df = pd.read_json(url)

#HEAD 
# print(df.head(3))
# print(df.head(5)) # starting index 0 to 4 
# print(df.head(-1)) # only print index 0,1,2,3
# print(df.head(-2)) # only print index 0,1,2
# print(df.head(-3)) # only print index 0,1

#TAIL
# print(df.tail(2)) #we get last 2 rows data
# print(df.tail(-1)) #we get last 2 rows data

#SHAPE
# print(df.shape)
# df = pd.DataFrame(data = [10,20,30,40,50],colums = ["age"])
# pritn(df)

#INFO
# print(df.info())

# VERBOSE
# df.info(verbose=True) #show all information
# df.info(verbose=False) #hide all information

#RENAME
# print(df.rename(columns={"name": "student_name"})) #This does not change original data columns
# print(df.rename(columns={"name": "student_name", "marks": "salary"}, inplace=True)) #inplace change original data columns
# print(df)

#DESCRIBE
# print(df.describe())


# # Question -> 1
# import pandas as pd

# data = {
#     "Emp_Id": [101, 102, 103, 104, 105, 106],
#     "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
#     "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
#     "salary": [50000, 45000, 60000, 55000, 48000, 52000],
#     "Experience": [2, 3, 5, 4, 1, 3]
# }

# df = pd.DataFrame(data)
# # print(df)


# #HEAD
# print(df.head(2))
# print(df.head(-2))
# print("\n")

# #TAIL
# print(df.tail(3))
# print(df.tail(-3))
# print("\n")


# #SHAPE
# print(df.shape)
# print("\n")


# #INFO
# print(df.info())
# print("\n")


# #VERBOSE
# df.info(verbose=True)
# df.info(verbose=False)
# print("\n")

# #RENAME
# print(df.rename(columns={"Name": "Emp_Name"}, inplace=True))
# print(df)
# print("\n")


# #DESCRIBE
# print(df.describe())

# <---- Question over ---->



#For single column data
# print(df['name'])


# Add single column
# df["salary"] = df["marks"]
# print(df)

# manually add column
# df["salary"] = [100,200,300,400,500]
# print(df)

# add 100 in marks column
# df["salary"] = df["marks"] + 100
# print(df)

# increment 10% in salary
# df["salary"] = [100,200,300,400,500]
# df["increment"] = df["salary"] + (df["salary"] / 10)
# print(df)