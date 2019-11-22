
# coding: utf-8

# In[169]:


#Assignment 5

#Use pandas.read_csv to load the file pivot_table_data.csv into a pandas.DataFrame called df:


# In[170]:


import pandas as pd 


# In[171]:


df = pd.read_csv('pivot_table_data.csv')


# In[172]:


df.head(5)


# In[173]:


#a. Consider the function

def df_filter(x):
    return (x < 0.5) & (x > -0.5)


# In[174]:


df_filter = df_filter(df['filter'])


# In[175]:


df_filtered = df.drop(df[df_filter == False].index)


# In[176]:


df_filtered.head(2)


# In[177]:


#b. A cross-tabulation counts the size of the groups formed from bucketing entries according to their values in different columns.
#Use pd.crosstab to define a pandas.DataFrame called df_crosstab with index row and columns column.


df_crosstab = pd.crosstab(df.row, df.column)


# In[178]:


df_crosstab


# In[179]:


#Use pd.pivot_table to define a pandas.DataFrame called df_pivot_table with
#data equal to df_filter
#index set to row column
#columns set to column column
#values from the value column
#aggfunc equal to max_min


# In[180]:


def max_min(x):
    return x.max() - x.min()


# In[181]:


df_pivot_table = pd.pivot_table(data = df, index = df['row'], columns = df['column'], values = 'value', aggfunc = max_min)


# In[182]:


df_pivot_table.head(1)


# In[225]:



import pandas as pd

df_raw = pd.read_csv("raw_data.csv")


# In[226]:


df_raw.head(3)


# In[227]:


#Replace times_of_trade with Time
df_raw.columns = ['Volume', 'Price', 'Time']
df_raw.head(3)


# In[229]:


#Transform each entry in Time to the format mm-dd-yyyy hh:mm:ss
#Use pd.to_datetime to convert each string in Time to a date-time
time = pd.to_datetime(df_raw['Time'])
time = time.dt.strftime('%m-%d-%Y %H:%M:%S')
df_raw['Time'] = pd.to_datetime(time)
df_raw.head(3)


# In[230]:


#Apply sort_values to sort by the entries in Time

df_raw.sort_values(by='Time')
df_raw.head(3)


# In[231]:


df_raw['Time'] = df_raw['Time'].dt.tz_localize('UTC')
df_raw['Time'] = df_raw['Time'].dt.tz_convert('US/Eastern')


# In[232]:


df_raw.set_index('Time', inplace = True)
df_raw.head(3)


# In[198]:


import pickle 
import matplotlib.pyplot as plt


with open('./trainset_x.pickle','rb') as handle_x:
    fileX = pickle.load(handle_x)
    
with open('./trainset_y.pickle','rb') as handle_y:
    fileY = pickle.load(handle_y)
    
plt.scatter(fileX, fileY, color='blue')
plt.title('Training Set: 100 Samples')


# In[199]:


from sklearn.tree import DecisionTreeRegressor

tree_regressor_max2 = DecisionTreeRegressor(max_depth=2)

tree_regressor_max5 = DecisionTreeRegressor(max_depth=5)


# In[200]:


tree_regressor_max2.fit(fileX, fileY)
tree_regressor_max5.fit(fileX, fileY)


# In[201]:


import numpy as np

test_set_x = np.reshape(np.linspace(0,2*np.pi,1000), (1000,1))
test_set_y5 = tree_regressor_max5.predict(test_set_x) 
plt.plot(test_set_x, test_set_y5, color='darkorange', label='train set', lw='5')
plt.scatter(fileX, fileY, color='b', edgecolors='k', label = 'test set')
plt.legend()
plt.title('Testing Set: Decision Tree Regressor Depth 5')


# In[202]:


test_set_x = np.reshape(np.linspace(0,2*np.pi,1000), (1000,1))
test_set_y2 = tree_regressor_max2.predict(test_set_x) 
plt.plot(test_set_x, test_set_y2, color='darkorange', label='train set', lw='5')
plt.scatter(fileX, fileY, color= 'b', edgecolors='k', label = 'test set')
plt.legend()
plt.title('Testing Set: Decision Tree Regressor Depth 2')


# In[203]:


tree_regressor_max5_min4 = DecisionTreeRegressor(max_depth=5, min_samples_leaf=4)
tree_regressor_max5_min4.fit(fileX, fileY)
test_regressor_max5_min4 = tree_regressor_max5_min4.predict(test_set_x)
plt.plot(test_set_x, test_regressor_max5_min4, color='darkorange', label='train set', lw='5')
plt.scatter(fileX, fileY, color='b', edgecolors='k', label = 'test set')
plt.legend()

plt.title('Testing Set: Decision Tree Regressor Depth 5, leaf minimum 4')

