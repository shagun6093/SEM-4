# 10) Write a Pandas program to set a given value for particular cell in DataFrame using index value
import pandas as pd
exam_data=({'name':['shagun','medhaj','anehri','akshay','deep','shashank','mamta'],'marks':[25,85,98,85,78,9,6]})
labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=labels)
print(df)
print("after updating")
df._set_value(6,'marks',10.2)
print(df)