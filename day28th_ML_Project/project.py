# project using mysql and joblib and SLR | MLR

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#pymysql connector
import pymysql
conn = pymysql.connect(host="localhost",user="root",database="day28th_db",password="2005")
print(conn)
query = "select avg_income,house_age,num_rooms,price, name from houses"
df = pd.read_sql(query, conn)
# print(df)


# # Static data
# data = {
#     "name": ['suraj', 'sushant', 'shivam', 'riya'],
#     "avg_income": [1000,200,300,400], # hundred and thousand
#     "house_age": [10.2, 2.5, 3.0, 4.0],
#     "num_rooms": [3,4,5,1],
#     "price": [10000,7000,15000,11000]
# }

# # Data frame
# df = pd.DataFrame(data)

# handle missing values
df.drop('name', axis=1, inplace = True)

# Feature scaling 
scaler = StandardScaler()
df[['avg_income', 'house_age', 'num_rooms']] = scaler.fit_transform(df[['avg_income', 'house_age', 'num_rooms']])
# print(df)

# Split Data
X = df[['avg_income', 'house_age', 'num_rooms']]
y = df["price"]

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

# Model Train
model = LinearRegression()
model.fit(x_train, y_train)

# Prediction
avg = int(input("Enter Avg. income: "))
age = int(input("Enter age of house: "))
rooms = int(input("Enter rooms in the house: "))

new_data = pd.DataFrame({
    "avg_income": [avg],
    "house_age": [age],
    "num_rooms": [rooms]
})

# Feature Scaling
new_data[['avg_income', 'house_age', 'num_rooms']] = scaler.transform(new_data[['avg_income', 'house_age', 'num_rooms']])

# Prediction
predict_data = model.predict(new_data)
print(f"Predicted value is : ₹{predict_data[0]:,.2f}")

# Model Dump
import joblib
joblib.dump(model, "house_model.joblib")