# Write a Python programming to create a pie chart of the popularity of programming Languages.
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
# import matplotlib.pyplot as plt
# # Data to plot
# languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
# popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"] # explode 1st slice
# # explode = (0.1, 0, 0, 0,0,0) # Plot
# plt.pie(popuratity, labels=languages, colors=colors,
# autopct='%1.1f%%', startangle=140)
# plt.axis('equal')
# plt.show()



import matplotlib.pyplot as plt
languages='java','python','php','javascript','c#','c++'
popularity =[22.2,17.6,8.8,8,7.7,6.7]
colors=["blue","green","yellow","black","orange","purple"]
plt.pie(popularity,labels=languages,colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2022 compared to a year ago")
plt.axis('equal')

plt.show()