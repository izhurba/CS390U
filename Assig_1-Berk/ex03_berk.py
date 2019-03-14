#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

count = 0

status = []
gender = []
ngen = []
dept = []
freq = []
A_freq = []
R_freq = []
MA_freq = []
FA_freq = []
MR_freq = []
FR_freq = []

with open("berkley.txt","r") as data:
    next(data)
    for line in data:
        words = line.split(',')
        status.append(words[0])
        gender.append(words[1])
        dept.append(words[2])
        freq.append(words[3])


for k in freq:
    if (count % 2 == 0):
        A_freq.append(freq[count])
    else:
        R_freq.append(freq[count])
    count +=1

count = 0

for g in A_freq:
    if (count % 2 == 0):
        MA_freq.append(A_freq[count])
    else:
        FA_freq.append(A_freq[count])
    count +=1

count = 0

for f in R_freq:
    if (count % 2 == 0):
        MR_freq.append(R_freq[count])
    else:
        FR_freq.append(R_freq[count])
    count +=1

count = 0

for h in gender:
    if (count % 2 == 0):
        ngen.append(gender[count])
    count +=1

count = 0

maf = np.asarray(MA_freq, dtype = int)
faf = np.asarray(FA_freq, dtype = int)
mrf = np.asarray(MR_freq, dtype = int)
frf = np.asarray(FR_freq, dtype = int)

print(maf)

width = 0.4
xlabel_offset = 0.2
ind = np.arange(6)
indX = np.arange(xlabel_offset, len(dept),1)

p1 = plt.bar(ind,maf, width)
p2 = plt.bar(ind,faf, width, bottom = maf)
p3 = plt.bar(ind+width,mrf, width)
p4 = plt.bar(ind+width,frf, width, bottom = mrf)

plt.xlabel('Dept')
plt.ylabel('Freq')
plt.title('Berkley Admission Data')
plt.yticks(np.arange(0,900,100))
plt.xticks(ind+width/2,('A', 'B', 'C', 'D', 'E', 'F'))
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Men accepted', 'Women Accepted', 'Men rejected', 'Women rejected'))

plt.show()

