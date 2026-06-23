# Data Preprocessing 


# Handle missing values :- 
# import pandas as pd

# 1. Data Collection :-
# data = {
#     'Name': ['Ram', 'Kamal','Ajay'],
#     'Age': [25,None,32],
#     'Salary': [5000,6000,None]
# }
# df = pd.DataFrame(data)
# print(df)


# 2. Data Cleaning :-  

# df['Age'].fillna(df['Age'].mean(), inplace = True) # fill nan values with some value
# df['Salary'].fillna(df['Salary'].mean(), inplace = True)
# print(df)

# print(df.dropna()) # drop specific row

# print(df.isnull().sum()) # sum of null



# Encoding categorial values :-

# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# data = {
#     'Name': ['Ram', 'Kamal','Ajay', 'Neetu', 'Kavi', 'Sapu'],
#     'Age': [25,None,32,20,21,22],
#     'Salary': [5000,6000,None, 7000, 8000, 9000], 
#     'Gender': ['male', 'male', 'male', 'None', 'female', 'female']
# }

# df = pd.DataFrame(data)
# print("Original dataframe :- ")
# print(df)

# # Label Encoder
# le = LabelEncoder()
# df_label = df.copy()
# df_label['Gender'] = df['Gender'].fillna('unknown')
# df_label['Gender_Encoder'] = le.fit_transform(df_label['Gender'])

# print('After label Encoding :- ')
# print(df_label)


# One Hot Encoding :- 
# import pandas as pd

# data = {
#     'colors': ['red', 'blue', 'green', 'red', 'blue']
# }

# df = pd.DataFrame(data)
# print("Original Data :- ")
# print(df)

# encoded_df = pd.get_dummies(df, columns=['colors'])

# print("After one hot encoding")
# print(encoded_df)

# Question -> blue, Blue, 

# import pandas as pd
# data = {
#     'colors': ['red', 'blue', 'green', 'red', 'Blue']
# }

# df = pd.DataFrame(data)
# print("Original Data :- ")
# print(df)

# df['colors'] = df['colors'].str.lower() 
# encoded_df = pd.get_dummies(df, columns=['colors'])

# print("After one hot encoding")
# print(encoded_df)