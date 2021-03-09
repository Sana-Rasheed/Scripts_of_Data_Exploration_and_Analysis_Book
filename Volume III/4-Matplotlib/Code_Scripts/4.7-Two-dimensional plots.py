#!/usr/bin/env python
# coding: utf-8

# ### Creating two-dimensional plots of functions and data

# #### Example1

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


xvalues = np.linspace(-np.pi, np.pi)
yvalues1 = np.sin(xvalues)
yvalues2 = np.cos(xvalues)
plt.plot(xvalues, yvalues1, lw=2, color='red',
label='sin(x)')
plt.plot(xvalues, yvalues2, lw=2, color='blue',
label='cos(x)')
plt.title('Trigonometric Functions')
plt.xlabel('x')
plt.ylabel('sin(x), cos(x)')
plt.axhline(0, lw=0.5, color='black')
plt.axvline(0, lw=0.5, color='black')
plt.legend()
None


# ### Generating multiple plots in a single figure

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


plt.figure(figsize=(6,6))
xvalues = np.linspace(-2, 2, 100)
plt.subplot(2, 2, 1)
yvalues = xvalues
plt.plot(xvalues, yvalues, color='blue')
plt.xlabel('$x$')
plt.ylabel('$x$')
plt.subplot(2, 2, 2)
yvalues = xvalues ** 2
plt.plot(xvalues, yvalues, color='green')
plt.xlabel('$x$')
plt.ylabel('$x^2$')
plt.subplot(2, 2, 3)
yvalues = xvalues ** 3
plt.plot(xvalues, yvalues, color='red')
plt.xlabel('$x$')
plt.ylabel('$x^3$')
plt.subplot(2, 2, 4)
yvalues = xvalues ** 4
plt.plot(xvalues, yvalues, color='black')
plt.xlabel('$x$')
plt.ylabel('$x^3$')
plt.suptitle('Polynomial Functions')
plt.tight_layout()
plt.subplots_adjust(top=0.90)
None


# In[ ]:




