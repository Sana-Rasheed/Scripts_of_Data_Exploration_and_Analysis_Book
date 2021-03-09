#!/usr/bin/env python
# coding: utf-8

# ## get_option(param)
# 

# ### display.max_rows
# 

# In[3]:


import pandas as pd
print (pd.get_option("display.max_rows"))


# ### display.max_columns
# 

# In[4]:


import pandas as pd
print (pd.get_option("display.max_columns"))


# ## set_option(param,value)
# 

# ### display.max_rows
# 

# In[8]:


import pandas as pd

pd.set_option("display.max_rows",80)

print (pd.get_option("display.max_rows"))


# ### display.max_columns
# 

# In[9]:


import pandas as pd

pd.set_option("display.max_columns",30)

print (pd.get_option("display.max_columns"))


# ### reset_option(param)
# 

# In[10]:


import pandas as pd

pd.reset_option("display.max_rows")
print (pd.get_option("display.max_rows"))


# ### describe_option(param)
# 

# In[11]:


import pandas as pd
pd.describe_option("display.max_rows")


# ### option_context()
# 

# In[12]:


import pandas as pd
with pd.option_context("display.max_rows",10):
   print(pd.get_option("display.max_rows"))
   print(pd.get_option("display.max_rows"))


# In[ ]:




