#!/usr/bin/env python
# coding: utf-8

# ## Broadcasting

# ### Example 1

# In[2]:


import numpy as np 
a = np.array([1,2,3,4])  
b = np.array([10,20,30,40])  
c = a * b  
print (c)


# ### Example 2

# In[4]:


import numpy as np 
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])  
   
print ('First array:') 
print (a) 
print ('\n')  
   
print ('Second array:') 
print (b) 
print ('\n')  
   
print ('First Array + Second Array') 
print (a + b)


# ## Iterating Over Array

# ### Example 1
# 

# In[7]:


import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)

print ('Original array is:')
print (a)
print ('\n')

print ('Modified array is:')
for x in np.nditer(a):
   print (x)


# ### Example 2
# 

# In[9]:


import numpy as np 
a = np.arange(0,60,5) 
a = a.reshape(3,4) 
   
print ('Original array is:')
print (a) 
print ('\n')  
   
print ('Transpose of the original array is:') 
b = a.T 
print (b) 
print ('\n')  
   
print ('Modified array is:') 
for x in np.nditer(b): 
   print (x)


# ## Iteration Order
# 

# ### Example 1
# 

# In[11]:


import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('Original array is:')
print (a)
print ('\n')

print ('Transpose of the original array is:')
b = a.T
print (b)
print ('\n')

print ('Sorted in C-style order:')
c = b.copy(order = 'C')
print (c)
for x in np.nditer(c):
   print (x)

print ('\n')

print ('Sorted in F-style order:')
c = b.copy(order = 'F')
print (c)
for x in np.nditer(c):
   print (x)


# ### Example 2
# 

# In[12]:


import numpy as np 
a = np.arange(0,60,5) 
a = a.reshape(3,4) 

print ('Original array is:') 
print (a) 
print ('\n')  

print ('Sorted in C-style order:') 
for x in np.nditer(a, order = 'C'): 
   print (x)  
print ('\n') 

print ('Sorted in F-style order:') 
for x in np.nditer(a, order = 'F'): 
   print (x)


# ### Modifying Array Values
# 

# In[13]:


import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('Original array is:')
print (a)
print ('\n')

for x in np.nditer(a, op_flags = ['readwrite']):
   x[...] = 2*x
print ('Modified array is:')
print (a)


# ### External Loop
# 

# In[14]:


import numpy as np 
a = np.arange(0,60,5) 
a = a.reshape(3,4) 

print ('Original array is:') 
print (a) 
print ('\n')  

print ('Modified array is:') 
for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
   print (x)


# ### Broadcasting Iteration
# 

# In[15]:


import numpy as np 
a = np.arange(0,60,5) 
a = a.reshape(3,4) 

print ('First array is:') 
print (a) 
print ('\n')  

print ('Second array is:') 
b = np.array([1, 2, 3, 4], dtype = int) 
print (b)  
print ('\n') 

print ('Modified array is:') 
for x,y in np.nditer([a,b]): 
   print ("%d:%d" % (x,y))


# In[ ]:




