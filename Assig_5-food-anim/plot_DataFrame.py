import matplotlib.pyplot as plt
import pandas as pd

filename = 'food_imports.csv'
data_year = pd.read_csv(filename, index_col=0).T

df2 = pd.DataFrame(data_year)
df2.plot.bar()

data_food = pd.read_csv(filename, index_col=0)

df3 = pd.DataFrame(data_food)
df3.plot.bar()

plt.show()
