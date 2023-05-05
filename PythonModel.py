#!/usr/bin/env python
# coding: utf-8

# # Simple linear regression model 

# ## Import the relevant libraries 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()


# ## Load the data

# In[2]:


data = pd.read_csv('C:/Users/aleksandar.dimitrov/Desktop/Python Tests/1.01. Simple linear regression.csv')


# In[3]:


data


# In[4]:


data.describe()


# ## Linear Regression Creating
# 
# ##### SAT = Critical Reading + Mathematics + Writing 
# ##### GPA = Grade point average (at graduation from university)
# ##### We will create a linear regression which predicts GPA based on the SAT score obtained 

# ### Define the dependand and the independant variables
# $$y = b_0 + b_1 x_1$$

# In[5]:


y = data['GPA']
x1 = data['SAT']


# ### Data exploration

# In[6]:


plt.scatter(x1,y)
plt.xlabel('SAT',fontsize=20)
plt.ylabel('GPA',fontsize=20)
plt.show()


# ### Regression itself

# In[7]:


x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results.summary()


# In[8]:


plt.scatter(x1, y)
yhat = 0.0017*x1 + 0.275
fig = plt.plot(x1, yhat, lw=4, c='orange', label='regression line')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
plt.show()


# ## Load the categorical data

# In[9]:


categorical_data = pd.read_csv('C:/Users/aleksandar.dimitrov/Desktop/Python Tests/1.03. Dummies.csv')


# In[10]:


categorical_data


# In[11]:


cdata = categorical_data.copy()


# In[12]:


cdata['Attendance'] = cdata['Attendance'].map({'Yes': 1, 'No': 0})


# In[13]:


cdata


# In[14]:


cdata.describe()


# ### Regression 

# In[15]:


y = cdata['GPA']
x1 = cdata[['SAT', 'Attendance']]


# In[16]:


x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results.summary()


# ### We have two equations that have the same slope but different intercept
# 
# GPA = 0.8665 + 0.0014 * SAT
# 
# GPA = 0.6439 + 0.0014 * SAT 
# 

# In[17]:


plt.scatter(cdata['SAT'], y)
yhat_no = 0.6439 + 0.0014*cdata['SAT']
yhat_yes = 0.8665 + 0.0014*cdata['SAT']
fig = plt.plot(cdata['SAT'], yhat_no, lw=2, c='#006837')
fig = plt.plot(cdata['SAT'], yhat_yes, lw=2, c='#a50026')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
plt.show() 


# ## Predictions based on the regressions we created above 

# In[18]:


x


# ### We create a data frame which we use for the predictions pusposes 

# In[19]:


new_data = pd.DataFrame({'const':1, 'SAT':[1700,1670], 'Attendance':[0,1]})
new_data = new_data[['const', 'SAT','Attendance']]
new_data


# In[20]:


new_data.rename(index={0:'Bob', 1:'Alice'})


# In[21]:


predictions = results.predict(new_data)
predictions


# ### Alice scored lower on the SAT, but she attended > 75% of lectures

# In[22]:


predictionsdf = pd.DataFrame({'Predictions':predictions})
joined = new_data.join(predictionsdf)
joined.rename(index={0:'Bob', 1:'Alice'})

