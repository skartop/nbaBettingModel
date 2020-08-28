import keras
import numpy
import pandas as pd
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

dataset = pd.read_csv('matchups/2009matchups.csv', delimiter=',')

for year in range(2010, 2019):
    print(year)
    if year == 2012:
        continue
    yeardataset = pd.read_csv('matchups/%dmatchups.csv' % year, delimiter=',')
    dataset = pd.concat([dataset, yeardataset])

dataset = dataset.drop(['home_team',
                        'visitor_team',
                        'home_points',
                        'visitor_points',
                        'favorite',
                        'total',
                        'winner',
                        'over',
                        'date'], axis=1)
cols = dataset.columns.tolist()
cover = cols[2]
spread = cols[1]
rest = cols[3:]
reordered_cols = [cover] + [spread] + rest
dataset = dataset[reordered_cols].to_numpy()
X = dataset[:, 1:]
y = dataset[:, 0]

# define the keras model
model = Sequential()
model.add(Dense(64, input_dim=19, activation='selu'))
model.add(Dense(32, activation='selu'))
model.add(Dense(32, activation='selu'))
model.add(Dense(16, activation='selu'))
model.add(Dense(2, activation='selu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, y, epochs=300, batch_size=10)

# evaluate the keras model
oldModel = keras.models.load_model('spreadpredictionmodel')
_, oldAccuracy = oldModel.evaluate(X, y)
_, accuracy = model.evaluate(X, y)
print('Old Accuracy: %.2f' % (oldAccuracy * 100))
print('Accuracy: %.2f' % (accuracy * 100))

# make class predictions with the model
predictions = model.predict_classes(X)
# summarize the first 5 cases
for i in range(15):
    print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

if accuracy > oldAccuracy:
    print("replacing old model!")
    model.save('spreadpredictionmodel')
