#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.cluster import *
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
from ntpath import split, basename
from os import stat


# In[2]:


def readData(path, label_col = None, return_dataframe = False):
    dataframe = pd.read_csv(path)
    if(label_col is None):
        X = dataframe.to_numpy()
    else:
        X = np.array(dataframe.drop(label_col, axis = 1))
    
    if(return_dataframe):
        return X, dataframe
    return X


# In[3]:


def cluster(method, parameters = {}):
    methods = {"KMeans" : KMeans,
               "AffinityPropagation" : AffinityPropagation,
               "AgglomerativeClustering" : AgglomerativeClustering,
               "Birch" : Birch,
               "DBSCAN" : DBSCAN,
               "FeatureAgglomeration" : FeatureAgglomeration,
               "MiniBatchKMeans" : MiniBatchKMeans,
               "MeanShift" : MeanShift,
               "OPTICS" : OPTICS,
               "SpectralClustering" : SpectralClustering,
               "SpectralBiclustering" : SpectralBiclustering,
               "SpectralCoclustering" : SpectralCoclustering,
               "GaussianMixture": GaussianMixture,}
               
    return methods[method](**parameters)


# In[4]:


def getScores(X, clusters):
    slt_score = silhouette_score(X, clusters)
    db_score = davies_bouldin_score(X, clusters)
    return (slt_score, db_score)


# In[5]:


def fileNameFromPath(path):
    head, tail = split(path)
    return tail or basename(head)


# In[6]:


def writeData(file_name, method, slt_score, db_score, k = '-', seed = '-'): 
    file = open(file_name, 'a')
    if(stat(file_name).st_size == 0):
        file.write("method,n_cluster,seed,silhoutte,db\n")
        print("method,n_cluster,seed,silhoutte,db\n")
    
    file.write(method + ',' + k + ',' + seed + ',' + slt_score + ',' + db_score + '\n')
    print(method + ',' + k + ',' + seed + ',' + slt_score + ',' + db_score + '\n')
    
    file.close()


# In[7]:


def analyze(path, method, file_name, parameters = {}, k_range = None, seed_values = None, label_col = None, export_dataset = False):
    dataset = readData(path, label_col)
    try:
        if(k_range is not None and seed_values is not None):
            for x in range(k_range[0], k_range[1]):
                if(method == "SpectralBiclustering"):
                    parameters["n_clusters"] = (x, dataset.shape[1])
                elif(method == "GaussianMixture"):
                    parameters["n_components"] = x;
                else:
                    parameters["n_clusters"] = x
                for y in seed_values:
                    parameters["random_state"] = y
                    cluster_method = cluster(method, parameters)
                    cluster_method.fit(dataset)
                    if(method == "SpectralBiclustering" or method == "SpectralCoclustering"):
                        scores = getScores(dataset, cluster_method.row_labels_)
                    elif(method == "GaussianMixture"):
                        scores = getScores(dataset, cluster_method.predict(dataset))
                    else:
                        scores = getScores(dataset, cluster_method.labels_)
                    writeData(file_name, method, k = str(x), seed = str(y), slt_score = str(scores[0]), db_score = str(scores[1]))
        elif(k_range is not None and seed_values is None):
            for x in range(k_range[0], k_range[1]):
                parameters["n_clusters"] = x
                cluster_method = cluster(method, parameters)
                cluster_method.fit(dataset)
                scores = getScores(dataset, cluster_method.labels_)
                writeData(file_name, method, k = str(x), slt_score = str(scores[0]), db_score = str(scores[1]))
        elif(k_range is None and seed_values is not None):
            for y in seed_values:
                parameters["random_state"] = y
                cluster_method = cluster(method, parameters)
                cluster_method.fit(dataset)
                scores = getScores(dataset, cluster_method.labels_)
                writeData(file_name, method, seed = str(y), slt_score = str(scores[0]), db_score = str(scores[1]))
        else:
            cluster_method = cluster(method, parameters)
            cluster_method.fit(dataset)
            scores = getScores(dataset, cluster_method.labels_)
            writeData(file_name, method, slt_score = str(scores[0]), db_score = str(scores[1]))
    except MemoryError:
        print("MemoryError in " + path)


# In[17]:


def export(path, method, k = None, seed = None, label_col = None, parameters = {}):
    if(k is not None and seed is not None):
        file_name = "exported" + '_' + fileNameFromPath(path) + '_' + method + '_' + str(k) + '_' + str(seed) + '.csv'
    elif(k is not None and seed is None):
        file_name = "exported" + '_' + fileNameFromPath(path) + '_' + method + '_' + str(k) + '.csv'
    elif(k is None and seed is not None):
        file_name = "exported" + '_' + fileNameFromPath(path) + '_' + method + '_' + str(seed) + '.csv'
    else:
        file_name = "exported" + '_' + fileNameFromPath(path) + '_' + method + '.csv'
    dataset, dataframe = readData(path, label_col, True)
    if(k is not None):
        parameters["n_clusters"] = k
    if(seed is not None):
        parameters["random_state"] = seed
    cluster_method = cluster(method, parameters)
    cluster_method.fit(dataset)
    scores = getScores(dataset, cluster_method.labels_)
    print("Silhouette: " + str(scores[0]))
    print("Davies Bouldin: " + str(scores[1]))
    if(method == "SpectralBiclustering" or method == "SpectralCoclustering"):
        dataframe["cluster"] = cluster_method.row_labels_
    else:
        dataframe["cluster"] = cluster_method.labels_
        
    dataframe.to_csv(file_name, index = False)
    
    parameters.clear()


# In[13]:


def analyzeAll(path, k_range, seed_values, label_col = None):
    file_name = fileNameFromPath(path) + '_' + 'k' + str(k_range) +'_' + 'seed' + str(seed_values) + '.csv'
    have_none = ["DBSCAN", "OPTICS", "MeanShift"]
    have_k = ["AgglomerativeClustering", "Birch"]
    have_seed_and_k = ["KMeans", "MiniBatchKMeans", "GaussianMixture"]
    
    for method in have_seed_and_k:
        analyze(path, method, file_name, k_range = k_range, seed_values = seed_values, label_col = label_col, parameters = {})
    for method in have_k:
        analyze(path, method, file_name, k_range = k_range, label_col = label_col, parameters = {})
    for method in have_none:
        analyze(path, method, file_name, label_col = label_col, parameters = {})

