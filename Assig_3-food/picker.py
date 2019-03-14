import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib.widgets import CheckButtons

labels = []
years = []
amounts = []
f_am = []

with open('food_imports.csv','r') as csvData:
    csvfile = csv.reader(csvData, delimiter = ",")
    years = next(csvfile)
    for row in csvfile:
        labels.append(row[0])
        amounts.append(row[1:])

     
years.remove('Category')

#amounts = np.array(amounts)
for thing in amounts:
    thing = [x.replace(',','') for x in thing]
    f_am.append(thing)

f_am = np.asarray(f_am, dtype = float)
#print(*amounts)
#f_am = np.ndarray.astype(amounts, float)
#print(type(f_am))


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Food Imports')
ax.set_xlabel('Years')
ax.set_ylabel('Thousands of Dollars')



l1, = ax.plot(years, f_am[0], 'o', linestyle = '-', label = labels[0], picker=2)  # 5 points tolerance
l2, = ax.plot(years, f_am[1], 'o', linestyle = '-', label = labels[1], picker=2)  # 5 points tolerance
l3, = ax.plot(years, f_am[2], 'o', linestyle = '-', label = labels[2], picker=2)  # 5 points tolerance
l4, = ax.plot(years, f_am[3], 'o', linestyle = '-', label = labels[3], picker=2)  # 5 points tolerance
l5, = ax.plot(years, f_am[4], 'o', linestyle = '-', label = labels[4], picker=2)  # 5 points tolerance
l6, = ax.plot(years, f_am[5], 'o', linestyle = '-', label = labels[5], picker=2)  # 5 points tolerance
l7, = ax.plot(years, f_am[6], 'o', linestyle = '-', label = labels[6], picker=2)  # 5 points tolerance
l8, = ax.plot(years, f_am[7], 'o', linestyle = '-', label = labels[7], picker=2)  # 5 points tolerance
l9, = ax.plot(years, f_am[8], 'o', linestyle = '-', label = labels[8], picker=2)  # 5 points tolerance
l10, = ax.plot(years, f_am[9], 'o', linestyle = '-', label = labels[9], picker=2)  # 5 points tolerance
l11, = ax.plot(years, f_am[10], 'o', linestyle = '-', label = labels[10], picker=2)  # 5 points tolerance
l12, = ax.plot(years, f_am[11], 'o', linestyle = '-', label = labels[11], picker=2)  # 5 points tolerance
l13, = ax.plot(years, f_am[12], 'o', linestyle = '-', label = labels[12], picker=2)  # 5 points tolerance
l14, = ax.plot(years, f_am[13], 'o', linestyle = '-', label = labels[13], picker=2)  # 5 points tolerance
l15, = ax.plot(years, f_am[14], 'o', linestyle = '-', label = labels[14], picker=2)  # 5 points tolerance

plt.subplots_adjust(left=0.07, right = 0.80)

lines = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15] 

leg = ax.legend(loc='upper center', bbox_to_anchor=(1.12, 0.9), fancybox = True, shadow = True)
leg.get_frame().set_alpha(0.4)

lined = dict()
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(5)
    lined[legline] = origline



'''
rax = plt.axes([0.82, .3, 0.16, 0.5])
labs = [str(line.get_label()) for line in lines]
vis = [line.get_visible() for line in lines]
check = CheckButtons(rax, labs, vis)


def func(label):
    index = labs.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()
'''
def onpick(event):
    if event.artist in lined.keys():
        legline = event.artist
        origline = lined[legline]
        vis = not origline.get_visible()
        origline.set_visible(vis)
        if vis:
            legline.set_alpha(1.0)
        else:
            legline.set_alpha(0.2)
        fig.canvas.draw()
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    lbl = thisline.get_label()
    ind = event.ind
    points = tuple(zip(xdata[ind], ydata[ind]))
    print(lbl + " values are: ", points)


'''
def secpick(self, event):
    if event.artist in self.lined.keys():
        legline = event.artist
        origline = lined[legline]
        vis = not origline.get_visible()
        origline.set_visible(vis)
        if vis:
            legline.set_alpha(1.0)
        else:
            legline.set_alpha(0.2)
        fig.canvas.draw()
'''
#fig.canvas.mpl_connect('pick_event', secpick)
fig.canvas.mpl_connect('pick_event', onpick)

#check.on_clicked(func)

plt.show()

