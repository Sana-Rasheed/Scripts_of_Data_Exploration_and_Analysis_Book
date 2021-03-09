#!/usr/bin/env python
# coding: utf-8

# ### Applying Aggregations on DataFrame
# 

# In[1]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])

print (df)
r = df.rolling(window=3,min_periods=1)
print (r)


# ### Apply Aggregation on a Whole Dataframe
# 

# In[2]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r.aggregate(np.sum))


# ### Apply Aggregation on a Single Column of a Dataframe
# 

# In[4]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r['A'].aggregate(np.sum))


# ### Apply Aggregation on Multiple Columns of a DataFrame

# In[5]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r[['A','B']].aggregate(np.sum))


# ### Apply Multiple Functions on a Single Column of a DataFrame
# 

# In[6]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r['A'].aggregate([np.sum,np.mean]))


# ### Apply Multiple Functions on Multiple Columns of a DataFrame
# 

# In[7]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r[['A','B']].aggregate([np.sum,np.mean]))


#  ### Apply Different Functions to Different Columns of a Dataframe
# 

# In[8]:


import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randn(3, 4),
   index = pd.date_range('1/1/2000', periods=3),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r.aggregate({'A' : np.sum,'B' : np.mean}))


# In[ ]:




