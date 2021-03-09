#!/usr/bin/env python
# coding: utf-8

# ### Create a Range of Dates
# 

# In[2]:


import pandas as pd

print (pd.date_range('1/1/2011', periods=5))


# ### Change the Date Frequency
# 

# In[5]:


import pandas as pd

print (pd.date_range('1/1/2011', periods=5,freq='M'))


# ### bdate_range
# 

# In[3]:


import pandas as pd

print (pd.date_range('1/1/2011', periods=5))


# ### String

# In[6]:


import pandas as pd

print (pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))


# ### Integer
# 

# In[7]:


import pandas as pd

print (pd.Timedelta(6,unit='h'))


# ### Data Offsets
# 

# In[8]:


import pandas as pd

print (pd.Timedelta(days=2))


# ### to_timedelta()
# 

# In[9]:


import pandas as pd

print (pd.Timedelta(days=2))


# ### Operations
# 

# In[10]:


import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))

print (df)


# ### Addition Operations
# 

# In[11]:


import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']

print (df)


# ### Subtraction Operation
# 

# In[12]:


import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']
df['D']=df['C']+df['B']

print (df)


# In[ ]:




