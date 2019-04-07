import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches
from matplotlib.table import Cell


year = []
ytotal = []
month = []
mtotal = []
day = []

c = np.arange(1, 6)
norm = mpl.colors.Normalize(vmin=c.min(), vmax=c.max())
cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.PuBu)
cmap.set_array([])

cmap.to_rgba(4.5)

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

for y in range(1970, 2018):
    #print(y)
    #print(year.count(y))
    ytotal.append(year.count(y))


for t in ytotal:
    x = counter + t
    for m in range(1,13):
        mtotal.append(month[counter:x].count(m))
    counter = counter + t
print(mtotal)



popup_spot = (110, 200)  # location for messages on screen
ratio = 0.15             # skinniest aspect ratio allowed for internal rectangles
colors = ['r', 'g', 'b', 'c', 'm', '#DEAAF4', '#CCCCCC', 'y']
data = [90, 50, 480.0, 30, 20, 181.2, 67.7, 19, 362]
person = ["Ann", "Bob", "Cal", "Dee", "Eve", "Fay", "Guy", "Hal", "Ivy"]
shapes = {}         # holds sub-rectangles indexed by name
size_limit = 300.0       # used for zooming figure for viewing
largest = max(data)
factor = size_limit / np.sqrt(largest)      # scaling factor for viewing

swX = 20.0         # starting x coord for first rectangle
swY = 70.0         # starting y coord for first rectangle
bbArea = factor*sum(data)           # area of bounding rectangle
thickness = np.sqrt(bbArea) * 0.77  # width of bounding rectangle


# class that defines a rectangle object (one per data item)
class Rect:

    def __init__(self, num, who, facecolor='#7777CC', sw_corner=(0.0, 0.0), height=10.0, width=10.0):
        self.num = num   # num is value (area of a rectangle)
        self.name = who
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
    fig.suptitle("Rectangles", fontsize=16)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.ylim((0, 280))
    plt.xlim((0, 270))


def get_next_color():       # cycles through colors
    c = colors.pop(0)
    colors.append(c)
    return c


def build():        # Build the rectangles and attach to axis
    thicksq = thickness * thickness
    width = 0
    curr_x = swX
    while len(data) > 0:
        curr_y = swY
        curr_x += width
        rsum = 0.0
        vals = []       # list of rectangles to stack into one column
        while True:     # gather values to make into a column of rectangles
            val = data.pop(0)
            rsum += val * factor
            vals.append(val)
            if len(data) == 0 or rsum / thicksq >= ratio:
                break
        width = rsum / thickness    # column width
        for v in vals:      # create the rectangles in this column
            name = person.pop(0)
            height = thickness * factor * v / rsum
            shapes[name] = Rect(v, name, facecolor=get_next_color(), sw_corner=(curr_x, curr_y),
                                height=height, width=width)
            curr_y += height



fig = plt.figure(figsize=(10, 7))
ax = fig.add_axes([0.05, 0.05, .90, .9], frameon=False)
ax.axis("equal")    # so squares will look square



bbSW = (swX, swY)   # coordinates of sw corner of bounding box
build()   # create patches at specific locations

for rt in shapes.values():  # add all of the rectangles to the axis for rendering
    mp = rt.get_patch()
    ax.add_patch(mp)
    mp.set_picker(3)






ani = animation.FuncAnimation(fig, animate, frames=tf_am, init_func=init,
                              interval=FRAME_DELTA, repeat=True, blit=True)



plt.show()
