

import matplotlib.pyplot as plt
languages='java','python','php','javascript','c#','c++'
popularity =[22.2,17.6,8.8,8,7.7,6.7]
colors=["blue","green","yellow","black","orange","purple"]
plt.pie(popularity,labels=languages,colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2022 compared to a year ago")
plt.axis('equal')

plt.show()
