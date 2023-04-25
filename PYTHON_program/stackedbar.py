# write a Python program to create a stacked bar plot with error bars.
# Note: Use bottom to stack the women?s bars on top of the men?s bars.
# Sample Data:
# Means (men) = (22, 30, 35, 35, 26)
# Means (women) = (25, 32, 30, 35, 29)
# Men Standard deviation = (4, 3, 4, 1, 5)
# Women Standard deviation = (3, 5, 2, 3, 3)


import numpy as np
import matplotlib.pyplot as plt
N = 5
menMeans = (22, 30, 35, 35, 26)
womenMeans = (25, 32, 30, 35, 29)
menStd = (4, 3, 4, 1, 5)
womenStd = (3, 5, 2, 3, 3) # the x locations for the groups
index = np.arange(N)
# the width of the bars
width = 0.35
p1 = plt.bar(index, menMeans, width, yerr=menStd, color='red')
p2 = plt.bar(index, womenMeans, width,bottom=menMeans, yerr=womenStd, color='green')
plt.ylabel('Scores')
plt.xlabel('Groups')
plt.title('Scores by group\n' + 'and gender')
plt.xticks(index, ('Group1', 'Group2', 'Group3', 'Group4', 'Group5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))
plt.show()