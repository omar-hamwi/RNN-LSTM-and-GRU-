# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LJzRF-idt4CMf16WxAVdULvIPss7w_12
"""

# Commented out IPython magic to ensure Python compatibility.
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# %matplotlib inline

dataset = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv')

# Importing the dataset
from sklearn.preprocessing import normalize
data_scaled = normalize(dataset)
data_scaled = pd.DataFrame(data_scaled, columns=dataset.columns)
X=data_scaled
X.head()

# Using the dendrogram to find the optimal number of clusters
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()

# Training the Hierarchical Clustering model on the dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 2, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

# Visualising the clusters
#plt.figure(figsize=(10, 7))  
plt.scatter(X['Milk'], X['Grocery'], c=hc.labels_)



#Calculating Silhouette Score
#Silhouette Score = (b-a)/max(a,b)
#X= np.random.rand(50,2)
Y= 2 + np.random.rand(50,2)
Z= np.concatenate((X,Y))
Z=pd.DataFrame(Z) #converting into data frame for ease

sns.scatterplot(Z[0],Z[1])

KMean= KMeans(n_clusters=2)
KMean.fit(Z)
label=KMean.predict(Z)
print(f'Silhouette Score(n=2): {silhouette_score(Z, label)}')

from sklearn.manifold import TSNE
import plotly.express as px
tsne = TSNE(n_components=2, random_state=0)
projections = tsne.fit_transform(X)
fig = px.scatter(
 projections, x=0, y=1,
 color=y_hc, labels={'color': 'spam'}
)
fig.show()

pip install umap-learn

import umap
import plotly.express as px
projections = umap.UMAP().fit_transform(X)
fig = px.scatter(
 projections, x=0, y=1,
 color=y_hc, labels={'color': 'spam'}
)
fig.show()

"""**The Elbow method is a very popular technique and the idea is to run k-means clustering for a range of clusters k (let???s say from 1 to 10) and for each value, we are calculating the sum of squared distances from each point to its assigned center(distortions).**"""

distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(X)
    distortions.append(kmeanModel.inertia_)

plt.figure(figsize=(16,8))
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

kmeanModel = KMeans(n_clusters=3)
kmeanModel.fit(X)

kmeanModel = KMeans(n_clusters=3)
kmeanModel.fit(X)



X['k_means']=kmeanModel.predict(X)
X['target']=iris['target']
fig, axes = plt.subplots(1, 2, figsize=(16,16))
axes[0].scatter(X[0], X[1], c=X['target'])
axes[1].scatter(X[0], X[1], c=X['k_means'], cmap=plt.cm.Set1)
axes[0].set_title('Actual', fontsize=18)
axes[1].set_title('K_Means', fontsize=18)

