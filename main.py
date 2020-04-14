#!/usr/bin/env python
# coding: utf-8

# In[1]:


from script import analyzeAll, export


# In[2]:


def main(task, path, params, opt = {}):
    tasks = {"analyzeAll" : analyzeAll,
            "export" : export,}
    tasks[task](path, *params, **opt)


# In[5]:


main("analyzeAll", "iris.csv", [(2,6), (1,5)], {"label_col" : "variety"})
main("export", "iris.csv", ["KMeans"], {"k" : 3, "seed" : 5, "label_col" : "variety"})

