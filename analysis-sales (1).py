#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import os
import glob


# In[2]:


##### task 1 merging 1 months of sales data into one #####


# In[53]:


# df = pd.read_csv("./Sales_Data/Sales_April_2019.csv")
files = [file for file in os.listdir("./Sales_Data")]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv("./Sales_Data/"+file)
    all_months_data = pd.concat([all_months_data, df])
all_months_data.to_csv('all_data.csv', index = False)
all_data = pd.read_csv("./all_data.csv")
all_data


# In[ ]:


# add additional column


# In[99]:


all_data["month"] = all_data['Order Date'].str[0:2]
all_data['month'] = all_data['month'].astype('int32')
all_data.head()


# delete NaN rows

# In[100]:


nan_df = all_data[all_data.isna().any(axis=1)]

all_data = all_data.dropna(how='all')
all_data.head()


# In[69]:


# find 'or'


# In[101]:


all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
all_data.head()


# In[70]:


#### Make quanitity and price correct types


# In[102]:


all_data["Quantity Ordered"] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])


# What was the best month for sales?

# In[67]:


#add sales column


# In[103]:


all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data.head()


# In[95]:


results = all_data.groupby('month').sum()


# In[116]:


def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]
all_data['City Purchased'] = all_data['Purchase Address'].apply(lambda x: f"{get_city(x)} {get_state(x)}")
all_data.head()


# In[118]:


results_city = all_data.groupby('City Purchased').sum()
results_city


# In[120]:


import matplotlib.pyplot as plt

results = all_data.groupby('month').sum()

months = range(1, 13)

plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD $')
plt.xlabel('Month Number')
plt.show()


# In[126]:


import matplotlib.pyplot as plt

results_city = all_data.groupby('City Purchased').sum()
results_city

cities = [city for city,df in all_data.groupby('City Purchased') ]

plt.bar(cities, results_city['Sales'])
plt.xticks(cities, rotation='vertical', fontsize=8)
plt.ylabel('Sales in USD $')
plt.xlabel('City Name')
plt.show()


# In[83]:


##### Q2: What U.S City had the highest number of Sales


# In[84]:


# create new column showing the cities


# In[93]:





# In[ ]:


## What time should we advertise to max sales


# In[132]:


all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
all_data.head()


# In[134]:


all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
all_data.head()


# In[139]:


hours = [hour for hour,df in all_data.groupby('Hour')]
plt.plot(hours, all_data.groupby(['Hour']).count())

plt.xticks(hours)
plt.grid()
plt.show()


# In[140]:


# What products are sold together


# In[142]:


df = all_data[all_data['Order ID'].duplicated(keep=False)]
df.head(20)


# In[150]:


df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df.head()
df = df[['Order ID', 'Grouped']].drop_duplicates()
df.head(import )


# In[ ]:


#Best day of the month for sales


# In[151]:


all_data['day'] = all_data['Order Date'].dt.day
all_data.head()


# In[157]:


days = [day for day,df in all_data.groupby('day')]




f = plt.figure()
f.set_figwidth(10)
f.set_figheight(6)
plt.plot(days, all_data.groupby(['day']).count())
plt.xticks(days)
plt.grid()
plt.show()


# In[ ]:





from itertools import combinations
from collections import counter
counter = Counter()

for row in df['Grouped']:
    row_list = row.split(',')
    counter.update(Counter(combinations(row_list, 2)))
counter.most_common(10)
