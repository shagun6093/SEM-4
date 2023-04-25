# 7) Write a Pandas program to append a new row 'k' to data frame with given values for eachcolumn. Now delete the new row and return the original DataFrame.
import pandas as pd
exam_data=({'name':['shagun','medhaj','anehri','akshay','deep','shashank','mamta'],'scores':[25,85,98,85,78,9,6]})
labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=labels)
print("\noriginal dataframe")
print(df)
print("\n Append new row")
df.loc['k']=['aryan','28']
print("\nall records after inserting new row")
print(df)
print("\ndelete new row")
df=df.drop('k')
print(df)