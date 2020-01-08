#!/usr/bin/env python
# coding: utf-8

# In[43]:


import h2o
import pandas as pd


# In[44]:


h2o.init(nthreads=-1)


# In[154]:


credata = pd.read_csv('credata.csv', sep = ',',names=['Gender','Age','Credit','Children','State','City','Occupation','Hourly Wage','Current Bank','Married','Education','Citizenship','Insurance','Zipcode','Income','Accepted'])
credata = credata.replace('+','Yes')
credata = credata.replace('-','No')
credata = credata.replace('a','Male')
credata = credata.replace('b','Female')


# In[155]:


newdata = h2o.H2OFrame(credata)


# In[156]:


newdata.tail()


# In[157]:


credata.tail()


# In[158]:


features = newdata.drop('Accepted', axis=1)


# In[159]:


features


# In[160]:


newdata['Gender'] = newdata['Gender'].asfactor()


# In[161]:


newdata['Accepted'] = newdata['Accepted'].asfactor()


# In[162]:


newdata['Gender'].table()


# In[163]:


newdata['Accepted'].table()


# In[164]:


features = list(newdata.columns)
features.remove('Accepted')
results = 'Accepted'
features


# In[165]:


cred_split = newdata.split_frame(ratios=[0.8], seed =1234)


# In[166]:


cred_train = cred_split[0]
cred_test = cred_split[1]


# In[167]:


cred_train.shape


# In[168]:


cred_test.shape


# In[169]:


from h2o.estimators.naive_bayes import H2ONaiveBayesEstimator


# In[170]:


cred_model = H2ONaiveBayesEstimator(model_id='cred_model', laplace=1)


# In[171]:


cred_model.train(x=features, y=results, training_frame=cred_train)
cred_model.train(x=features, y=results, training_frame=cred_test)


# In[172]:


cred_model.model_performance(cred_train)


# In[173]:


cred_model.model_performance(cred_test)


# In[174]:


cred_testing = cred_model.predict(cred_test)
cred_testing.tail()


# In[175]:


cred_testing = cred_model.predict(cred_train)


# In[176]:


cred_testing.head()


# 
