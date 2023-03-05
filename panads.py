import pandas as pd

'''pf=pd.read_csv('test.csv')
print(pf)
'''

'''
pf1=pd.read_json('https://api.sampleapis.com/codingresources/codingResources')
pf1.to_html('api.html')
print(pf1)
'''

'''
pf1=pd.read_json('https://api.sampleapis.com/codingresources/codingResources')

pf1.to_excel('api.xlsx',sheet_name='sheet1')
print(pf1)
'''

'''
pf1=pd.read_csv(r'')
print(pf1)
'''

'''
pf1=pd.read_excel(r"" )
pf1.to_csv('pivot.csv')
print(pf1)

'''

# shape (prints rows and columns)
'''
pf=pd.read_csv('api.csv')
pf1=pf.shape
print(pf1)
'''
'''
#df.info
pf=pd.read_csv('api.csv')
pf1=pf.info
print(pf1)
'''
#dtypes (Read the data type of column)
'''
pf=pd.read_csv('api.csv')
pf1=pf.dtypes
print(pf1)
'''
#columns (Read name of columns)
'''
pf=pd.read_csv('api.csv')
pf1=pf.columns
print(pf1)
'''

#head(10) (Read first n lines)
'''
pf=pd.read_csv('api.csv')
pf1=pf.head(12)
print(pf1)
'''

#tail(5) (Reads last n lines of datafreame)
'''
pf=pd.read_csv('api.csv')
print(pf.tail(5))
'''

#sample

'''
pf=pd.read_csv('api.csv')
pf2=pf.sample(11)
print(pf2)
'''

#describe (high level data analysis)
'''pf=pd.read_csv('api.csv')
pf2=pf.describe()
print(pf2)'''


#/featching perticular data of column
'''pf=pd.read_csv('api.csv')
pf1=pf[['id','url']]
print(pf1)'''


#Rename col or row name
'''pf=pd.read_csv('api.csv')
pf.rename({0:'A',1:'B'},axis=0,inplace=True )
print(pf)'''

#loc (row,col)
'''df=pd.read_csv('api.csv')

df1=df.loc[2:3,['id','topics']]
df1=df.to_string()
print(df1)'''

#iloc ()
'''df=pd.read_csv('api.csv')
df1=df.iloc[1:3,1:3]
print(df1)
'''


#Add new column
'''
df=pd.read_csv('api.csv')
#df1=df.to_string()
df['new_col']='python'
df.drop('new_col',axis=1,inplace=True)      #(Remove column)
print(df)'''


#Add two columns
'''df=pd.read_csv('api.csv')
df['add']=df['url']+df['topics']
print(df)'''

#Find unique data (Remove duplicate)
'''df=pd.read_csv('api.csv')
df1=(df["topics"].unique())
df2=df1['id'].value_counts()
print(df2)'''

#Sorting by ascending
'''df=pd.read_csv('api.csv')

df1=df.sort_values(by=['levels'])
print(df1)'''

'''df=pd.read_csv('api.csv')

df1=df[df['topics']=='ruby']
print(df1)'''



'''df=pd.read_excel('practice_excel.xlsx' )
obj=df.groupby('Taluka')
p=obj.get_group('Panvel')

print(p)'''

#Concat datafreames
pf=pd.read_excel('practice_excel.xlsx',sheet_name='Sheet1')
pf1=pd.read_excel('practice_excel.xlsx',sheet_name='Sheet2')
pf2=pd.read_excel('practice_excel.xlsx',sheet_name='Sheet3')
df_concat=pd.concat([pf,pf1],axis=1,keys=['df','df1'])
print(df_concat)


#Merging

