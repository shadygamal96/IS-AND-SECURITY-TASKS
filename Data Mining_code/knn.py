

import numpy as np
import pandas as pd

train = pd.read_csv('iris.data')
train.head()

cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
train.rename(columns = {cols[0]:0, cols[1]:1, cols[2]:2, cols[3]:3}, inplace=True)
train['distance'] = 9999
train.head()

target = pd.Series([7.0, 3.1, 5.6, 1.9])
target

train['distance'] = ((train.iloc[:,0]-target[0])**2 + (train.iloc[:,1]-target[1])**2 + (train.iloc[:,2]-target[2])**2 + (train.iloc[:,3]-target[3])**2) ** 0.5
train.iloc[::10]

k = 7
train = train.sort_values('distance', ascending=True)
knn = list(train.head(k).species)
knn

from statistics import mode
print(mode(knn))

import matplotlib.pyplot as plt
colors = {'Iris-setosa':'red', 'Iris-virginica':'blue', 'Iris-versicolor':'green'}
plt.scatter(
    train[2], 
    train[3], 
    c=train['species'].map(colors))
plt.scatter(target[2], target[3], c='orange')
plt.xlabel(cols[2])
plt.ylabel(cols[3])
plt.title('Iris Data Scatter Plot')