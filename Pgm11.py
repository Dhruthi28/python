#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
data1 = pd.DataFrame({'apple':[1,2,3],'orange':[4,5,6]})
data2 = pd.DataFrame({'apple':[7,8,9],'orange':[10,11,12]})
frame = [data1,data2]
res = pd.concat(frame)
print(res)


# In[8]:


import pandas as pd
df = pd.read_csv('Book1.csv')
print(df.head(1))
print(df.tail(1))


# In[ ]:




