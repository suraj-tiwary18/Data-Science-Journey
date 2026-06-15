# File Handling

# import pandas as pd
# import numpy as np
# url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/refs/heads/main/file2.json"
# df = pd.read_json(url)
# print(df)


# anjali -> marks = null
# df.loc[4, "marks"] = None
# df.loc[3, "roll no"] = None
# print(df)
# print(df.isnull()) #This method is use to find null values in database

# column count missing values
# print(df.isnull().sum())

# drop null values by row
# print(df.dropna())

# drop null values by col
# print(df.dropna(axis=1))

# fill by zero
# print(df.fillna(0))

# # roll no -> 200 | marks -> 100
# df['roll no'] = df['roll no'].fillna(200)
# df['marks'] = df['marks'].fillna(100)
# print(df)

# method 2
# df.fillna({"roll no": 200, 'marks':100}, inplace=True)
# print(df)

# marks -> mean | nan fill with average

# method -> 1
# mn = df['marks'].mean()
# print(df['marks'].fillna(mn))

# method -> 2
# print(df['marks'].fillna(df['marks'].mean()))




# Aggregation
# import pandas as pd
# import numpy as np
# url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/refs/heads/main/file2.json"
# df = pd.read_json(url)


# #manually
# print(df['marks'].sum())
# print(df['marks'].mean())
# print(df['marks'].min())
# print(df['marks'].max())

# by Aggregation
# print(df['marks'].agg(["sum", "mean", "min", "max"]))





# CONCATENATE
# import pandas as pd
# url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/refs/heads/main/file2.json"
# df = pd.read_json(url)
# df1 = pd.read_json(url)
# print(pd.concat([df,df1])) # default row 
# print(pd.concat([df,df1], axis=1)) #colomn


# Question -> 1
# df1.loc[df1["name"] == "abhishek", "name"] = "suraj"
# print(pd.concat([df,df1],axis= 1))