#!/usr/bin/env python
# coding: utf-8

# ## Trigonometric Functions
# 

# ### Example 1

# In[1]:


import numpy as np 
a = np.array([0,30,45,60,90]) 

print ('Sine of different angles:') 
# Convert to radians by multiplying with pi/180 
print (np.sin(a*np.pi/180)) 
print ('\n')  

print ('Cosine values for angles in array:') 
print (np.cos(a*np.pi/180)) 
print ('\n')  

print ('Tangent values for given angles:') 
print (np.tan(a*np.pi/180)) 


# ### Example 2

# In[3]:


import numpy as np 
a = np.array([0,30,45,60,90]) 

print ('Array containing sine values:') 
sin = np.sin(a*np.pi/180)
print (sin) 
print ('\n')  

print ('Compute sine inverse of angles. Returned values are in radians.') 
inv = np.arcsin(sin) 
print (inv) 
print ('\n')  

print ('Check result by converting to degrees:') 
print (np.degrees(inv)) 
print ('\n')  

print ('arccos and arctan functions behave similarly:') 
cos = np.cos(a*np.pi/180) 
print (cos) 
print ('\n')  

print ('Inverse of cos:') 
inv = np.arccos(cos) 
print (inv) 
print ('\n')  

print ('In degrees:') 
print (np.degrees(inv)) 
print ('\n')  

print ('Tan function:') 
tan = np.tan(a*np.pi/180) 
print (tan)
print ('\n')  

print ('Inverse of tan:') 
inv = np.arctan(tan) 
print (inv) 
print ('\n')  

print ('In degrees:') 
print (np.degrees(inv)) 


# ### Functions for Rounding
# 

# In[4]:


import numpy as np 
a = np.array([1.0,5.55, 123, 0.567, 25.532]) 

print ('Original array:') 
print (a) 
print ('\n')  

print ('After rounding:') 
print (np.around(a)) 
print (np.around(a, decimals = 1)) 
print (np.around(a, decimals = -1))


# ### numpy.floor()
# 

# In[5]:


import numpy as np 
a = np.array([-1.7, 1.5, -0.2, 0.6, 10]) 

print ('The given array:') 
print (a) 
print ('\n')  

print ('The modified array:') 
print (np.floor(a))


# ### numpy.ceil()
# 

# In[6]:


import numpy as np 
a = np.array([-1.7, 1.5, -0.2, 0.6, 10]) 

print ('The given array:') 
print (a) 
print ('\n')  

print ('The modified array:') 
print (np.ceil(a))


# In[ ]:




