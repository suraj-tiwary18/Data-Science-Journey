# import pandas as pd
# 1d -> method Series

#eg -> 1
# l = [10, 20, 30]
# df = pd.Series(data=l)
# print(df)

#eg -> 2
# d = {"name": "suraj", "age": 21, "roll-no": 123}
# df = pd.Series(data = d, index=["name", "age", "roll-no"])
# print(df)

#Suggestion
# help(pd.Series)
# pd.Series??

#DataFrame
# import pandas as pd
# d = {
#     "name": ["suraj", "sushant", "shivam", "deepak", "varun", "yash"],
#     "roll-no": [12,13,14,15,16,17]
# }
# df = pd.DataFrame(data = d)
# print(df)






# Connecting file :-

# By vs code editor :-

# cvs file :-
# import pandas as pd
# df = pd.read_csv("file2 - Sheet1.csv")
# print(df)

# Excel file :-
# import pandas as pd
# df = pd.read_excel("file2.xlsx")
# print(df)

# json file :-
# import pandas as pd
# df = pd.read_json("file2.json")
# print(df)




# By My_drive:-

# csv file :-
# import pandas as pd
# file_id = "1IkZMcB5glBak0qoPKcr5e1Ez1w_3ns_O"
# url = f"https://drive.google.com/uc?id={file_id}"
# df = pd.read_csv(url)
# print(df)

# Excel file :-
# import pandas as pd
# file_id = "1zWxpLVIL5jwglLqZ0CU4v-taqGewSHq8"
# url = f"https://drive.google.com/uc?id={file_id}"
# df = pd.read_excel(url)
# print(df)

# json file :-
# import pandas as pd
# file_id = "1_L0HptC0OatLdUTUswKW25Dmp3OhAh5m"
# url = f"https://drive.google.com/uc?id={file_id}"
# df = pd.read_json(url)
# print(df)

# This is csv file url link :-  https://drive.google.com/file/d/1IkZMcB5glBak0qoPKcr5e1Ez1w_3ns_O/view?usp=sharing
# This is excel file url link :- https://docs.google.com/spreadsheets/d/1zWxpLVIL5jwglLqZ0CU4v-taqGewSHq8/edit?usp=sharing&ouid=116356984792060427744&rtpof=true&sd=true
# This is json file url link :- https://drive.google.com/file/d/1_L0HptC0OatLdUTUswKW25Dmp3OhAh5m/view?usp=sharing




# By github

# csv file :-
# import pandas as pd
# url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/refs/heads/main/file2%20-%20Sheet1.csv"
# df = pd.read_csv(url)
# print(df)

# excel file :-
# import pandas as pd
# url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/main/file2.xlsx"
# df = pd.read_excel(url)
# print(df)

# json file :-
# import pandas as pd
# url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/main/file2.json"
# df = pd.read_json(url)
# print(df)