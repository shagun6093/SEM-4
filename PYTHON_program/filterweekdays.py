# write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day)==6 else '', weekdays)
for d in days:
    print(d)