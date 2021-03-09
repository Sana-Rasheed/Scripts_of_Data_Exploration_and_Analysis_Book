#!/usr/bin/env python
# coding: utf-8

# # Pandas - Series

# ### Create an Empty Series

# In[ ]:


#import the pandas library and aliasing as pd
import pandas as pd
s = pd.Series()
print (s)


# ### Create a Series from ndarray

# #### Example 1

# In[5]:


#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print (s)


# #### Example 2

# In[6]:


#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)


# ### Create a Series from dict

# #### Example 1

# In[ ]:


#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print (s) 


# #### Example 2

# In[8]:


#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print (s)


# ### Create a Series from Scalar

# In[9]:


#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
s = pd.Series(5, index=[0, 1, 2, 3])
print (s)


# ### Accessing Data from Series with Position

# #### Example 1

# In[10]:


import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print (s[0])


# #### Example 2

# In[11]:


import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first three element
print (s[:3])


# #### Example 3

# In[12]:


import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the last three element
print (s[-3:])


# ### Retrieve Data Using Label (Index)

# #### Example 1

# In[13]:


import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve a single element
print (s['a'])


# #### Example 2

# In[14]:


import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve multiple elements
print (s[['a','c','d']])


# #### Example 3

# In[15]:


import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve multiple elements
print (s['f'])


# In[ ]:




