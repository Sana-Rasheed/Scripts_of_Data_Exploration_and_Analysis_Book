#!/usr/bin/env python
# coding: utf-8

# ## 2. Pie Chart & Bar Chart

# In[16]:


import pandas as pd
import numpy as np
pstore = pd.read_csv("googleplaystore.csv")


# In[17]:


#importing all the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Analyzing the Content Rating column
pstore['Content Rating'].value_counts()


# In[18]:


#importing all the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Remove the rows with values which are less represented 
pstore = pstore[~pstore['Content Rating'].isin(["Adults only 18+","Unrated"])]

#Resetting the index
pstore.reset_index(inplace=True, drop=True)

#Analyzing the Content Rating column again
pstore['Content Rating'].value_counts()


# ### Pie Chart

# In[19]:


#importing all the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Plotting a pie chart
plt.figure(figsize=[9,7])
pstore['Content Rating'].value_counts().plot.pie()
plt.show()


# ### Bar Chart

# In[20]:


#importing all the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Plotting a bar chart
plt.figure(figsize=[9,7])
pstore['Content Rating'].value_counts().plot.barh()
plt.show()


# ## 3. Scatter Plots
# 

# In[4]:


import seaborn as sns
tips = sns.load_dataset("tips")


# In[5]:


sns.scatterplot(data=tips, x="total_bill", y="tip")


# In[6]:


sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")


# In[8]:


sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="time")


# In[7]:


sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="time")


# ## 4.Pair plot
# 

# In[10]:


import seaborn as sns

sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
g = sns.pairplot(iris)

import matplotlib.pyplot as plt
plt.show()


# In[11]:


g = sns.pairplot(iris, vars=["sepal_width", "sepal_length"])


# In[12]:


g = sns.pairplot(iris, diag_kind="kde")


# ## 5. Heatmap

# In[13]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)
sns.set()
uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data, vmin=0, vmax=1)
plt.show()


# ### heatmap colors

# In[14]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(50).reshape(10,5))
corr = df.corr()

ax1 = sns.heatmap(corr, cbar=0, linewidths=2,vmax=1, vmin=0, square=True, cmap='Blues')
plt.show()


# ### heatmap data

# In[15]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
ax = sns.heatmap(flights)
plt.title("Heatmap Flight Data")
plt.show()


# In[ ]:




