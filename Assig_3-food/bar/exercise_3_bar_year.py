import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = 'food_imports.csv'
data = pd.read_csv(filename, index_col=0).T
years = data.index.to_list()
values = data.to_numpy().T.tolist()
foods = data.columns.to_numpy().tolist()
years_int = list(map(int, years))
width = .2
ticks = np.arange(0, 80, 4)

# Prints index and first 5 rows of the data frame
print(data.index)
print(data.head())

df2 = pd.DataFrame(data)
df2.plot.bar()

fig, ax = plt.subplots()


def onpick(event):
    indx = int(event.indx)          # Reads index based on x-axis
    thisline = event.artist         # Reads the click artist for data element category
    label = thisline.get_label()    # Recognizes food name on click
    xdata = thisline.get_xdata()    # Recognizes year on click
    ydata = thisline.get_ydata()    # Recognizes value on click
    print('Mouse Pick Point:', label, ' [', xdata[indx], '] ', ' $', ydata[indx], '(In Millions)')


# Plots the figure
ind = np.arange(0, 80, 4)         # from 0 to 80, iterate by 4 (for x-axis spaces)

# for index in range(len(foods)):
#     ax.plot(years, data.iloc[:, index], picker=5, marker='o')

for i in np.arange(0, 15, 1):     # (0, 19, 1) from 0 to 18, iterate by 1
    # print(i)                    # prints 0, 1, ..., 18
    ax.bar(i - 1.5 + width * i, data.iloc[i, 0:19], width, align='edge')
    # ax.bar(years[i], data.iloc[:, i], align='edge')
    # Does this same thing as the one above
    # ax.bar(data.index[i], data.iloc[i, 0:19], width, align='edge')

# Plots the figure axis labels and title
ax.set_title('U.S. Food Imports (Year vs Value)', fontsize=14)
plt.xlabel('Years', fontsize=14)
ax.set_ylabel('Dollar Value in Millions of Dollars', fontsize=14)

plt.xticks(ticks, years)        # Fills xticks with year values from years list

fig.canvas.mpl_connect('pick_event', onpick)

plt.show()
