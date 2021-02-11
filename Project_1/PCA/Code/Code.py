# -*- coding: utf-8 -*-
"""Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iJQDE6aQi0sMo5Jjsy8DxBIqcv-6cuLs

**PCA**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# from google.colab import drive
# drive.mount('/content/drive')
datasets = ['pca_a','pca_b','pca_c']
for i in datasets:
  df = pd.read_csv('/content/drive/My Drive/DM Proj1/'+i+'.txt', sep="\t", header=None)
  X = df.iloc[:, :-1]
  X = (X - np.min(X)) / (np.max(X) - np.min(X)).values
  Y = df.iloc[:,-1]
  # print(Y)
  mean = np.mean(X.T, axis=1)
  center = X - mean
  cov = np.cov(center.T)
  eig_val, eig_vect = np.linalg.eig(cov)
  PC = 2
  P = eig_vect.T[0:PC]
  new_data = np.dot(X, P.T)
  # print(new_data)
  labels, index = np.unique(Y, return_inverse=True)
  # print(labels)
  fig, ax = plt.subplots()
  fig.set_size_inches(8, 8)
  dataset = pd.DataFrame({'one': new_data[:, 0], 'two': new_data[:, 1]})
  sc = ax.scatter(dataset['one'], dataset['two'], marker = 'o', c = index, alpha = 0.8)
  ax.set_xlabel('Feature 1', fontsize = 10)
  ax.set_ylabel('Feature 2', fontsize = 10)
  ax.set_title('PCA Dimensionality Reduction for' +' '+ i +' dataset', fontsize = 15)
  ax.legend(sc.legend_elements()[0], labels)
  plt.show()

"""**SVD**"""

from sklearn.decomposition import TruncatedSVD

datasets = ['pca_a','pca_b','pca_c']
for i in datasets:
  df = pd.read_csv('/content/drive/My Drive/DM Proj1/'+i+'.txt', sep="\t", header=None)
  X = df.iloc[:, :-1]
  X = (X - np.min(X)) / (np.max(X) - np.min(X)).values
  Y = df.iloc[:,-1]

  svd = TruncatedSVD(n_components=2)
  # svd.fit(X)
  new_data = svd.fit_transform(X)
  labels, index = np.unique(Y, return_inverse=True)
  # print(labels)
  fig, ax = plt.subplots()
  fig.set_size_inches(8, 8)
  dataset = pd.DataFrame({'one': new_data[:, 0], 'two': new_data[:, 1]})
  sc = ax.scatter(dataset['one'], dataset['two'], marker = 'o', c = index, alpha = 0.8)
  ax.set_xlabel('Feature 1', fontsize = 10)
  ax.set_ylabel('Feature 2', fontsize = 10)
  ax.set_title('SVD Dimensionality Reduction for' +' '+ i +' dataset', fontsize = 15)
  ax.legend(sc.legend_elements()[0], labels)
  plt.show()

"""**t-SNE**"""

# import time
from sklearn.manifold import TSNE

datasets = ['pca_a','pca_b','pca_c']
for i in datasets:
  df = pd.read_csv('/content/drive/My Drive/DM Proj1/'+i+'.txt', sep="\t", header=None)
  X = df.iloc[:, :-1]
  X = (X - np.min(X)) / (np.max(X) - np.min(X)).values
  # print(X)
  Y = df.iloc[:,-1]

  # time_start = time.time()
  tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
  new_data = tsne.fit_transform(X)
  labels, index = np.unique(Y, return_inverse=True)
  # print(labels)
  fig, ax = plt.subplots()
  fig.set_size_inches(8, 8)
  dataset = pd.DataFrame({'one': new_data[:, 0], 'two': new_data[:, 1]})
  sc = ax.scatter(dataset['one'], dataset['two'], marker = 'o', c = index, alpha = 0.8)
  ax.set_xlabel('Feature 1', fontsize = 10)
  ax.set_ylabel('Feature 2', fontsize = 10)
  ax.set_title('t-SNE Dimensionality Reduction for' +' '+ i +' dataset', fontsize = 15)
  ax.legend(sc.legend_elements()[0], labels)
  plt.show()