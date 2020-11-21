#!/usr/bin/env python
# coding: utf-8

# # Cryptocurrency prices
# 
# * **Filename:**  `cryptocurrencies.csv`
# * **Description:** Cryptocurrency prices for a handful of coins over time.
# * **Source:** https://coinmarketcap.com/all/views/all/ but from a million years ago (I cut and pasted, honestly)
# 
# ### Make a chart of bitcoin's high, on a weekly basis
# 
# You might want to do the cherry blossoms homework first, or at least read the part about `format=` and `pd.to_datetime`.
# 
# *Yes, that's the entire assignment. It isn't an exciting dataset, but it's just dirty enough to make charting this a useful experience.*

# In[2]:


import pandas as pd
df = pd.read_csv("cryptocurrencies.csv")


# In[3]:


df.head()


# In[5]:


df.set_index('date')


# <!-- df['month'] = pd.to_datetime(df['Full-flowering_date'], "format='%-m%d'", errors='coerce')
# 
# When you use pd.to_datetime, you can pass a format= argument that explains what the format is of the datetime. You use the codes here to mark out where the days, months, etc are. For example, 2020-04-09 would be converted using pd.to_datetime(df.colname, "format='%Y-%m-%d").
# errors='coerce' will return NaN for missing values. By default it just yells "I don't know what to do!!!"
# And remember how we used df.date_column.dt.month to get the number of the month? For the name, you use dt.strftime (string-formatted-time), and pass it the same codes to tell it what to do. For example, df.date_column.dt.strftime("%Y-%m-%d") would give you "2020-04-09". -->

# In[42]:


df['month'] = pd.to_datetime(df.date)


# In[43]:


df = df.set_index('month')


# In[44]:


df.dtypes


# In[64]:


# problem: high is a str (object) with commas
df['high'] = df['high'].str.replace(',', '')
df['high'] = df.high.astype(float)


# In[65]:


df.high


# In[73]:


df.resample('W').high.median().plot(kind='barh', title='bitcoin weekly highs', figsize=(12, 12))

