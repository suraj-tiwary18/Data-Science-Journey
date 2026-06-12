# import pandas as pd
# url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/refs/heads/main/student-data.json"
# df = pd.read_json(url)
# print(df)

# By default Ascending
# df.sort_values("english")
# print(df)

# By default asecnding method 1
# print(df.sort_values(by=["english"], ascending=False))

# Decending
# df.sort_values("english", ascending=False, inplace=True)
# print(df)

# Multiple cols sort
# print(df.sort_values(by=["english","maths"], ascending=[False, True]))

# Sort According to name
# a to z
# df["name"] = df["name"].str.lower()
# print(df.sort_values("name"))



# Operations :-

# Add column total = py+maths+english
# Total_Cols = df["Total"] = df["physics"] + df["maths"] + df["english"]
# print(Total_Cols)

# add row
# df.loc[14] = ["suraj", "Male", 80, 70, 70, 220]
# print(df)

# Update column

# Update row

# Delete column
# print(df.drop(14, axis=0))

# Delete row and column 
# df.drop()


# New data set 
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
print(df)

# Adding new column
df["doj"] = ['2025-01-10','2025-02-10','2025-03-10','2025-04-10','2025-05-10']
# print(df["doj"].dtype)

# convert string to date
df["doj"] = pd.to_datetime(df["doj"])
print(df["doj"].dtype)

# Date operation
print(df["doj"].dt.year)
print(df["doj"].dt.month)
print(df["doj"].dt.day)
print(df["doj"].dt.day_name())


# 20 days
print(df["doj"] + pd.to_timedelta("20 days"))
# print(df["doj"] + pd.to_timedelta(20, unit="D"))
