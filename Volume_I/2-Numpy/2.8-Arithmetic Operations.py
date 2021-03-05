#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
a = np.arange(9, dtype = np.float_).reshape(3,3) 

print ('First array:') 
print (a) 
print ('\n')  

print ('Second array:') 
b = np.array([10,10,10]) 
print (b) 
print ('\n')  

print ('Add the two arrays:') 
print (np.add(a,b)) 
print ('\n')  

print ('Subtract the two arrays:') 
print (np.subtract(a,b)) 
print ('\n')  

print ('Multiply the two arrays:') 
print (np.multiply(a,b)) 
print ('\n')  

print ('Divide the two arrays:') 
print (np.divide(a,b))


# ### numpy.reciprocal()
# 

# In[2]:


import numpy as np 
a = np.array([0.25, 1.33, 1, 0, 100]) 

print ('Our array is:') 
print (a) 
print ('\)n')  

print ('After applying reciprocal function:') 
print (np.reciprocal(a)) 
print ('\n')  

b = np.array([100], dtype = int) 
print ('The second array is:') 
print (b) 
print ('\n')  

print ('After applying reciprocal function:') 
print (np.reciprocal(b)) 


# ### numpy.power()
# 

# In[3]:


import numpy as np 
a = np.array([10,100,1000]) 

print ('Our array is:') 
print (a) 
print ('\n')  

print ('Applying power function:') 
print (np.power(a,2)) 
print ('\n')  

print ('Second array:') 
b = np.array([1,2,3]) 
print (b) 
print ('\n')  

print ('Applying power function again:') 
print (np.power(a,b))


# ### numpy.mod()
# 

# In[4]:


import numpy as np 
a = np.array([10,20,30]) 
b = np.array([3,5,7]) 

print ('First array:') 
print (a) 
print ('\n')  

print ('Second array:') 
print (b) 
print ('\n')  

print ('Applying mod() function:') 
print (np.mod(a,b)) 
print ('\n')  

print ('Applying remainder() function:') 
print (np.remainder(a,b)) 


# In[5]:


import numpy as np 
a = np.array([-5.6j, 0.2j, 11. , 1+1j]) 

print ('Our array is:') 
print (a) 
print ('\n')  

print ('Applying real() function:') 
print (np.real(a)) 
print ('\n')  

print ('Applying imag() function:') 
print (np.imag(a)) 
print ('\n')  

print ('Applying conj() function:') 
print (np.conj(a)) 
print ('\n')  

print ('Applying angle() function:') 
print (np.angle(a)) 
print ('\n')  

print ('Applying angle() function again (result in degrees)') 
print (np.angle(a, deg = True))


# In[ ]:




