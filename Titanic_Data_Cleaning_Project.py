#!/usr/bin/env python
# coding: utf-8

# In[1]:

#get_ipython().system('pip install pandas matplotlib seaborn')


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a tiny dataset of daily steps
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Steps': [7000, 8500, 10000, 5000, 6000, 12000, 11000]
}
df = pd.DataFrame(data)

# 2. Plot a simple bar chart
plt.bar(df['Day'], df['Steps'], color='skyblue')
plt.title('My Weekly Step Count')
plt.xlabel('Day of the Week')
plt.ylabel('Steps Taken')

# 3. Show the chart right here in the notebook
plt.show()
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


import pandas as pd

# Load the Titanic dataset directly from a public URL
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Look at the first 5 rows of the data
df.head()


# In[5]:


# Check how many missing values are in each column
df.isnull().sum()


# In[21]:


# 1. Fill missing Ages with the median age
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

# 2. Drop the Cabin column because it's mostly empty
df = df.drop(columns=['Cabin'])

# 3. Fill missing Embarked values with 'S' (the most common port)
df['Embarked'] = df['Embarked'].fillna('S')

# 4. Check if we have any missing values left
df.isnull().sum()


# In[18]:


# Create a chart showing survival rates by Passenger Class (Pclass)
# 1 = First Class, 2 = Second Class, 3 = Third Class
sns.barplot(
    x='Pclass', 
    y='Survived', 
    hue='Pclass',          # Colors the bars by class
    data=df, 
    palette='deep', 
    errorbar=None,         # This replaces 'ci=None' to fix the warning
    legend=False           # This hides an extra unnecessary legend box
)

# Add clear labels
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class (1st, 2nd, 3rd)')
plt.ylabel('Percentage Survived')

# Show the plot
plt.show()
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


# Create a grouped bar chart looking at Class AND Gender together
sns.barplot(
    x='Pclass', 
    y='Survived', 
    hue='Sex',             # This splits each class bar into Male vs Female!
    data=df, 
    palette='muted', 
    errorbar=None
)

# Customize labels to make it look highly professional
plt.title('Titanic Survival Rates by Class and Gender', fontsize=14, fontweight='bold')
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Percentage Survived', fontsize=12)
plt.xticks([0, 1, 2], ['1st Class', '2nd Class', '3rd Class']) # Renames 1, 2, 3 to pretty text
plt.grid(axis='y', linestyle='--', alpha=0.5)               # Adds a subtle background grid

# Show the plot
plt.show()
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:




