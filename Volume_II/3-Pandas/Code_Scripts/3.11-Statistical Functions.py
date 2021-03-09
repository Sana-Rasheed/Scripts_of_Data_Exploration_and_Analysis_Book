#!/usr/bin/env python
# coding: utf-8

# ### Percent_change
# 

# In[1]:


import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,4])
print (s.pct_change())

df = pd.DataFrame(np.random.randn(5, 2))
print (df.pct_change())


# ### Covariance
# 

# In[2]:


import pandas as pd
import numpy as np
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print (s1.cov(s2))


# In[3]:


import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print (frame['a'].cov(frame['b']))
print (frame.cov())


# ### Correlation
# 

# In[4]:


import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])

print (frame['a'].corr(frame['b']))
print (frame.corr())


# ### Data Ranking
# 

# In[6]:


import pandas as pd
import numpy as nm

s = pd.Series(np.random.randn(5), index=list('abcde'))
s['d'] = s['b'] # so there's a tie
print (s.rank())


# ### .rolling() Function
# 

# In[8]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df.rolling(window=3).mean())


# ### .expanding() Function
# 

# In[9]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df.expanding(min_periods=3).mean())


# ### .ewm() Function
# 

# In[10]:


import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df.ewm(com=0.5).mean())


# In[ ]:




