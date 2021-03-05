#!/usr/bin/env python
# coding: utf-8

# ## ndarray.shape
# 

# ### Example 1
# 

# In[1]:


import numpy as np 
a = np.array([[1,2,3],[4,5,6]]) 
print (a.shape)


# ### Example 2
# 

# In[3]:


# this resizes the ndarray 
import numpy as np 

a = np.array([[1,2,3],[4,5,6]]) 
a.shape = (3,2) 
print (a)


# ### Example 3
# 

# In[4]:


import numpy as np 
a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2) 
print (b)


# ## ndarray.ndim
# 

# ### Example 1
# 

# In[5]:


# an array of evenly spaced numbers 
import numpy as np 
a = np.arange(24) 
print (a)


# ### Example 2
# 

# In[6]:


# this is one dimensional array 
import numpy as np 
a = np.arange(24) 
a.ndim  

# now reshape it 
b = a.reshape(2,4,3) 
print (b)
# b is having three dimensions


# ## numpy.itemsize
# 

# ### Example 1
# 

# In[7]:


# dtype of array is int8 (1 byte) 
import numpy as np 
x = np.array([1,2,3,4,5], dtype = np.int8) 
print (x.itemsize)


# ### Example 2
# 

# In[8]:


# dtype of array is now float32 (4 bytes) 
import numpy as np 
x = np.array([1,2,3,4,5], dtype = np.float32) 
print (x.itemsize)


# ### numpy.flags
# 

# In[9]:


import numpy as np 
x = np.array([1,2,3,4,5]) 
print (x.flags)


# ### numpy.empty
# 

# In[17]:


import numpy as np 
x = np.empty([3,2], dtype = int) 
print (x)


# ### numpy.zeros
# 

# ### Example 1
# 

# In[11]:


# array of five zeros. Default dtype is float 
import numpy as np 
x = np.zeros(5) 
print (x)


# ### Example 2
# 

# In[12]:


import numpy as np 
x = np.zeros((5,), dtype = np.int) 
print (x)


# ### Example 3
# 

# In[13]:


# custom type 
import numpy as np 
x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print (x)


# ### numpy.ones
# 

# ### Example 1
# 

# In[14]:


# array of five ones. Default dtype is float 
import numpy as np 
x = np.ones(5) 
print (x)


# ### Example 2
# 

# In[15]:


import numpy as np 
x = np.ones([2,2], dtype = int) 
print (x)


# In[ ]:




