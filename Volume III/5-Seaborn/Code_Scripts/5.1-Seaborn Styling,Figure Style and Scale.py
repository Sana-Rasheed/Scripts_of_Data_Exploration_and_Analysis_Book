#!/usr/bin/env python
# coding: utf-8

# ## Customizing the Overall Look of Your Figure

# ### Built-in Themes

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


tips = sns.load_dataset("tips")


# In[3]:


sns.set_style("darkgrid")
sns.stripplot(x="day", y="total_bill", data=tips)


# ### Background Color

# In[4]:


sns.set_style("dark")
sns.stripplot(x="day", y="total_bill", data=tips)


# In[5]:


sns.set_style("ticks")
sns.stripplot(x="day", y="total_bill", data=tips)


# ### Grids

# In[6]:


sns.set_style("whitegrid")
sns.stripplot(x="day", y="total_bill", data=tips)


# In[7]:


sns.set_style("white")
sns.stripplot(x="day", y="total_bill", data=tips)


# ### Despine

# In[8]:


sns.set_style("white")
sns.stripplot(x="day", y="total_bill", data=tips)
sns.despine()


# In[9]:


sns.set_style("whitegrid")
sns.stripplot(x="day", y="total_bill", data=tips)
sns.despine(left=True, bottom=True)


# ## Scaling Figure Styles for Different Mediums

# ### Scaling Plots

# In[10]:


sns.set_style("ticks")
 
# Smallest context:
sns.set_context("paper")
sns.stripplot(x="day", y="total_bill", data=tips)


# In[11]:


sns.set_style("ticks")
 
# Largest Context:
sns.set_context("poster")
sns.stripplot(x="day", y="total_bill", data=tips)


# ### Scaling Fonts and Line Widths

# In[12]:


# Set font scale and reduce grid line width to match
sns.set_context("poster", font_scale = .5, rc={"grid.linewidth": 0.6})
sns.stripplot(x="day", y="total_bill", data=tips)


# In[13]:


# Set font scale and increase grid line width to match
sns.set_context("poster", font_scale = 1, rc={"grid.linewidth": 5})
sns.stripplot(x="day", y="total_bill", data=tips)


# ### The RC Parameter

# In[14]:


sns.set_style("ticks")
sns.set_context("poster")
sns.stripplot(x="day", y="total_bill", data=tips)
sns.plotting_context()


# ### How To Temporarily Set The Plot Style
# 

# In[1]:


# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
iris = sns.load_dataset("iris")
tips = sns.load_dataset("tips")

# Set axes style to white for first subplot
with sns.axes_style("white"):
    plt.subplot(211)
    sns.swarmplot(x="species", y="petal_length", data=iris)

# Initialize second subplot
plt.subplot(212)

# Plot violinplot
sns.violinplot(x = "total_bill", data=tips)

# Show the plot                   
plt.show()


# ### How To Set The Figure Size in Seaborn
# 

# In[2]:


# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Initialize Figure and Axes object
fig, ax = plt.subplots(figsize=(10,4))

# Load in the data
iris = sns.load_dataset("iris")

# Create swarmplot
sns.swarmplot(x="species", y="petal_length", data=iris, ax=ax)

# Show plot
plt.show()


# In[3]:


# Import the libraries
import matplotlib.pyplot as plt
import seaborn as sns 

# Load data
titanic = sns.load_dataset("titanic")

# Set up a factorplot
g = sns.factorplot("class", "survived", "sex", data=titanic, kind="bar", size=6, aspect=2, palette="muted", legend=False)

# Show plot
plt.show()


# In[ ]:




