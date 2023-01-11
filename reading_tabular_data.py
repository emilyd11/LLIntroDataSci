#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


us_babies = pd.read_csv("~/Desktop/us_baby_names.csv")


# In[7]:


us_babies 


# In[8]:


us_babies['Year']


# In[9]:


us_babies['Year'] == 2014


# In[11]:


us_babies_2014 = us_babies.loc[us_babies['Year'] == 2014, :]


# In[12]:


us_babies_2014


# In[13]:


sorted_us_2014 = us_babies_2014.sort_values('Count', ascending = False)


# In[14]:


sorted_us_2014.iloc[0:5]


# In[15]:


states_babies = pd.read_csv('~/Desktop/state_baby_names.csv')


# In[18]:


states_babies_2014 = states_babies.loc[states_babies['Year'] == 2014,:]


# In[20]:


ca_babies_2014 = states_babies_2014.loc[states_babies_2014['State'] == 'CA', :]


# In[21]:


sorted_ca_2014 = ca_babies_2014.sort_values('Count', ascending = False)


# In[22]:


sorted_ca_2014.iloc[0:5]


# In[ ]:


def popular(s):
    '''this aggregate function: receives s, a Pandas Series, that contains baby names in order of highest count to lowest count. Returns the most popular name in s.'''
    return s.iloc[0]


# In[ ]:


ca_grouped = ca_babies.sort_values('Count', ascending = False).groupby(['Year', 'Gender']).agg(popular)


# In[27]:


us_emily = us_babies.loc[us_babies['Name'] == 'Emily', :]


# In[28]:


us_emily.plot.barh(x = 'Year', y = 'Count')


# In[ ]:




