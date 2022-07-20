import pandas as pd
dic={
    'country':[],
    'capital':[],
    }
df=pd.DataFrame(data=dic)
co=input("enter the country")
ca=input("enter the capital")
df=df.append({'country':co,'capital':ca},ignore_index=true)
print(df)
