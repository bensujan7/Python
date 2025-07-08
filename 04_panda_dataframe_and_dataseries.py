
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(0,16).reshape(4,4),index=["row1", "row2", "row3", "row4"], columns=["column1", "column2", "column3", "column4"])
print(df.head())
df.to_csv('test1.csv')

# ways of accessing the elements:- 1) .loc  2) .iloc
# .loc focuses on row but .iloc focuses on both row and column

print("\n",df.loc["row1"]) 
print(type(df.loc["row1"]))  # it is dataseries because it has series of number

print(df.iloc[0:3,0:2])   # prints 1,2&3 rows and 1&2 column
print(type(df.iloc[0:3,0:2]))   # it is dataframe because it has multiple data in rows and column



# converts DataFrames into arrays
print(df.iloc[:,:3].values)            # [:,:] returns all the values
print(df.iloc[:,:3].values.shape) 
print(df["column2"].value_counts())   # counts the repeatition of the elements of the column
print(df["column3"].unique)           # returns only unique values

data = {
    'Name': ['Alice', 'Bob', None],
    'Age': [25, None, 30],
    'City': ['NY', 'LA', 'Chicago']
}
df1 = pd.DataFrame(data) 


print(df1.isnull().sum())       # it checks every cell and returns true if null else returns false

print(df["column2"])   # directly accessing using column name
print(df[["column2","column3"]])  # can also access multiple column


