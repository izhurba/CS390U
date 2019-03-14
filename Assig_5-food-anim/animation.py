import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.animation as animation
import csv
from matplotlib.widgets import Slider

count = 0
pause = True
FRAME_DELTA = 1000       # milliseconds
fig, ax = plt.subplots()
rwidth = 1      # rectangle's width
rheight = 2     # rectangle's height

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

years.remove('Category')     

for thing in amounts:
    thing = [x.replace(',','') for x in thing]
    f_am.append(thing)
#years = np.array(years).astype(int)
f_am = np.asarray(f_am, dtype = float)
tf_am = np.transpose(f_am)
nlist = f_am[0].tolist()
#print(nlist)

xlabel = ax.text(0.5,0.9,"",bbox={'facecolor':'w','alpha':0.5,'pad':5},transform=ax.transAxes,ha="center")


rect = Rectangle((0, 0), rwidth, rheight)
rect1 = Rectangle((1, 0), rwidth, rheight)
rect2 = Rectangle((2, 0), rwidth, rheight)
rect3 = Rectangle((3, 0), rwidth, rheight)
rect4 = Rectangle((4, 0), rwidth, rheight)
rect5 = Rectangle((5, 0), rwidth, rheight)
rect6 = Rectangle((6, 0), rwidth, rheight)
rect7 = Rectangle((7, 0), rwidth, rheight)
rect8 = Rectangle((8, 0), rwidth, rheight)
rect9 = Rectangle((9, 0), rwidth, rheight)
rect10 = Rectangle((10, 0), rwidth, rheight)
rect11 = Rectangle((11, 0), rwidth, rheight)
rect12 = Rectangle((12, 0), rwidth, rheight)
rect13 = Rectangle((13, 0), rwidth, rheight)
rect14 = Rectangle((14, 0), rwidth, rheight)


def init():                     # init function for the animation
    global count
    count = 0
    top_y = max(map(max,f_am))
    top_y = top_y + (top_y/4)
    ax.set_xlim(0.0, 15.0)
    ax.set_ylim(0.0,top_y)
    rect.set_color('#00ffcc')
    rect1.set_color('#00ffcc')
    rect2.set_color('#00ffcc')
    rect3.set_color('#00ffcc')
    rect4.set_color('#00ffcc')
    rect5.set_color('#00ffcc')
    rect6.set_color('#00ffcc')
    rect7.set_color('#00ffcc')
    rect8.set_color('#00ffcc')
    rect9.set_color('#00ffcc')
    rect10.set_color('#00ffcc')
    rect11.set_color('#00ffcc')
    rect12.set_color('#00ffcc')
    rect13.set_color('#00ffcc')
    rect14.set_color('#00ffcc')
    
    ax.add_patch(rect)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rect3)
    ax.add_patch(rect4)   
    ax.add_patch(rect5)
    ax.add_patch(rect6)
    ax.add_patch(rect7)
    ax.add_patch(rect8)
    ax.add_patch(rect9)    
    ax.add_patch(rect10)
    ax.add_patch(rect11)
    ax.add_patch(rect12)
    ax.add_patch(rect13)
    ax.add_patch(rect14)  

    xlabel.set_text(years[0])

    return xlabel, rect, rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10, rect11, rect12, rect13, rect14, 


def animate(num):           # called each frame with rectangle height
    global count

    rect.set_height(num[0])
    rect1.set_height(num[1])
    rect2.set_height(num[2])
    rect3.set_height(num[3])
    rect4.set_height(num[4])
    rect5.set_height(num[5])
    rect6.set_height(num[6])
    rect7.set_height(num[7])
    rect8.set_height(num[8])
    rect9.set_height(num[9])
    rect10.set_height(num[10])
    rect11.set_height(num[11])
    rect12.set_height(num[12])
    rect13.set_height(num[13])
    rect14.set_height(num[14])
    
    #print(num)
    b = num[0]
    #print(b)
    a = nlist.index(b)

    #print(years[a])
    xlabel.set_text(years[a])
    count += 1

    return xlabel, rect, rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10, rect11, rect12, rect13, rect14, 
def onClick(event):
    global pause
    if pause:
        ani.event_source.start()
        pause = False
    else:
        ani.event_source.stop()
        pause = True

fig.canvas.mpl_connect('button_press_event',onClick)

ani = animation.FuncAnimation(fig, animate, frames=tf_am, init_func=init,
                              interval=FRAME_DELTA, repeat=False, blit=True)

ind = np.arange(15) + (rwidth/2)

plt.xticks(ind,labels[0:14], rotation = 23)
plt.ylabel("Amounts")
plt.show()
