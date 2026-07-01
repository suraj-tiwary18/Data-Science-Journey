# # Decisition Tree
# # Single decision tree 

# import pandas as pd 
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import mean_absolute_error, accuracy_score

# # Data Set
# data = {
#     "age":[20,22,25,28,30,35,40,45,50,55],
#     "salary":[20000,25000,27000,32000,45000,50000,60000,70000,80000,9000],
#     "buy":[0,0,0,0,1,1,1,1,1,0]
# }

# df = pd.DataFrame(data)
# print(df)

# # Features adn Target
# df = pd.DataFrame(data)
# x = df[['age', 'salary']] # Features
# y = df['buy'] # Target

# # Train Test Split
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# # Model
# model = DecisionTreeClassifier(random_state=42, criterion = 'entropy') # Criterion = gini | entropy
# model.fit(x_train, y_train)

# # # Prediction 
# # new_data = pd.DataFrame({
# #     "age": []
# # })

# y_pred = model.predict(x_test)

# print("actual data", y_test)
# print("Prediction", y_pred)



# # Eg. :-
# import matplotlib.pylab as plt
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import mean_absolute_error, accuracy_score
# import seaborn as sns


# # Data set
# data = {
#     "Age": [22, 25, 30, 35, 28, 40, 45, 23, 32, 27, 38, 29],
#     "Income": [25000, 30000, 45000, 50000, 40000, 70000, 65000, 20000, 55000, 35000, 60000, 42000],
#     "Credit_Score": [650, 700, 720, 750, 680, 800, 780, 600, 730, 690, 770, 710],
#     "Loan_Approved": [
#         "No", "No", "Yes", "Yes",
#         "No", "Yes", "Yes", "No",
#         "Yes", "No", "Yes", "Yes"
#     ]
# }

# df = pd.DataFrame(data)

# # Split data
# x = df[['Age', 'Income', 'Credit_Score',]]
# y = df['Loan_Approved']

# # Train Test Split
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# # Model
# model = DecisionTreeClassifier(random_state=42, criterion= 'entropy')
# model.fit(x_train, y_train)

# # Prediction
# new_data = pd.DataFrame({
#     "Age": [45],
#     "Income": [80000], 
#     "Credit_Score": [1500]
# })

# y_pred = model.predict(new_data)

# print("Predition: ", y_pred[0])

# #Accuracy
# y_test_p = model.predict(x_test)
# print("Accuracy: ", accuracy_score(y_test, y_test_p))


# # Graph :-
# sns.scatterplot(
#     x="Income",
#     y="Credit_Score",
#     hue="Loan_Approved",
#     data=df
# )
# plt.title("Income vs Credit Score")
# plt.show()




# Random Forest
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score # Model Accura

# # Data Set
# data = {
#     "age":[20,22,25,28,30,35,40,45,50,55],
#     "salary":[20000,25000,27000,32000,45000,50000,60000,70000,80000,9000],
#     "buy":[0,0,0,0,1,1,1,1,1,0]
# }

# df = pd.DataFrame(data)
# print(df)

# # Split data 
# x = df[['age', 'salary']]
# y = df['buy']

# # Train Teat Split 
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# # Model 
# model = RandomForestClassifier(random_state=42, n_estimators=10) # n_estimators
# model.fit(x_train, y_train)

# # Prediction
# y_pred = model.predict(x_test)

# print("prediction")
# print(y_pred)
# print("Accuracy")
# print(accuracy_score(y_test, y_pred))




# Confusion Metrics

# from sklearn.metrics import confusion_matrix

# actual = [1, 0, 1, 1, 0, 1, 0, 0]
# pred = [1, 0, 1, 0, 0, 1, 1, 0]

# cm = confusion_matrix(actual, pred)
# print(cm)


# import matplotlib.pyplot as plt
# from sklearn.metrics import ConfusionMatrixDisplay

# ConfusionMatrixDisplay.from_predictions(actual, pred)

# plt.show()



# Precision | recall | f1 score
import pandas as pd
import numpy as np
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix, f1_score

actual = [1, 0, 1, 1, 0, 1 , 0, 0]
pred = [1, 0, 1, 0, 0, 1, 1,  0]

# confusion matrix
cm = confusion_matrix(actual, pred)
print(cm)
precision_s = cm[0][0]/ (cm[0][0]+cm[1][0]) #precision score
print(precision_s) 
# print(3/(3+1)) # precision score


# precision score
# precision = precision_score(actual,pred)
# print(precision)


# Recall 
recall_s = cm[0][0] / (cm[0][0]+cm[0][1]) # Recall Score
print(recall_s)

# F1 Score 
f1 = f1_score(actual, pred)
print(f1)