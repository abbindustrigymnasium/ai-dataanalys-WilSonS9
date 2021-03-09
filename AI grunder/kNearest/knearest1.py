import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from collections import Counter

style.use('fivethirtyeight')

dataset   = {
    'Husr': [[35,35],[37,37],[42,32],[60,34],[63,36],[61,35],[65,22],[76,16]],
    'Hyresrättg': [[23,12], [26,33], [28,20], [19,6], [97,9]],
    'BostadsRättb': [[57,45],[24,28],[26,30]],
    'Radhusy': [[37,21],[45,47],[32,42],[55,24],[61,25]]
}
newFeature = [50,45]

def kNearest(data,predict,k=3):
    if len(data) >= k:
        warnings.warn('k is too small')
    distances = []
    for group,features in data.items():
        for feature in features:
            distances.append((np.linalg.norm(np.array(feature)-np.array(predict)),group))
    votes       = [i[1] for i in sorted(distances)[:k]]
    votesResult = Counter(votes).most_common(1)
    return votesResult[0][0]

print('Du bor i: ' +  kNearest(dataset,newFeature,5)[:-1])

[[plt.scatter(ii[0], ii[1], color = i[-1]) for ii in dataset[i]] for i in dataset]
plt.scatter(newFeature[0],newFeature[1], s=100)
plt.ylabel = 'Inkomst'
plt.xlabel = 'Ålder'
plt.show()