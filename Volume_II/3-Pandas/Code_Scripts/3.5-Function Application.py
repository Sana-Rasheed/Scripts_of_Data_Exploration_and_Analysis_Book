#!/usr/bin/env python
# coding: utf-8

# ### adder function

# In[10]:


import pandas as pd
import numpy as np

def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
print (df.pipe(adder,2))


# ### Row or Column Wise Function Application
# 

# ### Example 1

# In[9]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean)
print (df.apply(np.mean))


# ### Example 2
# 

# In[11]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean,axis=1)
print (df.apply(np.mean))


# ### Example 3
# 

# In[12]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(lambda x: x.max() - x.min())
print (df.apply(np.mean))


# ### Element Wise Function Application
# 

# ### Example 1

# In[13]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])

# My custom function
df['col1'].map(lambda x:x*100)
print (df.apply(np.mean))


# ### Example 2

# In[15]:


import pandas as pd
import numpy as np

# My custom function
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.applymap(lambda x:x*100)
print (df.apply(np.mean))


# In[ ]:




