#!/usr/bin/env python
# coding: utf-8

# ### Example 1
# 

# In[1]:


import numpy as np 
a = np.arange(10) 
s = slice(2,7,2) 
print (a[s])


# ### Example 2
# 

# In[2]:


import numpy as np 
a = np.arange(10) 
b = a[2:7:2] 
print (b)


# ### Example 3
# 

# In[3]:


# slice single item 
import numpy as np 

a = np.arange(10) 
b = a[5] 
print (b)


# ### Example 4
# 

# In[4]:


# slice items starting from index 
import numpy as np 
a = np.arange(10) 
print (a[2:])


# ### Example 5
# 

# In[5]:


# slice items between indexes 
import numpy as np 
a = np.arange(10) 
print (a[2:5])


# ### Example 6
# 

# In[7]:


import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print (a)  

# slice items starting from index
print ('Now we will slice the array from the index a[1:]') 
print (a[1:])


# ### Example 7
# 

# In[8]:


# array to begin with 
import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 

print ('Our array is:') 
print (a) 
print ('\n')  

# this returns array of items in the second column 
print ('The items in the second column are:')  
print (a[...,1]) 
print ('\n')  

# Now we will slice all items from the second row 
print ('The items in the second row are:') 
print (a[1,...])
print ('\n')  

# Now we will slice all items from column 1 onwards 
print ('The items column 1 onwards are:')
print (a[...,1:])


# ### Integer Indexing
# 

# ### Example 1
# 

# In[9]:


import numpy as np 

x = np.array([[1, 2], [3, 4], [5, 6]]) 
y = x[[0,1,2], [0,1,0]] 
print (y)


# ### Example 2
# 

# In[11]:


import numpy as np 
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
   
print ('Our array is:') 
print (x) 
print ('\n') 

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols] 
   
print ('The corner elements of this array are:')
print (y)


# ### Example 3
# 

# In[12]:


import numpy as np 
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

print ('Our array is:') 
print (x) 
print ('\n')  

# slicing 
z = x[1:4,1:3] 

print ('After slicing, our array becomes:') 
print (z) 
print ('\n')  

# using advanced index for column 
y = x[1:4,[1,2]] 

print ('Slicing using advanced index for column:') 
print (y)


# ### Boolean Array Indexing
# 

# ### Example 1
# 

# In[13]:


import numpy as np 
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

print ('Our array is:') 
print (x) 
print ('\n')  

# Now we will print the items greater than 5 
print ('The items greater than 5 are:') 
print (x[x > 5])


# ### Example 2
# 

# In[15]:


import numpy as np 
a = np.array([np.nan, 1,2,np.nan,3,4,5]) 
print (a[~np.isnan(a)])


# ### Example 3
# 

# In[16]:


import numpy as np 
a = np.array([1, 2+6j, 5, 3.5+5j]) 
print (a[np.iscomplex(a)])


# In[ ]:




