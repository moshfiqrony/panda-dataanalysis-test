import pandas as pd

df = pd.read_csv('./data.csv')

#reading accessing specific field and create a new data_frame and export to csv
new_df = df.head(3)
#conditional data framing
#in this section the data frame will be showing the 3 
# collumns and based on the given conditions

print(new_df[['_', '_001', '_002/price']][new_df['_002/price'] == True])