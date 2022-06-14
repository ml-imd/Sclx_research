#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Script import analyzeAll, export


# In[2]:


def main(task, path, params, opt = {}):
    tasks = {"analyzeAll" : analyzeAll,
            "export" : export,}
    tasks[task](path, *params, **opt)


# In[1]:


#main("analyzeAll", "iris.csv", [(2,3), (1,)], {"label_col" : "variety"})
#for k in range(2,11):
#    main("export", "base_v1.csv", ["AgglomerativeClustering"], {"k" : k})

