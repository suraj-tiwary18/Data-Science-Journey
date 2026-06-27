import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/refs/heads/main/moviesTMBD.csv"
df = pd.read_csv(url)

# handle missing values
df.drop(['overview', 'adult', 'title', 'original_language', 'release_date', 'Unnamed', 'id'], axis = 1, inplace = True, errors = 'ignore')

# feature scaling
scaler = StandardScaler()
df[['popularity', 'vote_average']] = scaler.fit_transform(df[[ 'popularity', 'vote_average']])
# print(df)

# split data 
X = df[['popularity', 'vote_average']]
y = df["vote_count"]

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

# Model Train
model = LinearRegression()
model.fit(x_train, y_train)


popu = int(input("Enter Popularity : "))
avg_vote = int(input("Enter Avg. Vote: "))

new_data = pd.DataFrame({
    "popularity": [popu],
    "vote_average": [avg_vote]
})

# Feature Scaling
new_data[['popularity', 'vote_average']] = scaler.transform(new_data[['popularity', 'vote_average']])

# Prediction
predict_data = model.predict(new_data)
print(f"Predicted value is : {predict_data[0]:.2f}")

# graphs :- 

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

sns.scatterplot(x=df['vote_average'], y=df['vote_count'])
plt.show()

sns.scatterplot(x=df['popularity'], y=df['vote_count'])
plt.show()

sns.histplot(df['vote_count'], kde=True)
plt.show()

# Model Dump
joblib.dump(model, "house_model.joblib")