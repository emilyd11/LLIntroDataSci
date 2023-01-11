#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sn 
import numpy as np


# In[2]:


listings = pd.read_csv('~/Desktop/Airbnb_NYC_2019.csv')


# In[3]:


listings


# In[6]:


sn.countplot(x = 'neighbourhood_group', data = listings)
plt.show()


# In[7]:


sn.barplot(x = 'neighbourhood_group', y = 'price', data = listings)
plt.show()


# In[8]:


sn.barplot(x = 'neighbourhood_group', y = 'price', data = listings, ci = False)
plt.show()


# In[10]:


plt.hist(listings['price'])
plt.xlabel('price (in US dollars)')
plt.show()


# In[12]:


plt.hist(listings['price'], bins = np.arange(0, 1100, 40))
plt.xlabel('price (in US dollars)')
plt.show()


# In[13]:


plt.scatter(x = listings['price'], y = listings['number_of_reviews'])
plt.xlabel('price')
plt.ylabel('number of reviews')
plt.show()


# In[14]:


plt.scatter(x = listings['price'], y = listings['number_of_reviews'])
plt.xlabel('price')
plt.ylabel('number of reviews')
plt.xlim(0, 1100)
plt.show()


# In[15]:


plt.scatter(x = listings['price'], y = listings['number_of_reviews'], s = 5)
plt.xlabel('price')
plt.ylabel('number of reviews')
plt.xlim(0, 1100)
plt.show()


# In[ ]:




