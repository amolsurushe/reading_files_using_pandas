#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # Usecase-1 Load all three csv datasets in Pandas Data frames and display first 5 records.

# In[2]:


custumer = pd.read_csv(r'C:\Users\Jui\Desktop\projrct\Handling diff type files\CSV_s1\customers.csv',names=['custno','firstname','lastname','gender','age','profession','contactNo','emailId','city','state','isActive','createdDate','updateDate'])


# In[3]:


custumer.head()


# In[4]:


pruduct_col = pd.read_csv(r'C:\Users\Jui\Desktop\projrct\Handling diff type files\CSV_s1\products.csv', names=['productno','productName','Descriptin','isActive','createdDate','UpdatedDate'])


# In[8]:


pruduct_col.head()


# In[9]:


transaction_col= pd.read_csv(r'C:\Users\Jui\Desktop\projrct\Handling diff type files\CSV_s1\transactions.csv',names=['txnno','txndate','custno','amount','productno','spendby'])


# In[10]:


transaction_col.head()


# # Usecase-2 Display only those customers from CSV_s1, who purchased more than 3 products

# In[11]:


transaction_col.groupby('custno').filter(lambda transaction_col:transaction_col['custno'].count()>3)['custno'].unique()


# # Usecase-3 Display top 5 most demanded products from CSV_s1
# 

# In[12]:


transaction_col['productno'].value_counts().head()


# # Usecase-4 Display top 5 transactions amount from CSV_s1
# 

# In[13]:


transaction_col.sort_values('amount',ascending = False).head(5)


# # Usecase-5 Display distinct professions from CSV_s1
# 

# In[14]:


custumer['profession'].unique()


# # Usecase-6 Display highest age in CSV_s1 customer’s dataset
# 

# In[15]:


custumer['age'].max()


# # usecase- 7 Display custno, gender, age, profession, contactno, productno, productName,txndate, spendby, amount from CSV_s1 for custno = 923

# In[16]:


custumer1 = custumer[['custno','gender','age','profession','contactNo']]


# In[17]:


custumer1


# In[18]:


product1 = pruduct_col[['productno','productName']]


# In[19]:


product1


# In[20]:


transactions1 = transaction_col[['txndate','spendby','amount']]


# In[21]:


transactions1


# In[22]:


join1 = pd.concat([custumer1,product1],axis=1)


# In[23]:


join1


# In[24]:


join4 = pd.concat([join1,transactions1],axis=1)


# In[25]:


join4.head()


# In[26]:


join4[join4['custno'] == 923]


# # Usecase-8 Load all three PSV (pipe separated values) dataset in Pandas Data frames and display first 5 record

# In[27]:


df = pd.read_csv('C:\\Users\\Jui\\Desktop\\PDS CLASS\\PythonProject PHASE 2\\PythonProject\\PSV_s2\\customers.txt',sep='|', names=['custno','firstname','lastname','gender','age','profession','contactNo','emailId','city','state','isActive','createdDate','UpdateDate'])


# In[28]:


df


# In[29]:


df.head()


# In[30]:


df1 = pd.read_csv('C:\\Users\\Jui\\Desktop\\PDS CLASS\\PythonProject PHASE 2\\PythonProject\\PSV_s2\\products.txt',sep='|', names=['productno','productName','Descriptin','isActive','createdDate','UpdatedDate'])


# In[31]:


df1


# In[32]:


df1.head()


# In[33]:


df3= pd.read_csv('C:\\Users\\Jui\\Desktop\\PDS CLASS\\PythonProject PHASE 2\\PythonProject\\PSV_s2\\transactions.txt',sep='|',names=['txnno','txndate','custno','amount','productno','spendby'])


# In[34]:


df3


# In[35]:


df3.head()


# # usecase-9 Load all three JSON datasets in Pandas Data frames and display first 5 records

# In[36]:


customer_json = 'C:\\Users\\Jui\\Desktop\\PDS CLASS\\PythonProject PHASE 2\\PythonProject\\JSON_s3\\customers.json'


# In[37]:


customers_json = pd.read_json(customer_json,
   convert_dates=True,lines = True)


# In[38]:


customers_json.head()


# In[39]:


product_json = 'C:\\Users\\Jui\\Desktop\\PDS CLASS\\PythonProject PHASE 2\\PythonProject\\JSON_s3\\products.json'


# In[40]:


products_json = pd.read_json(product_json,
    convert_dates=True,lines = True)


# In[41]:


products_json.head()


# In[42]:


transaction_json = 'C:\\Users\\Jui\\Desktop\\PDS CLASS\\PythonProject PHASE 2\\PythonProject\\JSON_s3\\transactions.json'


# In[43]:


transactions_json = pd.read_json(transaction_json,
    convert_dates=True,lines = True)


# In[44]:


transactions_json.head()


# In[ ]:




