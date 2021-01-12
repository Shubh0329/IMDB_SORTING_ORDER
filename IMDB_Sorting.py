#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd


# In[21]:


df1 = pd.read_csv("tmdb_5000_credits.csv")
df1.head()


# In[22]:


df1.info()


# In[23]:


df1.shape


# In[24]:


df2 = pd.read_csv("tmdb_5000_movies.csv")
df2.head()


# In[28]:


df1.columns = ['id','tittle','Cast','Crew']
df2=df2.merge(df1,on='id')


# In[30]:


df2.head()


# In[32]:


df2.columns


# In[33]:


df1.columns


# In[34]:


c = df2['vote_average'].mean()
c


# In[36]:


m = df2['vote_count'].quantile(0.9)
m


# In[38]:


list_movies = df2.copy().loc[df2['vote_count'] >= m]
list_movies.shape


# In[46]:


def weighted_rating(x,M=m,C=c):
    v=x['vote_count']
    R=x['vote_average']
    return (v/(v+m) *R) + (m/(v+m)*C)


# In[47]:


list_movies['score'] = list_movies.apply(weighted_rating,axis=1)


# In[48]:


list_movies.head(3)


# In[52]:


list_movies = list_movies.sort_values('score',ascending=False)
list_movies.head(10)


# In[54]:


list_movies[['tittle','vote_count','vote_average','score']].head(10)


# In[ ]:




