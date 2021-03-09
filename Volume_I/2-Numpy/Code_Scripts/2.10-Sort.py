#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np  
a = np.array([[3,7],[9,1]]) 

print ('Our array is:') 
print (a) 
print ('\n')

print ('Applying sort() function:') 
print (np.sort(a)) 
print ('\n') 
  
print ('Sort along axis 0:') 
print (np.sort(a, axis = 0)) 
print ('\n')  

# Order parameter in sort function 
dt = (np.dtype([('name', 'S10'),('age', int)])) 
a = (np.array([("raju",21),("anil",25),("ravi", 17), ("amar",27)], dtype = dt)) 

print ('Our array is:') 
print (a) 
print ('\n')  

print ('Order by name:') 
print (np.sort(a, order = 'name'))


# ### numpy.argsort()
# 

# In[4]:


import numpy as np 
x = np.array([3, 1, 2]) 

print ('Our array is:') 
print (x) 
print ('\n')  

print ('Applying argsort() to x:') 
y = np.argsort(x) 
print (y) 
print ('\n')  

print ('Reconstruct original array in sorted order:') 
print (x[y]) 
print ('\n')  

print ('Reconstruct the original array using loop:') 
for i in y: 
   print (x[i])


# ### numpy.lexsort()
# 

# In[5]:


import numpy as np 

nm = ('raju','anil','ravi','amar') 
dv = ('f.y.', 's.y.', 's.y.', 'f.y.') 
ind = np.lexsort((dv,nm)) 

print ('Applying lexsort() function:') 
print (ind) 
print ('\n')  

print ('Use this index to get sorted data:') 
print ([nm[i] + ", " + dv[i] for i in ind]) 


# ### numpy.argmax() and numpy.argmin()
# 

# In[6]:


import numpy as np 
a = np.array([[30,40,70],[80,20,10],[50,90,60]]) 

print ('Our array is:') 
print (a) 
print ('\n') 

print ('Applying argmax() function:') 
print (np.argmax(a)) 
print ('\n')  

print ('Index of maximum number in flattened array')
print (a.flatten()) 
print ('\n')  

print ('Array containing indices of maximum along axis 0:') 
maxindex = np.argmax(a, axis = 0) 
print (maxindex) 
print ('\n')  

print ('Array containing indices of maximum along axis 1:') 
maxindex = np.argmax(a, axis = 1) 
print (maxindex) 
print ('\n')  

print ('Applying argmin() function:') 
minindex = np.argmin(a) 
print (minindex) 
print ('\n')  
   
print ('Flattened array:') 
print (a.flatten()[minindex]) 
print ('\n')  

print ('Flattened array along axis 0:') 
minindex = np.argmin(a, axis = 0) 
print (minindex)
print ('\n')

print ('Flattened array along axis 1:') 
minindex = np.argmin(a, axis = 1) 
print (minindex)


# ### numpy.nonzero()
# 

# In[7]:


import numpy as np 
a = np.array([[30,40,0],[0,20,10],[50,0,60]]) 

print ('Our array is:') 
print (a) 
print ('\n')  

print ('Applying nonzero() function:') 
print (np.nonzero (a))


# ### numpy.where()
# 

# In[8]:


import numpy as np 
x = np.arange(9.).reshape(3, 3) 

print ('Our array is:') 
print (x)  

print ('Indices of elements > 3') 
y = np.where(x > 3) 
print (y)  

print ('Use these indices to get elements satisfying the condition') 
print (x[y])


# ### numpy.extract()
# 

# In[10]:


import numpy as np 
x = np.arange(9.).reshape(3, 3) 

print ('Our array is:') 
print (x)  

# define a condition 
condition = np.mod(x,2) == 0 

print ('Element-wise value of condition') 
print (condition)  

print ('Extract elements using condition') 
print (np.extract(condition, x))


# In[ ]:




