#!/usr/bin/env python
# coding: utf-8

# In[1]:


from script import readData
from sklearn.cluster import DBSCAN
import numpy as np
from os import stat


# In[2]:


def writeData(eps, m_points, n_clusters):
    file = open("dbscanLoopResult.csv", 'a')
    if(stat("dbscanLoopResult.csv").st_size == 0):
        file.write("epsilon,m_points,n_clusters\n")
    file.write(eps + ',' + m_points + ',' + n_clusters + '\n')
    file.close()


# In[16]:


def dbscanLoop(path, max_eps = 10, max_m_points = 30):
    dataset = readData(path)
    dbscan = DBSCAN()
    epsi = 2
    while(epsi <= 100):
        for m_points in range(2, (max_m_points + 2), 2):
            dbscan.set_params(**{"eps" : (epsi/10), "min_samples" : m_points})
            dbscan.fit(dataset)
            clusters = set(dbscan.labels_)
            n_clusters = len(clusters) - (1 if -1 in clusters else 0)
            writeData(str(epsi/10), str(m_points), str(n_clusters))
        epsi = epsi + 2


# In[17]:


dbscanLoop("teste.csv")


# Scikit_scylax_rn_p3v2.csv
