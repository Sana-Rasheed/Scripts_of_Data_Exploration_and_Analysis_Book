#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print (s)


# ### lower()

# In[3]:


import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print (s.str.lower())


# ### upper()

# In[5]:


import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print (s.str.upper())


# ### len()
# 

# In[6]:


import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
print (s.str.len())


# ### strip()
# 

# In[7]:


import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s)
print ("After Stripping:")
print (s.str.strip())


# ### split(pattern)
# 

# In[8]:


import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s)
print ("Split Pattern:")
print (s.str.split(' '))


# ### cat(sep=pattern)
# 

# In[9]:


import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.cat(sep='_'))


# ### get_dummies()
# 

# In[10]:


import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.get_dummies())


# ### contains ()
# 

# In[11]:


import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.contains(' '))


# ### replace(a,b)
# 

# In[12]:


import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s)
print ("After replacing @ with $:")
print (s.str.replace('@','$'))


# ### repeat(value)
# 

# In[13]:


import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.repeat(2))


# ### count(pattern)
# 

# In[14]:


import pandas as pd
 
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print ("The number of 'm's in each string:")
print (s.str.count('m'))


# ### startswith(pattern)
# 

# In[15]:


import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print ("Strings that start with 'T':")
print (s.str. startswith ('T'))


# ### endswith(pattern)
# 

# In[16]:


import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print ("Strings that end with 't':")
print (s.str.endswith('t'))


# ### find(pattern)
# 

# In[17]:


import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.find('e'))


# ### findall(pattern)
# 

# In[18]:


import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.findall('e'))


# ### swapcase()
# 

# In[19]:


import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print (s.str.swapcase())


# ### islower()
# 

# In[21]:


import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print (s.str.islower())


# ### isupper()
# 

# In[22]:


import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])

print (s.str.isupper())


# ### isnumeric()
# 

# In[23]:


import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])

print (s.str.isnumeric())


# In[ ]:




