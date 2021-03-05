#!/usr/bin/env python
# coding: utf-8

# ### numpy.ndarray.byteswap()
# 

# In[6]:


import numpy as np 
a = np.array([1, 256, 8755], dtype = np.int16) 

print ('Our array is:') 
print (a)  

print ('Representation of data in memory in hexadecimal form:')  
print (map(hex,a))

# byteswap() function swaps in place by passing True parameter 

print ('Applying byteswap() function:') 
print (a.byteswap(True)) 

print ('In hexadecimal form:') 
print (map(hex,a))
# We can see the bytes being swapped


# ### No Copy
# 

# In[9]:


import numpy as np 
a = np.arange(6) 

print ('Our array is:') 
print (a)  

print ('Applying id() function:') 
print (id(a))  

print ('a is assigned to b:') 
b = a 
print (b)  

print ('b has same id():') 
print (id(b))  

print ('Change shape of b:') 
b.shape = 3,2 
print (b)  

print ('Shape of a also gets changed:') 
print (a)


# ### View or Shallow Copy
# 

# In[10]:


import numpy as np 
# To begin with, a is 3X2 array 
a = np.arange(6).reshape(3,2) 

print ('Array a:') 
print (a)  

print ('Create view of a:') 
b = (a.view()) 
print (b)  

print ('id() for both the arrays are different:') 
print ('id() of a:')
print (id(a))  
print ('id() of b:') 
print (id(b))  

# Change the shape of b. It does not change the shape of a 
b.shape = 2,3 

print ('Shape of b:') 
print (b)  

print ('Shape of a:') 
print (a)


# In[11]:


import numpy as np 
a = np.array([[10,10], [2,3], [4,5]]) 

print ('Our array is:') 
print (a)  

print ('Create a slice:') 
s = a[:, :2] 
print (s)


# ### Deep Copy
# 

# In[15]:


import numpy as np 
a = np.array([[10,10], [2,3], [4,5]]) 

print ('Array a is:') 
print (a)  

print ('Create a deep copy of a:') 
b = a.copy() 
print ('Array b is:') 
print (b) 

#b does not share any memory of a 
print ('Can we write b is a') 
print (b is a)  

print ('Change the contents of b:') 
b[0,0] = 100 

print ('Modified array b:') 
print (b)  

print ('a remains unchanged:') 
print (a)


# In[ ]:




