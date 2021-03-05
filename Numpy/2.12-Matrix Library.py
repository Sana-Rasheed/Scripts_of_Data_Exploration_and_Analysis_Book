#!/usr/bin/env python
# coding: utf-8

# ### matlib.empty()
# 

# In[1]:


import numpy.matlib 
import numpy as np 

print (np.matlib.empty((2,2))) 
# filled with random data


# ### numpy.matlib.zeros()
# 

# In[2]:


import numpy.matlib 
import numpy as np 
print (np.matlib.zeros((2,2))) 


# ### numpy.matlib.ones()
# 

# In[3]:


import numpy.matlib 
import numpy as np 
print (np.matlib.ones((2,2)))


# ### numpy.matlib.eye()
# 

# In[4]:


import numpy.matlib 
import numpy as np 
print (np.matlib.eye(n = 3, M = 4, k = 0, dtype = float))


# ### numpy.matlib.identity()
# 

# In[5]:


import numpy.matlib 
import numpy as np 
print (np.matlib.identity(5, dtype = float))


# ### numpy.matlib.rand()
# 

# In[6]:


import numpy.matlib 
import numpy as np 
print (np.matlib.rand(3,3))


# In[7]:


import numpy.matlib 
import numpy as np  

i = np.matrix('1,2;3,4') 
print (i) 


# In[8]:


import numpy.matlib 
import numpy as np  

j = np.asarray(i) 
print (j) 


# In[9]:


import numpy.matlib 
import numpy as np  

k = np.asmatrix (j) 
print (k)


# In[ ]:




