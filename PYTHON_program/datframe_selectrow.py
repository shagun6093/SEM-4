import pandas as pd
exam_data=({'name':['shagun','medhaj','anehri','akshay','deep','shashank','mamta'],'marks':[25,85,98,85,78,9,6]})
labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=labels)
print("\noriginal dataframe")
print(df)

print("\nrows having marks equal to 25")
print(df[df['marks']==25])