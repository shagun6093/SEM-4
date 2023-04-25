import pandas as pd
exam_data=({'name':['shagun','medhaj','anheri','shashank','mamta','akshay'],'attempts':[5,8,1,4,2,1]})
labels=['a','b','c','d','e','f']
df=pd.DataFrame(exam_data,index=labels)
print("attempts greater than 2")
print(df[df['attempts']>2])