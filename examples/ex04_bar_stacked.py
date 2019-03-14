#!/usr/bin/python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
width = 0.35       # the width of the bars: can also be len(x) sequence
ind = np.arange(N)    # the x locations for the groups
xlabel_offset = 0.17  #width / 2.0  # to center xlabels on the bar
print("Offest is: ",xlabel_offset)
indX = np.arange(xlabel_offset,N,1)  #where to put the x-axis labels

p1 = plt.bar(ind, menMeans, width, color='#d62728', yerr=menStd)
p2 = plt.bar(ind, womenMeans, width, color='#d6c228',
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
#plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.xticks(indX, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()
