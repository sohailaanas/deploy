#!/usr/bin/env python
# coding: utf-8

# In[5]:


from fastapi import FastAPI
import uvicorn


# In[6]:


app = FastAPI()


# In[19]:


@app.get("/{name}")
def hello(name):
    return {"Hello {} and welcome to this API".format(name)}


# In[20]:


@app.get("/")
def greet():
    return{"Hello World!"}


# In[21]:


if __name__ =="__main__":
    uvicorn.run(app)


# In[ ]:





# In[ ]:




