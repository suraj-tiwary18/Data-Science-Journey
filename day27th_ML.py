# # Feature Scaling

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler

# data = {
#     "Experience": [300,600,900,1500],
#     "salary": [1000,2500,2000,3000]
# }

# df = pd.DataFrame(data)
# print(df)

# # Standard Scaler
# scaler = StandardScaler()
# df['Experience'] = scaler.fit_transform(df[['Experience']]) # 2d
# print(df)

# # Split Data
# X = df['Experience']
# Y = df['salary']

# print(X)
# print(Y)

# # Graph :- 
# plt.plot(X , Y)
# plt.title("Experience vs Salary ")
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.show()


# # data split training testing
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split

# data = {
#     "Experience": [300,600,900,1500],
#     "salary": [1000,2500,2000,3000]
# }

# df = pd.DataFrame(data)
# print(df)

# # Split Data
# X = df['Experience'] # capital X
# Y = df['salary']

# # Train test split
# x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2, random_state=2)
# print("x train : ", x_train)
# print("x test : ", x_test)
# print("y_train : ", y_train)
# print("y test : ", y_test)




# Example no. 1 :-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/extended_salary_data.csv"
df = pd.read_csv(url)
print(df)

# Split Data
X = df[['experience']]
Y = df['salary']

# Train Test split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
print("X Train : ", x_train)
print("X test : ", x_test)
print("Y Train :", y_train)
print("Y test :" , y_test)


# Simple linear Reg. | Prediction
from sklearn.linear_model import LinearRegression

# model fit
model = LinearRegression()
model.fit(x_train, y_train) # 2d

# input form user
user = int(input("Enter your experience : "))
# model prediction
new_data = {
    "experience": [user]
}

df1 = pd.DataFrame(new_data)
print(df1)
pred_data = model.predict(df1)
print(pred_data[0])