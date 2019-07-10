import pandas as pd
import numpy as np

df = pd.read_csv('weather.csv');


print(df)

print('\n------------------------------------------------------------------------------------')

repl_df = df.replace(-9999, np.NaN)
print(repl_df)

print('\n------------------------------------------------------------------------------------')

repl_2_df = repl_df.replace(-99999, np.NaN)
print(repl_2_df)

















