# project using mysql and joblib and SLR | MLR

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# #pymysql connector
# import pymysql
# conn = pymysql.connect(host="13.220.156.88",user="mluser",database="ml_db",password="mlpass123")
# print(conn)
# query = "select avg_income,house_age,num_rooms,price, name from houses"
# df = pd.read_sql(query, conn)
# print(df)


# Static data
data = {
    "name": ['suraj', 'sushant', 'shivam', 'riya'],
    "avg_income": [1000,200,300,400], # hundred and thousand
    "house_age": [10.2, 2.5, 3.0, 4.0],
    "num_rooms": [3,4,5,1],
    "price": [10000,7000,15000,11000]
}

# Data frame
df = pd.DataFrame(data)

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
new_data = pd.DataFrame({
    "avg_income": [900],
    "house_age": [8],
    "num_rooms": [5]
})

# Feature Scaling
# new_data[['avg_income', 'house_age', 'num_rooms']] = scaler.fit_transform(new_data[['avg_income', 'house_age', 'num_rooms']])

# Prediction
predict_data = model.predict(new_data)
print(f"Predicted value is : {predict_data[0]}")

# Model Dump
import joblib
joblib.dump(model, "house_model.joblib")

