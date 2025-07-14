import pandas as pd

# JSON to CSV files

Data = '{"Employee name": "Ben", "Email": "ben1@gmail.com", "Job_profile": [{"Title1": "Team leader", "Title2": "senior developer" }] }'
#Data = json.loads(Data)
df = pd.read_json(Data)

# convert into different json format
df.to_json()
print(df)
df.to_json(orient='records')
print(df)
#df1 = pd.read_csv("wine.data",header= None)
#print(df1)

# url = "https://www.w3schools.com/html/html_tables.asp"
# dfs = pd.read_html(url, match= "Country", header= 0)
# print(dfs) 

url1 = "table.html"
df1 = pd.read_html(url1)
print(df1)