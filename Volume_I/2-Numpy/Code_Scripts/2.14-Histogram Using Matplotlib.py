#!/usr/bin/env python
# coding: utf-8

# ### numpy.histogram()
# 

# In[1]:


import numpy as np 
   
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
np.histogram(a,bins = [0,20,40,60,80,100]) 
hist,bins = np.histogram(a,bins = [0,20,40,60,80,100]) 
print (hist) 
print (bins) 


# ### plt()
# 

# In[2]:


from matplotlib import pyplot as plt 
import numpy as np  
   
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
plt.hist(a, bins = [0,20,40,60,80,100]) 
plt.title("histogram") 
plt.show()


# ### numpy.save()
# 

# In[3]:


import numpy as np 
a = np.array([1,2,3,4,5]) 
np.save('outfile',a)


# In[4]:


import numpy as np 
b = np.load('outfile.npy') 
print (b) 


# ### savetxt()
# 

# In[5]:


import numpy as np 

a = np.array([1,2,3,4,5]) 
np.savetxt('out.txt',a) 
b = np.loadtxt('out.txt') 
print (b) 


# In[ ]:




