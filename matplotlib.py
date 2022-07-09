#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r'C:\Users\Neha\Documents\cpf.csv')
df


# In[4]:


xdf = df['Experience']


# In[5]:


xdf


# In[6]:


ax = xdf.plot(kind = 'bar')
ax


# In[ ]:




