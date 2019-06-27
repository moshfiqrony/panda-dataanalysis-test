import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./data.csv')[['_', '_001']]
new_df = df.head(10).dropna().count()
plt.show()
