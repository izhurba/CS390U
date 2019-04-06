import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.table import Cell

year = []
ytotal = []
month = []
mtotal = []
day = []

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

    mtotal.append(month[counter:x].count(1))
    mtotal.append(month[counter:x].count(2))
    mtotal.append(month[counter:x].count(3))
    mtotal.append(month[counter:x].count(4))
    mtotal.append(month[counter:x].count(5))
    mtotal.append(month[counter:x].count(6))
    mtotal.append(month[counter:x].count(7))
    mtotal.append(month[counter:x].count(8))
    mtotal.append(month[counter:x].count(9))
    mtotal.append(month[counter:x].count(10))
    mtotal.append(month[counter:x].count(11))
    mtotal.append(month[counter:x].count(12))

    counter = counter + t


