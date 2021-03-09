#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd

tips =pd.read_csv("tips.csv")
tips.head()


# ### SELECT
# 

# In[15]:


print (tips[['total_bill', 'tip', 'smoker', 'time']].head(5))


# ### WHERE
# 

# In[16]:


print (tips[tips['time'] == 'Dinner'].head(5))


# ### GroupBy
# 

# In[17]:


print (tips.groupby('sex').size())


# ### Top N rows
# 

# In[18]:


tips = tips[['smoker', 'day', 'time']].head(5)
print (tips)


# In[ ]:




