import pandas as pd
exam_data=({'name':['shagun','medhaj','anehri','akshay','deep','shashank','mamta'],'marrks':[25,85,98,85,78,9,6]})
labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=labels)
print("original dataframe")
print(df)
rollno=[100,78,25,14,56,8,74]
df['rollno']=rollno
print("updated dataframe")
print(df)