#!/usr/bin/env python
# coding: utf-8

# ### .loc()
# 

# ### Example 1
# 

# In[1]:


#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

#select all rows for a specific column
print (df.loc[:,'A'])


# ### Example 2
# 

# In[2]:


# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select all rows for multiple columns, say list[]
print (df.loc[:,['A','C']])


# ### Example 3
# 

# In[3]:


# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select few rows for multiple columns, say list[]
print (df.loc[['a','b','f','h'],['A','C']])


# ### Example 4
# 

# In[4]:


# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select range of rows for all columns
print (df.loc['a':'h'])


# ### Example 5
# 

# In[5]:


# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# for getting values with a boolean array
print (df.loc['a']>0)


# ## .iloc()
# 

# ### Example 1
# 

# In[6]:


# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# select all rows for a specific column
print (df.iloc[:4])


# ### Example 2
# 

# In[7]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Integer slicing
print (df.iloc[:4])
print (df.iloc[1:5, 2:4])


# ### Example 3
# 

# In[8]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Slicing through list of values
print (df.iloc[[1, 3, 5], [1, 3]])
print (df.iloc[1:3, :])
print (df.iloc[:,1:3])


# ## Use of Notations

# ### Example 1
# 

# In[12]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print (df['A'])


# ### Example 2
# 

# In[13]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

print (df[['A','B']])


# ### Example 3
# 

# In[14]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print (df[2:2])


# ### Attribute Access
# 

# In[15]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

print (df.A)


# In[ ]:




