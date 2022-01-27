#Tsnzeel
#!/usr/bin/env python
# coding: utf-8

# ### Example 1

# In[2]:


import numpy as np  
a = np.array([1,2,3]) 
print (a)


# ### Example 2

# In[4]:


# more than one dimensions 
import numpy as np 
a = np.array([[1, 2], [3, 4]]) 
print (a)


# ### Example 3

# In[5]:


# minimum dimensions 
import numpy as np 
a = np.array([1, 2, 3,4,5], ndmin = 2) 
print (a)


# ### Example 4

# In[7]:


# dtype parameter 
import numpy as np 
a = np.array([1, 2, 3], dtype = complex)
print (a)


# ### Data Type Objects

# ### Example 1

# In[9]:


# using array-scalar type 
import numpy as np
dt = np.dtype(np.int32) 
print (dt)


# ### Example 2

# In[11]:


#int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc.
import numpy as np  

dt = np.dtype('i4')
print (dt)


# ### Example 3

# In[12]:


# using endian notation 
import numpy as np
dt = np.dtype('>i4')
print (dt)


# ### Example 4

# In[13]:


# first create structured data type  
import numpy as np
dt = np.dtype([('age',np.int8)]) 
print (dt)


# ### Example 5

# In[14]:


# now apply it to ndarray object  
import numpy as np 

dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print (a)


# ### Example 6

# In[15]:


# file name can be used to access content of age column  
import numpy as np 

dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print (a['age'])


# ### Example 7

# In[16]:


import numpy as np 
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
print (student)


# ### Example 8

# In[17]:


import numpy as np 

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print (a)


# In[ ]:




