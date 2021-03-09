#!/usr/bin/env python
# coding: utf-8

# ### Importing Libraries

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")


# ### Apply the  default seaborn theme, scaling, and color palette

# In[6]:


# Plot color palette
def plot_color_palette(palette: str):
    figure = sns.palplot(sns.color_palette())
    plt.xlabel("Color palette: " + palette)
    plt.show(figure)

palettes = ["deep", "muted", "pastel", "bright", "dark", "colorblind"]
for palette in palettes:
    sns.set(palette=palette)
    plot_color_palette(palette)


# ### Load your dataset

# In[7]:


tips = sns.load_dataset("tips")
tips.head()


# ### Plot data

# In[9]:


# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_style()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(x="total_bill", y="tip", 
            col="time", # Categorical variables that will determine the faceting of the grid.
            hue="smoker", # Grouping variable that will produce elements with different colors.
            style="smoker", # Grouping variable that will produce elements with different styles.
            size="size", # Grouping variable that will produce elements with different sizes.
            data=tips)


# ### Example1

# In[11]:


sns.lmplot(x="total_bill", y="tip", data=tips)


# ### Example2

# In[12]:


sns.lmplot(x="size", y="tip", data=tips)


# ### Example3

# In[13]:


import numpy as np
sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean)


# ### Example4
# 

# In[14]:


tips["big_tip"] = (tips.tip / tips.total_bill) > .15
sns.lmplot(x="total_bill", y="big_tip",
           y_jitter=.03, 
           logistic=True, 
           data=tips)


# ### Example5

# In[15]:


sns.jointplot(x="total_bill", y="tip", 
              kind="reg", # Options are "scatter", "reg", "resid", "kde", "hex"
              data=tips)


# ### Example6

# In[16]:


sns.pairplot(hue="smoker", # Grouping variable that will produce elements with different colors.
             data=tips)


# ## API abstraction across visualizations

# In[11]:


dots = sns.load_dataset("dots")
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
)


# ## Statistical estimation and error bars

# In[12]:


fmri = sns.load_dataset("fmri")
sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", col="region",
    hue="event", style="event",
)


# In[13]:


sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")


# ## Specialized plots for categorical data

# ### Example1

# In[14]:


sns.catplot(x="day", y="total_bill", 
            hue="smoker", # Grouping variable that will produce elements with different colors.
            kind="swarm", # Options are: "point", "bar", "strip", "swarm", "box", "violin", or "boxen"
            data=tips)


# ### Example2

# In[15]:


sns.catplot(x="day", y="total_bill", 
            hue="smoker", # Grouping variable that will produce elements with different colors.
            kind="violin", # Options are: "point", "bar", "strip", "swarm", "box", "violin", or "boxen"
            split=True, 
            data=tips)


# ### Example3

# In[16]:


sns.catplot(x="day", y="total_bill", 
            hue="smoker", # Grouping variable that will produce elements with different colors.
            kind="bar", # Options are: "point", "bar", "strip", "swarm", "box", "violin", or "boxen"
            data=tips)


# ### Opinionated defaults and flexible customization

# In[18]:


sns.relplot(
    data=df,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g"
)


# In[ ]:




