#!/usr/bin/env python
# coding: utf-8

# ### numpy.amin() and numpy.amax()
# 

# In[1]:


import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 

print ('Our array is:') 
print (a)  
print ('\n')  

print ('Applying amin() function:') 
print (np.amin(a,1)) 
print ('\n')  

print ('Applying amin() function again:') 
print (np.amin(a,0)) 
print ('\n')  

print ('Applying amax() function:') 
print (np.amax(a)) 
print ('\n')  

print ('Applying amax() function again:') 
print (np.amax(a, axis = 0))


# ### numpy.ptp()
# 

# In[2]:


import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 

print ('Our array is:') 
print (a) 
print ('\n')  

print ('Applying ptp() function:') 
print (np.ptp(a)) 
print ('\n')  

print ('Applying ptp() function along axis 1:') 
print (np.ptp(a, axis = 1)) 
print ('\n')   

print ('Applying ptp() function along axis 0:')
print (np.ptp(a, axis = 0)) 


# ### numpy.percentile()
# 

# In[3]:


import numpy as np 
a = np.array([[30,40,70],[80,20,10],[50,90,60]]) 

print ('Our array is:') 
print (a) 
print ('\n')  

print ('Applying percentile() function:') 
print (np.percentile(a,50)) 
print ('\n')  

print ('Applying percentile() function along axis 1:') 
print (np.percentile(a,50, axis = 1)) 
print ('\n')  

print ('Applying percentile() function along axis 0:') 
print (np.percentile(a,50, axis = 0))


# ### numpy.median()
# 

# In[4]:


import numpy as np 
a = np.array([[30,65,70],[80,95,10],[50,90,60]]) 

print ('Our array is:') 
print (a) 
print ('\n')  

print ('Applying median() function:') 
print (np.median(a)) 
print ('\n')  

print ('Applying median() function along axis 0:') 
print (np.median(a, axis = 0)) 
print ('\n')  
 
print ('Applying median() function along axis 1:') 
print (np.median(a, axis = 1))


# ### numpy.mean()
# 

# In[5]:


import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 

print ('Our array is:') 
print (a) 
print ('\n')  

print ('Applying mean() function:') 
print (np.mean(a)) 
print ('\n')  

print ('Applying mean() function along axis 0:') 
print (np.mean(a, axis = 0)) 
print ('\n')  

print ('Applying mean() function along axis 1:') 
print (np.mean(a, axis = 1))


# ### numpy.average()
# 

# In[6]:


import numpy as np 
a = np.array([1,2,3,4]) 

print ('Our array is:') 
print (a) 
print ('\n')  

print ('Applying average() function:') 
print (np.average(a)) 
print ('\n')  

# this is same as mean when weight is not specified 
wts = np.array([4,3,2,1]) 

print ('Applying average() function again:') 
print (np.average(a,weights = wts)) 
print ('\n')  

# Returns the sum of weights, if the returned parameter is set to True. 
print ('Sum of weights') 
print (np.average([1,2,3, 4],weights = [4,3,2,1], returned = True))


# In[7]:


import numpy as np 
a = np.arange(6).reshape(3,2) 

print ('Our array is:') 
print (a) 
print ('\n')  

print ('Modified array:') 
wt = np.array([3,5]) 
print (np.average(a, axis = 1, weights = wt)) 
print ('\n')  

print ('Modified array:') 
print (np.average(a, axis = 1, weights = wt, returned = True))


# ### Standard Deviation
# 

# In[8]:


import numpy as np 
print (np.std([1,2,3,4]))


# ### Variance
# 

# In[9]:


import numpy as np 
print (np.var([1,2,3,4]))


# In[ ]:




