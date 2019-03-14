import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = 'food_imports.csv'
data = pd.read_csv(filename, index_col=0).T
years = data.index.to_list()
values = data.to_numpy().T.tolist()
foods = data.columns.to_numpy().tolist()
years = list(map(int, years))

width = .2

fig, ax = plt.subplots()


def onpick(event):
    indx = int(event.indx)            # Reads index based on x-axis
    thisline = event.artist         # Reads the click artist for data element category
    label = thisline.get_label()    # Recognizes food name on click
    xdata = thisline.get_xdata()    # Recognizes year on click
    ydata = thisline.get_ydata()    # Recognizes value on click
    print('Mouse Pick Point:', label, ' [', xdata[ind], '] ', ' $', ydata[ind], '(In Millions)')


x_vals = np.arange(len(years))

ind = np.arange(0, 75, 5)
for i in np.arange(0, 15, 1):
    p1 = ax.bar(ind - 1.5 + width * i, data.iloc[i, 0:15], width, align='edge')


# Plots the figure axis labels and title
ax.set_title('U.S. Food Imports (Year vs Value)', fontsize=14)
plt.xlabel('Years', fontsize=14)
ax.set_ylabel('Dollar Value in Millions of Dollars', fontsize=14)
ticks = np.arange(0, 75, 5)
# plt.xticks(ticks, ['A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'A'])
plt.xticks(ticks, foods)


fig.canvas.mpl_connect('pick_event', onpick)


plt.show()
