#!/usr/bin/env python
# coding: utf-8

# ### Object Creation
# 

# In[1]:


import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
print (s)


# ### pd.Categorical
# 

# In[2]:


import pandas as pd

cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print (cat)


# In[3]:


import pandas as pd

cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print (cat)


# In[4]:


import pandas as pd

cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print (cat)


# ### Description
# 

# In[5]:


import pandas as pd
import numpy as np

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"cat":cat, "s":["a", "c", "c", np.nan]})

print (df.describe())
print (df["cat"].describe())


# ### Get the Properties of the Category
# 

# In[6]:


import pandas as pd
import numpy as np

s = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print (s.categories)


# In[7]:


import pandas as pd
import numpy as np

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print (cat.ordered)


# ### Renaming Categories
# 

# In[8]:


import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
s.cat.categories = ["Group %s" % g for g in s.cat.categories]
print (s.cat.categories)


# ### Appending New Categories
# 

# In[9]:


import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
s = s.cat.add_categories([4])
print (s.cat.categories)


# ### Removing Categories
# 

# In[10]:


import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
print ("Original object:")
print (s)

print ("After removal:")
print (s.cat.remove_categories("a"))

