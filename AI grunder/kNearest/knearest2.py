import numpy as np
import pandas as pd
from sklearn import preprocessing, neighbors, model_selection

df = pd.read_csv('votering.csv')
df.drop('punkt', 1, inplace = True)
df = df[['rost', 'parti', 'fodd']]

encoder = preprocessing.LabelEncoder()

df.replace('-', 'KD', inplace = True)
input_labels = ['C', 'KD', 'M', 'L', 'MP', 'S', 'V', 'SD'] # C ---> 0   KD ---> 1   L ---> 2    M ---> 3    MP ---> 4   S ---> 5    SD ---> 6   V ---> 7
encoder.fit(input_labels)
df['parti']    = encoder.transform(df['parti'])

input_labels = ['Nej', 'Ja', 'Frånvarande', 'Avstår'] # Avstår ---> 0   Frånvarande ---> 1   Ja ---> 2   Nej ---> 3
encoder.fit(input_labels)
df['rost']    = encoder.transform(df['rost'])

df.replace('?', '-9999', inplace = True)

X = np.array(df.drop(['rost'], 1))
Y = np.array(df['rost'])

XTrain, XTest, YTrain, YTest = model_selection.train_test_split(X, Y, test_size = 0.2)
XTrain                       = XTrain.reshape(len(XTrain), -1)
YTrain                       = YTrain.reshape(len(YTrain), -1)

clf      = neighbors.KNeighborsClassifier()
clf.fit(XTrain, YTrain)
acc = clf.score(XTest, YTest)
print(df.iloc[0])
print(XTrain[0])

print('Acc:', acc, '\nThis is Pog!')

exampleMeasure = np.array([[5, 1973], [3, 1987]])
exampleMeasure = exampleMeasure.reshape(len(exampleMeasure), -1)

prediction = clf.predict(exampleMeasure)
print(prediction)

decoded = encoder.inverse_transform(prediction)
print('Decoded:', list(decoded))