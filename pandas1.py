import pandas as pd
pf=pd.read_excel('practice_excel.xlsx',sheet_name='Sheet1')
pf1=pd.read_excel('practice_excel.xlsx',sheet_name='Sheet2')
pf2=pd.read_excel('practice_excel.xlsx',sheet_name='Sheet3')

p=pd.merge(pf,pf1,how="inner",on="Client_Code")
p1=pd.merge(p,pf2,how="inner",on='Client_Code')

print(p1)
