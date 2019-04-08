import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches
from matplotlib.table import Cell

year = []
ytotal = []
ydict = {}
month = []
mtotal = []
day = []

year_text = ""

counter = 0

with open("terrordata.csv","r") as data:
    csvfile = csv.reader(data, delimiter = ',')
    next(csvfile)
    for row in csvfile:
        year.append(int(row[0]))
        month.append(int(row[1]))
        day.append(int(row[2]))

#print(year[0])
#print(year.count('1970'))

for y,x in zip(range(1970, 2018),range(12,600,12)):
    #print(y)
    #print(year.count(y))
    ytotal.append(year.count(y))
    ydict[y] = x


for t in ytotal:
    x = counter + t
    for m in range(1,13):
        mtotal.append(month[counter:x].count(m))
    counter = counter + t

#print(mtotal)


print('Enter a year from 1970 to 2017: ')
p = int(input())

if p in ydict:
    year_text = str(p)
    if p == 1970:
        a = ydict[p]
        #print('Printing a: ' + str(a))
        testM = mtotal[0:a] 
    else:
        b = ydict[p]
        a = ydict[p-1]
        testM = mtotal[a:b]
else:
    print('Not a valid year, try again')
    quit()



mL = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
shapes = {}

c = np.arange(1,6)
norm = mpl.colors.Normalize(vmin=c.min(), vmax=c.max())
cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.Reds)
cmap.set_array([])
colors = ['r','g','b','r','g','b','r','g','b','r','g','b']


swX = 2.5         # starting x coord for first rectangle
swY = 5.0         # starting y coord for first rectangle




# class that defines a rectangle object (one per data item)
class Rect:

    def __init__(self, num, who, facecolor='#7777CC', sw_corner=(0.0, 0.0), height=0, width=0):
        self.num = num   # num is value (area of a rectangle)
        self.mL = who
        self.sw_corner = sw_corner
        self.height = height
        self.width = width
        self.rect = Cell(sw_corner, width, height, edgecolor='#000000', facecolor=facecolor)
        self.rect._loc = 'center'
        # self.rect.angle = 45.0
        label = "{0}".format(who)
        self.rect.get_text().set_text(label)
        self.rect.set_gid(who)

    def get_patch(self):
        return self.rect


def __init():
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)




def get_next_color(v):       # cycles through colors
    vls = v/100
    if vls < 0.25:
        face = cmap.to_rgba(1)

    elif vls < 0.5:
        face = cmap.to_rgba(1.5)

    elif vls < 1:
        face = cmap.to_rgba(2)
    
    elif vls < 3:
        face = cmap.to_rgba(2.5)
    
    elif vls < 6:
        face = cmap.to_rgba(3)
    
    elif vls < 9:
        face = cmap.to_rgba(3.5)
     
    elif vls < 12:
        face = cmap.to_rgba(4)
     
    elif vls < 15:
        face = cmap.to_rgba(4.5)
     
    elif vls < 18:
        face = cmap.to_rgba(5)
     
    elif vls < 21:
        face = cmap.to_rgba(5.5)
   
    else:
        face = cmap.to_rgba(6)
    return face


def build():        # Build the rectangles and attach to axis
    nc = 0
    nv = 0
    width = 1
    curr_x = swX
    while len(testM) > 0:
        curr_y = swY

        rsum = 0.0
        vals = []       # list of rectangles to stack into one column
        while True:     # gather values to make into a column of rectangles
            val = testM.pop(0)
            vals.append(val)
            if len(testM) == 0: 
                break

        for v in vals:      # create the rectangles in this column
            name = mL.pop(0)
            height = 1
            shapes[name] = Rect(v, name, facecolor=get_next_color(v), sw_corner=(curr_x, curr_y),
                                height=height, width=width)
            mL.append(name)
            curr_x += width
            nc+=1
            if nc % 4 ==0 :
                curr_x = swX
                curr_y -= height




fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.axis("equal")    # so squares will look square
xlabel = ax.text(0.5,0.95,"Heatmap of Terrorism incidents in " + year_text,bbox={'facecolor':'w','alpha':0.5,'pad':5},transform=ax.transAxes,ha="center")



bbSW = (swX, swY)   # coordinates of sw corner of bounding box
build()   # create patches at specific locations



map1 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(1))
map2 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(1.5))
map3 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(2))
map4 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(2.5))
map5 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(3))
map6 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(3.5))
map7 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(4))
map8 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(4.5))
map9 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(5))
map10 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(5.5))
map11 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(6))

labels = ['Less than 1.5%', 'Less than 2%', 'Less than 2.5%', 'Less than 3%', 'Less than 4%', 'Less than 6%', 'Less than 8%', 'Less than 9%', 'Less than 10%', 'Less than 11%', 'Less than 12%', '13% or more' ]

ax.legend([map1, map2, map3, map4, map5, map6, map7, map8, map9, map10, map11],
                  labels, loc ='center right', fancybox=True)




#ani = animation.FuncAnimation(fig, animate, frames=tf_am, init_func=init,
#                              interval=FRAME_DELTA, repeat=True, blit=True)


for rt in shapes.values():  # add all of the rectangles to the axis for rendering
    mp = rt.get_patch()
    ax.add_patch(mp)
    mp.set_picker(3)

plt.xticks(range(0,10))
plt.yticks(range(0,10))
ax.set_ylim(bottom=0)
ax.set_xlim(left=0)
plt.show()
