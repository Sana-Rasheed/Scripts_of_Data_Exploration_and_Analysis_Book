#!/usr/bin/env python
# coding: utf-8

# ### Working with Images

# In[14]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('matplotlib.png')


# In[15]:


plt.imsave("matplotlib.png", img, cmap = 'gray', origin = 'lower')


# In[16]:


imgplot = plt.imshow(img)


# In[ ]:




