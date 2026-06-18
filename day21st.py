# Subplots

# 1D Graph:- 

# import matplotlib.pyplot as plt

# # Graph one data
# year = [2010,2015,2020,2025]
# dairy = [100,520,630,400]

# # Graph two data
# year1 = [1990,2000,2005,2010]
# farming = [300,200,250,100]

# fig, aux = plt.subplots(1,2)

# # This is first chart
# aux[0].plot(year, dairy) # first col for line chart
# aux[0].set_xlabel("year")
# aux[0].set_ylabel("dairy")
# aux[0].set_title("dairy production graph")

# # This is second chart
# aux[1].plot(year, dairy) # first col for line chart
# aux[1].set_xlabel("year1")
# aux[1].set_ylabel("farming")
# aux[1].set_title("goods production graph")

# plt.show()


# # 2D Graph:-
# import matplotlib.pyplot as plt

# # Graph 1
# year = [2000,2005,2010,2015]
# google = [100,150,200,250]

# # Graph 2
# microsoft = [110,160,210,260]

# # Graph 3
# apple = [90,140,250,300]

# # Graph 4
# tesla = [80,130,200,260]

# fig, aux = plt.subplots(2,2)

# # Plot Chart
# # fist row and first col
# aux[0][0].plot(year, google)
# aux[0][0].set_xlabel("year")
# aux[0][0].set_ylabel("Revenue")
# aux[0][0].set_title("Revenue of Google")

# # Bar Chart
# # first row and second col
# aux[0][1].bar(year, microsoft)
# aux[0][1].set_xlabel("year")
# aux[0][1].set_ylabel("Revenue")
# aux[0][1].set_title("Revenue of Microsoft")

# # Pie Chart
# # Second row and first col
# aux[1][0].pie(apple, labels=year, startangle=210)
# aux[1][0].set_xlabel("year")
# aux[1][0].set_ylabel("Revenue")
# aux[1][0].set_title("Revenue of Apple")

# # Scatter chart
# # Second row and second col
# aux[1][1].scatter(year, tesla)
# aux[1][1].set_xlabel("year")
# aux[1][1].set_ylabel("Revenue")
# aux[1][1].set_title("Revenue of Tesla")

# plt.tight_layout()
# # plt.show()

# #save this diagram
# # option 1
# plt.gcf().canvas.get_supported_filetypes()
# plt.savefig("subplot.jpg")

# plt.show()




# Mini Project
import pandas as pd
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/refs/heads/main/temperature_data.json"
df = pd.read_json(url)
# print(df)

# Drop Row 3 -> Wednesday
df.dropna(subset=["temperature_c"], inplace=True)
# print(df)

# Fill average value -> humidity -> nan
df.fillna(df["humidity_pct"].mean(), inplace=True)
# print(df)

# new cols -> farenheit | cell+1.8 -> + 32
df["temperature_f"] = (df["temperature_c"] * 1.8)+32
# print(df)

# subplots -> 1d -> line chat | pie chart
fig, aux = plt.subplots(1,2)
aux[0].plot(df["humidity_pct"], df["temperature_c"])
aux[0].set_xlabel("humidity")
aux[0].set_ylabel("temperature in celsius")
aux[0].set_title("Humidity with celsius")

aux[1].pie(df["temperature_f"], labels=df["day"], autopct="%1.1f%%")
aux[1].set_title("Humidity with farenheit")

# Save Image
# plt.savefig("project1.jpg")
plt.show()