# Write a Python program to create bar plot of scores by group and gender. Use multiple X values on the same chart for men and women.
# Means (men) = (22, 30, 35, 35, 26)
# Means (women) = (25, 32, 30, 35, 29)


# insstall necessary library numpy
import numpy as np
import matplotlib.pyplot as plt
# data to plot
#craeting 3 variables
#defines the numebr of groups
n_groups = 5

#tuple of scores of men means
men_means = (22, 30, 33, 30, 26)
#tuple of scores of men means
women_means = (25, 32, 30, 35, 29) # create plot

# creating figure and an axes using subplots function
fig, ax = plt.subplots()

#craeting array of evenly spaced values for x axis
index = np.arange(n_groups)

# defining opacit and barwidth
bar_width = 0.35
opacity = 0.8

# rects1 and rects2 are variables that store the returned objects from the bar function,
rects1 = plt.bar(index, men_means, bar_width,
alpha=opacity,
color='b',
label='Men')
rects2 = plt.bar(index + bar_width, women_means, bar_width,
alpha=opacity,
color='r',
label='Women')


plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')

# This line sets the tick labels on the x-axis to the values in the tuple
plt.xticks(index + bar_width, ('G1', 'G2', 'G3', 'G4', 'G5'))

# These three lines add a legend to the plot, adjust the layout of the plot to make sure all the labels and axes are visible, and then display the plot on the screen.

plt.legend()
plt.tight_layout()
plt.show()