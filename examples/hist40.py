#!/usr/bin/python
#histogram example from Data Science From Scratch P. 40
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

grades = [83, 45, 56, 29,91, 88, 65, 12, 77, 95, 61, 88, 71, 51, 90, 82, 86, 70,69,41]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

#to learn about Counter
nums = [80, 40, 50, 90, 80, 60, 70, 90, 60, 80, 70, 50, 90, 80, 40]
counts = Counter(x for x in nums)
print(counts)

plt.bar([x - 4 for x in histogram.keys()],  #shift each bar x coord left by 4
	histogram.values(),						#set bar height for each bar
	8)										#each bar width is 8
plt.axis([-5, 105, 0, 7])					#x-axis -5..105, y-axis 0..7
plt.xticks([10*i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of students")
plt.title("Distribution of Grades")

plt.show()
