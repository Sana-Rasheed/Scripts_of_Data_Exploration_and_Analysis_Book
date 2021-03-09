#!/usr/bin/env python
# coding: utf-8

# In[30]:


import seaborn as sns


# ## 1. Distribution Plots

# In[31]:


import pandas as pd
import numpy as np
pstore = pd.read_csv("googleplaystore.csv")
pstore.head(10)


# In[32]:


#importing all the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Create a distribution plot for rating
sns.distplot(pstore.Rating)
plt.show()


# In[33]:


#Change the number of bins
sns.distplot(pstore.Rating, bins=20, kde = False)
plt.show()


# ### distribution of App ratings

# In[34]:


#importing all the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Create a distribution plot for rating
sns.distplot(pstore.Rating, bins=20, color="g")
plt.title("Distribution of app ratings", fontsize=20, color = 'red')
plt.show()


# ### Styling the Seaborn graphs

# In[35]:


#importing all the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Adding dark background to the graph
plt.style.use("dark_background")
#Create a distribution plot for rating
sns.distplot(pstore.Rating, bins=20, color="g")
plt.title("Distribution of app ratings", fontsize=20, color = 'red')
plt.show()

