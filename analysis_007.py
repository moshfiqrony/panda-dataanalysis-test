import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('weather_by_cities.csv')

print(df)

grouped_data = df.groupby('city')

for city, city_df in grouped_data:
    print(city)
    print(city_df)


n_df = grouped_data.get_group('mumbai')
print(n_df)
print(grouped_data.max())
print(grouped_data.mean())
print(grouped_data.describe())
print(grouped_data.mean())


