# # Clustering :-

# import pandas as pd
# from sklearn.cluster import KMeans

# data = {
#     "age": [22, 25, 24, 45, 50, 48, 20, 47],
#     "income": [22000, 25000, 24000, 45000, 50000, 48000, 20000, 47000]
# }

# df = pd.DataFrame(data)
# print(df)

# # Input (feature)
# X = df[['age', 'income']]

# # Model
# model = KMeans(n_clusters=2, random_state=42) # n_clusters divides the data into 2 parts
# model.fit(X)

# # Clusters 
# clusters = model.labels_ # 0 is defining the young age and 1 is define the older age
# print(clusters)
# df['cluster'] = clusters # adding new columns "cluster"
# print(df)




# # Eg :-
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans

# data = {
#     "age": [22, 25, 24, 45, 50, 48, 20, 47],
#     "income": [22000, 25000, 24000, 45000, 50000, 48000, 20000, 47000]
# }

# df = pd.DataFrame(data)
# print(df)

# # Input
# X = df[['age', 'income']]

# # Model
# model = KMeans(n_clusters=2, random_state=42)
# model.fit(X)

# # Clusters
# df['cluster'] = model.labels_

# # Graphs  :-
# plt.scatter(df['age'], df['income'], c=df['cluster'])
# plt.xlabel('age')
# plt.ylabel('income')
# plt.title("Group the Data")
# plt.show()

# Eg :-
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = {
    "Name": [
        "Aman", "Rohit", "Priya", "Neha",
        "Rahul", "Simran", "Arjun", "Sneha"
    ],
    "Height": [
        150, 152, 155, 168,
        170, 172, 185, 188
    ],
    "Weight": [
        45, 47, 50, 65,
        68, 70, 90, 92
    ]
}

df = pd.DataFrame(data)

# Input
X = df[[ 'Height', 'Weight']]

# Model
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

# Cluster
df['Cluster'] = model.labels_

# Graph :-
plt.scatter(df['Height'], df['Weight'],  c=df['Cluster'])
plt.ylabel('Height')
plt.ylabel("Weight")
plt.title("Group the Data")
plt.show()