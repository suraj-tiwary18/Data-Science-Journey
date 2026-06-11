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
# # print(df)

# #Operation on Column
# # print(df[df["Department"] == "IT"])

# # df.loc[df["Name"] == "Amit", "Salary"] = 55000
# # print(df)

# df.loc[df["Department"] == "HR", "Salary"] *= 1.10
# print(df)

# df = df[df["Emp_ID"] != 105]
# print(df)



# Operation on student-data.json file
import pandas as pd
url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/refs/heads/main/student-data.json"
df = pd.read_json(url)
# print(df)

# All male values
# male = df.loc[df["gender"] == "Male"]
# print(male)

# Print Raja and Dinesh 
# print(df.iloc[3:9:5])

# Filter 1
# print(df[df["english"] == 95])

# Filter 2
# print(df[df["maths"] < 60])

# physics values less than and equal to 56
# print(df[df["physics"] <= 56])

# print(df[(df["gender"] == "Male") & (df["maths"] > 80)])
# print(df[(df["gender"] == "Female") | (df["maths"] > 80)])

# print values maths > 90 and english > 90
# print(df[(df["maths"] >= 90) & (df["english"] >= 90)] ["name"])

# print values maths > 90 and english > 90 and they are male only print name
# print(df[(df["maths"] > 90) & (df["english"] > 90) & (df["gender"] == "Male")] ["name"])