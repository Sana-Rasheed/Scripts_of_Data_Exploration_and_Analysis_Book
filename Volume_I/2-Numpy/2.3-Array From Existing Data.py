#!/usr/bin/env python
# coding: utf-8

# ## numpy.asarray
# 

# ### Example 1
# 

# In[1]:


# convert list to ndarray 
import numpy as np 

x = [1,2,3] 
a = np.asarray(x) 
print (a)


# ### Example 2
# 

# In[19]:


# dtype is set 
import numpy as np 

x = [1,2,3]
a = np.asarray(x, dtype = float) 
print (a)


# ### Example 3
# 

# In[3]:


# ndarray from tuple 
import numpy as np 

x = (1,2,3) 
a = np.asarray(x) 
print (a)


# ### Example 4
# 

# In[4]:


# ndarray from list of tuples 
import numpy as np 

x = [(1,2,3),(4,5)] 
a = np.asarray(x) 
print (a)


# ### numpy.fromiter

# In[10]:


# obtain iterator object from list 
import numpy as np 
list = range(5) 
it = iter(list)  

# use iterator to create ndarray 
x = np.fromiter(it, dtype = float) 
print (x)


# ### numpy.arange
# 

# ### Example 1
# 

# In[11]:


import numpy as np 
x = np.arange(5) 
print (x)


# ### Example 2
# 

# In[12]:


import numpy as np 
# dtype set 
x = np.arange(5, dtype = float)
print (x)


# ### Example 3
# 

# In[13]:


# start and stop parameters set 
import numpy as np 
x = np.arange(10,20,2) 
print (x)


# ### numpy.linspace
# 

# ### Example 1
# 

# In[14]:


import numpy as np 
x = np.linspace(10,20,5) 
print (x)


# ### Example 2
# 

# In[15]:


# endpoint set to false 
import numpy as np 
x = np.linspace(10,20, 5, endpoint = False) 
print (x)


# ### Example 3
# 

# In[16]:


# find retstep value 
import numpy as np 

x = np.linspace(1,2,5, retstep = True) 
print (x) 
# retstep here is 0.25


# ### numpy.logspace
# 

# ### Example 1
# 

# In[17]:


import numpy as np 
# default base is 10 
a = np.logspace(1.0, 2.0, num = 10) 
print (a)


# ### Example 2
# 

# In[18]:


# set base of log space to 2 
import numpy as np 
a = np.logspace(1,10,num = 10, base = 2) 
print (a)


# In[ ]:




