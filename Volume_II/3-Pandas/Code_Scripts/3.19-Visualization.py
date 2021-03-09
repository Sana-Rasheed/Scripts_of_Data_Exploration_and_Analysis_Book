#!/usr/bin/env python
# coding: utf-8

# ### Basic Plotting: plot
# 

# In[1]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
   periods=10), columns=list('ABCD'))

df.plot()


# ### Bar Plot
# 

# In[5]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10,4),columns=('a','b','c','d'))
df.plot.bar()


# In[6]:


import pandas as pd
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar(stacked=True)


# In[7]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])

df.plot.barh(stacked=True)


# ### Histograms
# 

# In[8]:


import pandas as pd
import numpy as np

df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

df.plot.hist(bins=20)


# In[22]:


import pandas as pd
import numpy as np

df=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1,'d':np.random.randn(1000)-2}, columns=['a', 'b', 'c','d'])

df.hist(bins=20)


# In[19]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box()


# In[15]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.area()


# In[16]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b')


# In[17]:


import pandas as pd
import numpy as np

df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)


# In[ ]:




