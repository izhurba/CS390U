import cartopy.crs as ccrs
import cartopy.io.shapereader as shp_reader
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import numpy as np
import csv


states = []
numbs = []
data_dict = {}

with open("opioidData.txt","r") as data:
    reader = csv.reader(data, delimiter=':')
    for row in reader:
        states.append(row[0].rstrip())
        numbs.append(float(row[1]))

for i in range(50):
    data_dict.setdefault(states[i],numbs[i])

print(states)
print(numbs)
print(data_dict)

fig = plt.figure()

ax = plt.axes([0,0,1,1],projection=ccrs.LambertConformal())
ax.set_extent([-160,-72,20,72],ccrs.Geodetic())

shape_name = 'admin_1_states_provinces_lakes_shp'
states_shp = shp_reader.natural_earth(resolution='110m',category='cultural',name=shape_name)

c = np.arange(1, 6)
norm = mpl.colors.Normalize(vmin=c.min(), vmax=c.max())
cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.PuBu)
cmap.set_array([])

ax.outline_patch.set_visible(False)

for states in shp_reader.Reader(states_shp).records():
    edge_color = 'black'
    try:
        # use the name of this state to get population density
        state_density = data_dict[states.attributes['name']]

    except:
        state_density = 0

    # scheme to assign color to each state
    if state_density < 5:

        facecolor = cmap.to_rgba(1)

    elif state_density < 10:

        facecolor = cmap.to_rgba(2)

    elif state_density < 15:

        facecolor = cmap.to_rgba(3)

    elif state_density < 20:
        facecolor = cmap.to_rgba(4)

    elif state_density < 25:
        facecolor = cmap.to_rgba(5)

    elif state_density < 30:
        facecolor = cmap.to_rgba(6)

    elif state_density < 35:
        facecolor = cmap.to_rgba(7)

    else:
        facecolor = cmap.to_rgba(8)

    map1 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(1))
    map2 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(2))
    map3 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(3))
    map4 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(4))
    map5 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(5))
    map6 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(6))
    map7 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(7))
    map8 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(8))
    labels = ['Opioid under 5', 'Opioid under 10', 'Opioid under 15', 'Opioid under 20',
                  'Opioid under 25', 'Opioid under 30', 'Opioid under 35', 'Opioid above 35']
    ax.add_geometries([states.geometry], ccrs.PlateCarree(),
                          facecolor=facecolor, edgecolor=edge_color)
    ax.legend([map1, map2, map3, map4, map5, map6, map7, map8],
                  labels, fancybox=True)

        
plt.show()
