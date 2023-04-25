# pyplot module installation for creating and customizing the visulalization
import matplotlib.pyplot as plt
# creating two list
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# This line creates a list x_pos using a list comprehension that enumerates the index positions of the x list. This is necessary for positioning the bars on the chart.
x_pos = [i for i, _ in enumerate(x)]
# creating a bar by x,y axis
plt.bar(x_pos, popularity, color='blue')
# seting x,y axis
plt.xlabel("Languages")
plt.ylabel("Popularity")
# title of the chart
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red') # Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
# show the chart
plt.show()




