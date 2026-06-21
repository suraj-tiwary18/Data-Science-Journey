
# # Create First Chart
# import matplotlib.pyplot as plt # visualization
# x = [2010, 2015, 2020, 2025] # x cord
# y = [100, 200, 250, 300] # y cord
# plt.bar(x, y) #Line graph
# plt.xlabel("years") # x label
# plt.ylabel("sales") # y label
# plt.title("sales report") # graph title
# plt.show() # graph show


# practice
# import matplotlib.pyplot as plt
# x = [2010, 2015, 2020, 2025] # x cord
# y = [100, 200, 250, 300] # y cord

# # graph size
# plt.figure(figsize=(6, 2)) # width or height
# plt.plot(x, y, color="b", marker="o", linestyle="dashed", linewidth=4, markersize = 14, )
# plt.show()








# import matplotlib.pyplot as plt
# x = [2010,2015,2020,2025] # x cord
# y = [100,200,250,300] # y cord.
 
# #
# # **Markers**
 
# # |character      |  |  |description |
# # |-------------|  -------------------------------|
# # |'.'       | | |point marker|
# # |','       | | |pixel marker|
# # |'o'       | | |circle marker|
# # |'v'       | | |triangle_down marker|
# # |'^'       | | |triangle_up marker|
# # |'<'       | | |triangle_left marker|
# # |'>'       | | |triangle_right marker|
# # |'1'       | | |tri_down marker|
# # |'2'       | | |tri_up marker|
# # |'3'       | | |tri_left marker|
# # |'4'       | | |tri_right marker|
# # |'8'       | | |octagon marker|
# # |'s'       | | |square marker|
# # |'p'       | | |pentagon marker|
# # |'P'       | | |plus (filled) marker|
# # |'*'       | | |star marker|
# # |'h'       | | |hexagon1 marker|
# # |'H'       | | |hexagon2 marker|
# # |'+'       | | |plus marker|
# # |'x'       | | |x marker|
# # |'X'       | | |x (filled) marker|
# # |'D'       | | |diamond marker|
# # |'d'       | | |thin_diamond marker|
# # |'|'       | | |vline marker|
# # |'_'       | | |hline marker|
 
# # **Line Styles**
 
# # |character      |  |  |  |description |
# # |-------------|   -------------------------------|
# # |'-'       | | | |solid line style|
# # |'--'      | | | |dashed line style|
# # |'-.'      | | | |dash-dot line style|
# # |':'       | | | |dotted line style|
 
# # Example format strings:
 
# #     'b'    # blue markers with default shape
# #     'or'   # red circles
# #     '-g'   # green solid line
# #     '--'   # dashed line with default color
# #     '^k:'  # black triangle_up markers connected by a dotted line
# # **Colors**
 
# # |character      |  |  |  |color |
# # |-------------|   -------------------------------|
# # |'b'       | | | |blue|
# # |'g'       | | | |green|
# # |'r'       | | | |red|
# # |'c'       | | | |cyan|
# # |'m'       | | | |magenta|
# # |'y'       | | | |yellow|
# # |'k'       | | | |black|
# # |'w'       | | | |white|
# # graph size
# plt.figure(figsize=(6,2)) # width or height
# plt.plot(x,y,color="y",marker='*',linestyle=":",linewidth=4,markersize=14)
# plt.show()






# Mult Line Chart
# import matplotlib.pyplot as plt

# x = [2010, 2015, 2020, 2025]
# y1 = [100, 200, 260, 500]
# y2 = [150, 185, 195, 400]

# plt.plot(x, y1, label="jeans")
# plt.plot(x, y2, label="shirt")
# plt.legend() # info of label
# plt.show()



# Question -> 1
# import matplotlib.pyplot as plt

# years = [2020, 2021, 2022, 2023, 2024, 2025]

# google = [180, 210, 260, 300, 350, 410]
# microsoft = [140, 168, 198, 230, 280, 340]
# amazon = [220, 250, 290, 330, 390, 450]
# apple = [190, 220, 270, 320, 380, 460]
# tesla = [30, 50, 80, 120, 170, 240]

# plt.figure(figsize=(10, 5)) # width or height

# plt.plot(years, google, marker='o', label='Google')
# plt.plot(years, microsoft, marker='o', label='Microsoft')
# plt.plot(years, amazon, marker='o', label='Amazon')
# plt.plot(years, apple, marker='o', label='Apple')
# plt.plot(years, tesla, marker='o', label='Tesla')
# plt.xlabel("Years")
# plt.ylabel("Revenue")
# plt.title("Revenue Growth of Top Tech Companies (2020-2025)")

# plt.legend()
# plt.show()



# Bar Chart
# import matplotlib.pyplot as plt
# x = [2015, 2020, 2025, 2030]
# y = [100,150,200,290]

# # size
# plt.figure(figsize=(6,2)) 
# plt.bar(x,y)
# plt.show()



#Question -> 2 (# mult bar chart)
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([1,2,3,4])
# y1 = [10, 20, 20, 40]
# y2 = [20, 30, 25, 30]
# # calculation -> width
# w = 0.40
# plt.bar(x - w/2,y1, label='boys', width=w) #hide second #/2 iss liye lgaya kyu ki do bar bana rhe hn toh hmne ye 
# plt.bar(x + w/2,y2, label="girl",width=w) # show 

# plt.xlabel("groups")
# plt.ylabel("number of students")
# plt.title("No. of student in Each Group")
# plt.legend()
# plt.show()
# # we import numpy because "x - w/2" works on array