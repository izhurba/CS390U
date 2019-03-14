#!/usr/bin/python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import csv
from matplotlib import style
style.use('ggplot')

days = []
watts = []

with open('June2017.csv', 'r') as fil:
    data = csv.reader(fil, delimiter=',')
    next(data)
    for row in data:
        days.append(row[0])
        watts.append(row[1])

watts = np.asarray(watts, dtype=float)
days = mdates.datestr2num(days)

fig,ax = plt.subplots()
ax.plot(days,watts)

plt.title('Solar Data from June 2017')
plt.ylabel('Watts')
plt.xlabel('Days')
xfmt = mdates.DateFormatter('%m/%d/%Y %H:%M')
ax.xaxis.set_major_formatter(xfmt)

fig.autofmt_xdate()
plt.show()
