# Revision :- 

# # Train Test Split
# from sklearn.model_selection import train_test_split

# x = [[2], [3], [4], [5], [6]] # input | features
# y = [30, 40, 50, 60, 70] # Output | target

# # Split Dataset
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# print("Training Features: ")
# print(x_train)
# print("\n")

# print("Testing Features: ")
# print(x_test)
# print("\n")

# print("Training Labels: ")
# print(y_train)
# print("\n")

# print("Testing Labels: ")
# print(y_test)






# # Linear Regression
# import pandas as pd
# from sklearn.linear_model import LinearRegression

# data = {
#     "Experience": [1,2,3,4,5],
#     "Salary": [3,5,7,9,11]
# }

# df = pd.DataFrame(data)
# x = df[['Experience']] # input single
# y = df['Salary']

# # model
# model = LinearRegression()
# model.fit(x, y)

# # prediction
# new_data = pd.DataFrame({
#     "Experience": [6]
# })
# pred = model.predict(new_data)
# print(pred[0])



# New Topics :-

# # Evaluation Matrix :-

# import pandas as pd
# import numpy as np
# from sklearn.metrics import mean_absolute_error
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import r2_score

# # Actual values prediction
# y_true = np.array([50,60,75,90,100])
 
# # Predicted Values
# y_pred = np.array([52,58,78,88,105])

# # mae (mean absolute error)
# mae = mean_absolute_error(y_true, y_pred)
# print(mae)

# # mse (mean squared error)
# mse = mean_squared_error(y_true, y_pred)
# print(mse)

# # rmse (square root of mse)
# rmse = np.sqrt(mse)
# print(rmse)

# # r2 score
# r2 = r2_score(y_true, y_pred)
# print(r2)






# Lasso vs Ridge Regression

# Ridge Regression :-

# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import Ridge, Lasso
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# data = {
#     "size":[1000,1200,1500,1800,2000,2200,2500,2700,3000,3200],
#     "bedrooms":[2,2,3,3,3,4,4,4,5,5],
#     "age":[20,18,15,12,10,8,6,5,4,2],
#     "price":[30,35,45,50,55,60,68,72,80,85]
# }

# df = pd.DataFrame(data)

# # Split Data in x and y
# x = df[['size', 'bedrooms', 'age']]
# y = df['price']

# # Split data in training and testing
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# # Training -> Ridge Regression
# ridge = Ridge(alpha=1.0)
# ridge.fit(x_train, y_train)

# ridge_p = ridge.predict(x_test)
# print("X Test")
# print(x_test)
# print("\n")

# print("Prediction")
# print(ridge_p)

# # MAE
# mae = mean_absolute_error(y_test, ridge_p)
# print("MAE : ", mae)

# # MSE
# mse = mean_squared_error(y_test, ridge_p)
# print("MSE :",mse)

# # RMSE
# rmse = np.sqrt(mse)
# print("RMSE :", rmse)

# # R2 Score
# r2 = r2_score(y_test, ridge_p)
# print("R2 score: ", r2)

# # model intercept
# print(ridge.intercept_) # 1
 
# # model coef  price = intercept + (cof1,* feat1)
# print(ridge.coef_)




# Lesso Regression :-

# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import Ridge, Lasso
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# data = {
#     "size":[1000,1200,1500,1800,2000,2200,2500,2700,3000,3200],
#     "bedrooms":[2,2,3,3,3,4,4,4,5,5],
#     "age":[20,18,15,12,10,8,6,5,4,2],
#     "price":[30,35,45,50,55,60,68,72,80,85]
# }

# df = pd.DataFrame(data)

# # Split :-
# x = df[['size', 'bedrooms', 'age']]
# y = df['price']

# # Training and Testing
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# # Training -> Lasso reg.
# lasso = Lasso(alpha=1.0)
# lasso.fit(x_train, y_train)

# lasso_p = lasso.predict(x_test)
# print("X Test")
# print(x_test)
# print("\n")

# print("Prediction")
# print(lasso_p)

# # MAE
# mae = mean_absolute_error(y_test, lasso_p)
# print("MAE : ", mae)

# # MSE
# mse = mean_squared_error(y_test, lasso_p)
# print("MSE :",mse)

# # RMSE
# rmse = np.sqrt(mse)
# print("RMSE :", rmse)

# # R2 Score
# r2 = r2_score(y_test, lasso_p)
# print("R2 score: ", r2)

# # model intercept
# print(lasso.intercept_) # 1
 
# # model coef  price = intercept + (cof1,* feat1)
# print(lasso.coef_)






# Classifications :- 

# Logicstic Regression :- (no algo only classification works)
# import pandas as pd
# from sklearn.linear_model import LogisticRegression

# data = {
#     "hours": [1,2,3,4,5,6,7],
#     "result": [0, 0, 0, 1, 1, 1, 1]
# }

# df = pd.DataFrame(data)
# print(df)

# # Split x and y
# x = df[['hours']]
# y = df['result']

# # model 
# model = LogisticRegression()
# model.fit(x, y)

# # Prediction
# new_data = pd.DataFrame({
#     "hours": [3.4]
# })

# pred_d = model.predict(new_data)
# print("Predicted data is : ", pred_d)

# # Probability prediction
# prob_d = model.predict_proba(new_data)
# print("Probability of fail and pass : ", prob_d)



# KNN :-
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

data = {
    "weight": [100,110,120,170,180,190],
    "fruits": [0, 0, 0, 1, 1, 1] #  0 -> apple and 1 orange
}

df = pd.DataFrame(data)
# print(df)

# Split x and y
x = df[['weight']]
y = df['fruits']

# Model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x, y)

# new data 
u_data = float(input("Enter the weight of fruit: ",))
new_data = pd.DataFrame({
    "weight": [u_data]
})

pred_d = model.predict(new_data)

if pred_d == 0:
    print("Apple")
else:
    print("Orange")