


import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(0,16).reshape(4,4),index=["row1", "row2", "row3", "row4"], columns=["column1", "column2", "column3", "column4"])
print(df.head())
