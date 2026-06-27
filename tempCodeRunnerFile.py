# Label Encoding
from sklearn.preprocessing import LabelEncoder

# Method -> 1
le = LabelEncoder()
df['colors_encoder1'] = le.fit_transform(df['colors'])
# print(df)

# Method -> 2
df['colors_encoder2'] = LabelEncoder().fit_transform(df['colors'])
print(df)

# Method -> 3
import sklearn
df['colors_encoder3'] = sklearn.preprocessing.LabelEncoder().fit_transform(df['colors'])
print(df)