#!/usr/bin/env python
# coding: utf-8

# ## PyLab module

# ### Basic Plotting

# #### Example1

# In[2]:


from numpy import *
from pylab import *
x = linspace(-3, 3, 30)
y = x**2
plot(x, y)
show()


# #### Example2

# In[3]:


from pylab import *
x = linspace(-3, 3, 30)
y = x**2
plot(x, y, 'r.')
show()


# #### Example3

# In[4]:


from pylab import *
plot(x, sin(x))
plot(x, cos(x), 'r-')
plot(x, -sin(x), 'g--')
show()


# In[ ]:




