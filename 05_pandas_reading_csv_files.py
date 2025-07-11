import pandas as pd
import numpy as np
from io import StringIO, BytesIO

data = ('col1,col2,col3\n',
        'a,3,c\n',
        '2,b,s')
csv_string = ''.join(data)             # joins the tuple into single string
df=pd.read_csv(StringIO(csv_string))   
print(df)
df.to_csv("test1.csv")        # writes the dataframe to a csv file

# read from specific column
df = pd.read_csv(StringIO(csv_string),usecols=["col1","col3"])
print(df)

#specifying column datatypes
data1 = ('a,b,c,d\n',
         '0,1,2,3\n',
         '4,5,6,7\n',
         '8,9,10,11')
data1_s = ''.join(data1)
df1 = pd.read_csv(StringIO(data1_s),dtype=int)     
print(df1)
print(df1["a"])    # prints column a
df2=pd.read_csv(StringIO(data1_s),dtype={'a':int,'b':float,'c':'Int64'})
print(type(df2['a'][1]))
print(df2.dtypes)           # gives datatype of all column


# index columns and delimiter
df3 = pd.read_csv(StringIO(data1_s),index_col=0)   # if you give col=1, it makes second column as index 
print(df3)
df4 = pd.read_csv(StringIO(data1_s))
print(df4)                  



