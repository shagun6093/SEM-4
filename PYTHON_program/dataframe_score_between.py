import pandas as pd
exam_data=({'name':['shagun','medhaj','anehri','akshay','deep','shashank','mamta'],'scores':[25,85,98,85,78,9,6]})
labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=labels)
print("scores between 50-90")
print(df[df['scores'].between(50,90)])