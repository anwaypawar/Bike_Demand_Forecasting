#!/usr/bin/env python
# coding: utf-8

# In[17]:


# import the library
import pandas as pd
import numpy as np


# In[19]:


# import the dataset
data=pd.read_csv('Uber_New_Analysis.csv',skipfooter=1,engine='python')


# 

# In[20]:


# print the data
print(data)


# In[21]:


# print only top 5 rows
data.head()


# In[22]:


data.head(10)


# In[23]:


# last 5 rows
data.tail()


# In[24]:


# type
type(data)


# In[25]:


# shape of data
data.shape


# In[26]:


# shape of data
data.shape[1]


# In[27]:


# all the data type
data.dtypes


# In[28]:


# print complete information 
data.info()


# In[29]:


# print null values/ missing values
data.isnull()


# In[30]:


data.isnull().sum()
# handle null values in Purpose col


# In[31]:


# Summary of data
data.describe(include="all")


# In[32]:


data.T
#transpose of data


# In[33]:


# print the name of columns
data.columns


# In[34]:


data.index


# In[16]:


# missing values in purpose
# outliers also
# Date- DateTime Type
# Convert object data in numerical


# # Selection of data

# In[21]:


# print only start date
data.columns


# In[22]:


data['START_DATE*']


# In[23]:


data['MILES*']


# In[24]:


type(data['MILES*'])


# In[27]:


data.loc[:,'START_DATE*':'MILES*']


# In[35]:


data['START*']=data['START*'].str.replace('?','')


# In[37]:


pd.set_option('display.max_colwidth', None)


# In[38]:


pd.set_option('display.max_rows', None)


# In[39]:


#
data.columns


# In[18]:


# Display columns 'CATEGORY*', 'START*', 'MILES*',
# using loc function
data.loc[:,['CATEGORY*', 'START*', 'MILES*']]


# In[19]:


data.loc[0:21,['CATEGORY*', 'START*', 'MILES*']]


# In[20]:


# iloc method
# display first 3 col of data using iloc


# In[21]:


data.columns


# In[25]:


data.iloc[:,0:3]


# In[26]:


data.iloc[0:10,0:3] # loc methos takes complete index, iloc does the n-1


# In[27]:


data.columns


# In[28]:


# display first 15 rows of CATEGORY*,'MILES*' using iloc method
data.iloc[0:15,[2,5]]


# In[29]:


data.loc[0:15,:]


# In[32]:


# Print the rows where miles less than 10
data[data['MILES*']<10]


# In[34]:


data[data['MILES*']<10].shape


# In[35]:


data[data['MILES*']<10].shape[0]


# In[36]:


# Print the number of rows where start statation is Cary
data.head()


# In[42]:


data[data['START*']=='Fort Pierce'].shape[0]


# In[43]:


# print the columns CATEGORY*','MILES*' where miles less than 5
data.columns


# In[45]:


# Row index pass condition of miles, col index use list pass name of 
data.loc[data['MILES*']<5,['CATEGORY*','MILES*']]


# # Create a new column in data

# In[47]:


# create a new col based on miles whereever miles less than 5 "Small" , >=5 and <20- "Average', more than long journey 
data.head()


# In[48]:


df1=data.copy()


# In[53]:


data.head()


# In[52]:


df1.head()


# In[49]:


# function 
def func1(num):
    if num<5:
        return "Small"
    elif num>=5 and num<20:
        return "Average"
    else:
        return "Long"


# In[50]:


# create a new col
df1['Journey_len']=df1['MILES*'].apply(func1) # apply fun will apply some function


# In[51]:


df1.head()


# In[54]:


# function 
def func2(name):
    if name=='Fort Pierce':
        return "Most Visited"
    else:
        return "Not Interested"


# In[55]:


# create a new col
df1['destination']=df1['START*'].apply(func2)


# In[57]:


df1.head(15)


# # Columns Information

# In[58]:


# in category col what cat. are present
data['CATEGORY*'].unique()


# In[59]:


data['CATEGORY*'].nunique()


# In[60]:


# Number of records in each category 
data['CATEGORY*'].value_counts()


# In[62]:


# print the number of records in each category of Purpose col
data['PURPOSE*'].value_counts()


# In[63]:


print(data['PURPOSE*'].nunique())


# In[64]:


# Visualization 
data['PURPOSE*'].value_counts().plot(kind='bar')


# # Handle Missing Values

# In[65]:


# check sum of null values 
data.isnull().sum()


# In[66]:


# Print the precentatge of missing values
(data.isnull().sum()/len(data))*100


# In[67]:


# handle missing values
df=data.copy()


# In[68]:


# Drop the null value
df.dropna()


# In[70]:


df.isnull().sum()


# In[71]:


# change permanent
df.dropna(inplace=True)
# output is as view only


# In[72]:


df.isnull().sum()


# In[74]:


df.shape


# In[73]:


data.isnull().sum()


# In[75]:


data.shape


# In[76]:


# Handle missing values
# Fill the missing value with some Constant----'NA'
data['PURPOSE*'].fillna('NA')


# In[77]:


data.isnull().sum()


# In[78]:


data.head()


# In[79]:


data['PURPOSE*'].fillna(method='ffill')


# In[80]:


data['PURPOSE*'].fillna(method='bfill')


# In[81]:


# fill the missing value with mode
data['PURPOSE*'].fillna('Meeting')


# In[83]:


# fill the missing value with mode
data['PURPOSE*'].fillna('NA',inplace=True)


# In[84]:


data.isnull().sum()


# In[85]:


# Categorical data - Missing values- Constant, ffill, bfill, mode
data.head()


# In[86]:


data['MILES*'].hist()


# In[87]:


# Use median to handle missing value in Miles
data['MILES*'].fillna(data['MILES*'].median())


# # Machine learning need to convert Categorical col into numerical

# In[88]:


data.head()


# In[89]:


# Convert Binary values into 0 1 in Categorical col 
data['CATEGORY*'].unique()


# In[90]:


df3=data.copy()


# In[91]:


df3['CATEGORY*'].replace({'Business':1,'Personal':0},inplace=True)


# In[92]:


df3.head()


# In[93]:


# Dummy Encoding- Create dummy variable - 0 1 1 One hot coding
df3['PURPOSE*'].unique()


# # Meal   Supp   meeting Customer  ................
#    1      0       0       0      0  0 0 0
#    0       1      0       0     
#    0       0      1       0     0   0  0 

# In[94]:


# apply dummy encoding
pd.get_dummies(df3['PURPOSE*'])


# In[95]:


df3.head()


# In[97]:


# get_dummies() -Every object data type - dummy var
df3.dtypes


# In[98]:


# Convert Start date & End Date into Date time
df3['START_DATE*']=pd.to_datetime(df3['START_DATE*'])
df3['END_DATE*']=pd.to_datetime(df3['END_DATE*'])


# In[99]:


df3.dtypes


# In[100]:


pd.get_dummies(df3)


# In[101]:


df3.head()


# In[102]:


# Sort the data
# Group of data
# Ouliers
# Concatedata
# merge


# In[103]:


# sort the data
# miles
data.sort_values(by=['MILES*'])


# In[104]:


# sort the data
# miles
data.sort_values(by=['MILES*'],ascending=False)


# In[106]:


# sort the data
# miles
data.sort_values(by=['START*','MILES*'],ascending=[True,False])


# # Apply Grouping on data

# In[107]:


# Check how many rides were booked from each start point
data.groupby('START*')


# In[108]:


data.groupby('START*').count()


# In[109]:


# Sum of miles from each start point
data.groupby('START*')['MILES*'].sum()


# In[110]:


# Sum of miles from each start point
data.groupby('START*')['MILES*'].agg(["mean","sum","max","min","count"])


# In[111]:


# Sum of miles from each start point
data.groupby('START*')['MILES*'].agg(["max"])


# In[113]:


# extract the data where miles less than 10
#data['Miles'].sum()
data.columns


# In[114]:


# groupby with 2 columns
data.groupby(['CATEGORY*','PURPOSE*']).count()


# In[115]:


# groupby with 2 columns
data.groupby(['CATEGORY*','PURPOSE*'])['MILES*'].count()


# # Outlier Detection

# In[116]:


# Remove the outlier data
# Handle Outlier


# 1.5IQR rule- Stat way find the outlier
# Business way 5%, 95%....


# In[117]:


data.boxplot()


# In[118]:


df=data.copy()


# In[119]:


df.columns


# In[120]:


# 1.5IQR Rule
IQR=df['MILES*'].quantile(0.75)-df['MILES*'].quantile(0.25)
IQR


# In[121]:


lower=df['MILES*'].quantile(0.25)-(1.5*IQR)

upper=df['MILES*'].quantile(0.75)+(1.5*IQR)


# In[122]:


print(lower)


# In[123]:


print(upper)


# In[125]:


df[df['MILES*']<-8.35]


# In[127]:


df[df['MILES*']>upper].count()


# In[129]:


# Ignore Or Handle
# drop function
df.drop(df[df['MILES*']>upper].index,inplace=True)


# In[130]:


df.shape


# In[131]:


df.head()


# In[132]:


data.shape


# In[133]:


df.boxplot()


# In[134]:


df[df['MILES*']>upper].count()


# In[135]:


df1=data.copy()


# In[137]:


# handle the outlier
df1.loc[df1['MILES*']>upper,'MILES*']=21.65


# In[138]:


df1.boxplot()


# In[ ]:




