import pandas as pd
data_frame = pd.read_csv('./data_2.csv',header=None, names=[
    'Full Name', 
    'Phone Brand', 
    'Username'
    ], index_col='Username')
new_df = data_frame.head(10)
new_df.to_csv('New_data.csv');

exported_data = pd.read_csv('./New_data.csv')

print(exported_data)