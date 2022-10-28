#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


reaction= pd.read_excel(r'C:\Users\sunka\OneDrive\Desktop\Reaction_Join.xlsx')


# In[5]:


reaction.head()

content=pd.read_excel(r"C:\Users\sunka\OneDrive\Desktop\Content_Join.xlsx")
# In[6]:


content=pd.read_excel(r"C:\Users\sunka\OneDrive\Desktop\Content_Join.xlsx")


# In[7]:


content.head()


# In[8]:


left_join=pd.merge(reaction,content,on='Content ID',how='left')


# In[9]:


left_join.head()


# In[10]:


file_name='left_join.xlsx'


# In[11]:


left_join.to_excel(file_name)


# In[12]:


print('DataFrame is written to Excel File successfully.')


# In[13]:


file_name


# In[14]:


left_join.head()


# In[15]:


left_join.to_excel(r'C:\Users\sunka\OneDrive\Desktop\Reaction_Join.xlsx',sheet_name='Sheet2',index=False)


# In[4]:


Cleaned_doc= pd.read_excel(r'C:\Users\sunka\OneDrive\Desktop\Reaction_Join.xlsx')


# In[6]:


Cleaned_doc.head()


# In[9]:


Reaction_types= pd.read_excel(r"C:\Users\sunka\Downloads\Internship\Reaction_Types.xlsx")


# In[10]:


Reaction_types.head()


# In[11]:


Answer_model=pd.merge(Cleaned_doc,Reaction_types,on='Type',how='left')


# In[12]:


Answer_model.head()


# In[15]:


Answer_model.shape


# In[16]:


Answer_model.to_excel(r"C:\Users\sunka\OneDrive\Desktop\Answer.xlsx",index=False)


# In[ ]:




