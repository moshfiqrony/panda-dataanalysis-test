import pandas as pd
import numpy as np

df = pd.read_csv('weather_by_cities.csv')

print(df)

grouped_data = df.groupby('city')

for city, city_df in grouped_data:
    print(city)
    print(city_df)



