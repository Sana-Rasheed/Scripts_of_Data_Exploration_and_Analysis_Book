#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
plt.show()


# In[2]:


from matplotlib import pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
plt.plot(x,y)


# In[ ]:




