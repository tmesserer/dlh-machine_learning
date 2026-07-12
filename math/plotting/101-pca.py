#!/usr/bin/env python3
# %%
"""Module for plotting with matplotlib and pyplot"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

# your code here
plt.figure(figsize=(6.4, 4.8))
ax = plt.subplot(projection='3d')
ax.zaxis.labelpad = -1.5
plt.subplots_adjust(right=0.8)

ax.set_title('PCA of Iris Dataset')
ax.set_xlabel('U1')
ax.set_ylabel('U2')
ax.set_zlabel('U3')

x_data = pca_data[:, 0]
y_data = pca_data[:, 1]
z_data = pca_data[:, 2]

ax.scatter(xs=x_data,
           ys=y_data,
           zs=z_data,
           c=labels,
           cmap='plasma')

plt.show()
