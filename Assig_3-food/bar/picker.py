import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib.widgets import Slider

labels = []
years = []
amounts = []
f_am = []
i_am = []


with open('food_imports.csv','r') as csvData:
    csvfile = csv.reader(csvData, delimiter = ",")
    years = next(csvfile)
    for row in csvfile:
        labels.append(row[0])
        amounts.append(row[1:])

     

#amounts = np.array(amounts)
for thing in amounts:
    thing = [x.replace(',','') for x in thing]
    f_am.append(thing)
years = np.array(years).astype(int)
f_am = np.asarray(f_am, dtype = float)
i_am = np.array(f_am).astype(int)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Food Imports')
ax.set_xlabel('Years')
ax.set_ylabel('Thousands of Dollars')






width = 0.2
xlabel_offset = 0.1
ind = np.arange(len(labels))
indX = np.arange(xlabel_offset, len(labels), 1)

print(type(years[0]))
print(np.shape(ind))
print(np.shape(i_am[0,:]))
#for i in i_am:
l1, = ax.bar(years,i_am) 



#axcolor = 'lightgoldenrodyellow'
#axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
#axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

#sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0, valstep=delta_f)
#samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)


#def update(val):
#    amp = samp.val
#    freq = sfreq.val
#    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
#    fig.canvas.draw_idle()
#sfreq.on_changed(update)
#samp.on_changed(update)

#resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
#button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


#def reset(event):
#    sfreq.reset()
#    samp.reset()
#button.on_clicked(reset)




#plt.subplots_adjust(left=0.07, right = 0.80)

#lines = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15] 

#leg = ax.legend(loc='upper center', bbox_to_anchor=(1.12, 0.9), fancybox = true, shadow = true)
#leg.get_frame().set_alpha(0.4)

#lined = dict()
#for legline, origline in zip(leg.get_lines(), lines):
#    legline.set_picker(5)
#    lined[legline] = origline



#def onpick(event):
#    if event.artist in lined.keys():
#        legline = event.artist
#        origline = lined[legline]
#        vis = not origline.get_visible()
#        origline.set_visible(vis)
#        if vis:
#            legline.set_alpha(1.0)
#        else:
#            legline.set_alpha(0.2)
#        fig.canvas.draw()
#    thisline = event.artist
#    xdata = thisline.get_xdata()
#    ydata = thisline.get_ydata()
#    lbl = thisline.get_label()
#    ind = event.ind
#    points = tuple(zip(xdata[ind], ydata[ind]))
#    print(lbl + " values are: ", points)


#fig.canvas.mpl_connect('pick_event', onpick)


plt.show()
