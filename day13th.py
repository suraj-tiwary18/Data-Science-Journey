# import pandas as pd
# df = pd.Series([10,20,30])
# print(df)
# print(df[0])


#dict
# import pandas as pd
# dict = {"name":["suraj","sushant","varun","deepak","shivam"],
#         "age":[20,22,21,23,24],
#         "salary":[{"IN-hand":"15000","ctc":"1.21lpa"},{"In-hand":"20000","ctc":"2.21lpa"},
#                   {"IN-hand":"25000","ctc":"3.21lpa"},{"In-hand":"30000","ctc":"3.21lpa"},
#                   {"IN-hand":"40000","ctc":"4.21lpa"}]
#         }

# df = pd.DataFrame(dict)
# print(df)


#eg:-
# import pandas as pd
# dict = {"name":["dheeraj","kunal","praveen","anjali","abhishek singh"],
#         "age":[20,21,22,23,30],
#         "salary":[15000,20000,25000,30000,35000]
#         }
# df = pd.DataFrame(dict) # without DataFrame we can't access pandas method
# print(df)


# csv
# import pandas as pd
# df = pd.read_csv("file1.csv")
# print(df)



# csv
# import pandas as pd
# method of github
# url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/refs/heads/main/file1.csv"
# method of google drive
# file_id = "1IkZMcB5glBak0qoPKcr5e1Ez1w_3ns_O"
# url = f"https://drive.google.com/uc?id={file_id}"
# df = pd.read_csv(url)
# print(df)
# use csv file
# df = pd.read_csv(url)
# print(df)