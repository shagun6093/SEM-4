# 6) Write a Pandas program to calculate the mean of all students' scores. Data is stored in adataframe.
import pandas as pd
exam_data=({'name':['shagun','medhaj','anehri','akshay','deep','shashank','mamta'],'scores':[25,85,98,85,78,9,6]})
labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=labels)
print("Mean of all students scores")
print(df['scores'].mean ())