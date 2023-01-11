#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


crime = pd.read_csv('~/Desktop/crime_boston.csv')


# In[3]:


crime


# In[4]:


crime.groupby('INCIDENT_NUMBER').count()


# In[5]:


crime.isnull()


# In[6]:


crime.isnull().any(axis=1)


# In[7]:


rows_w_missing_vals = crime.isnull().any(axis=1)

crime[rows_w_missing_vals]


# In[11]:


crime_cleaned = crime.drop(columns = ['YEAR', 'MONTH', 'HOUR'])


# In[13]:


crime_cleaned['OFFENSE_CODE_GROUP'].unique()


# In[15]:


crime_cleaned['OFFENSE_DESCRIPTION'].unique()


# In[16]:


crime_cleaned['DAY_OF_WEEK'].unique()


# In[17]:


crime_cleaned = crime_cleaned.drop(columns='Location')


# In[ ]:




