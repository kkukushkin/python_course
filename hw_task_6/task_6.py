from keras.models import Sequential
from keras.layers import Dense
import numpy as np

#task 1
np.set_printoptions(precision=2, floatmode='fixed', supress = True)
dataset = np.getfromtxt('data.txt', delimiter = ',', dtype = float)

for i in range(len(dataset[0]) - 1):
    dataset = dataset[~np.isnan(dataset[:,i])]

dataset = np.around(dataset[:, i])

Y = dataset[:, -1]
X = dataset[:, :9]

model = Sequential()
model.add(Dense(12, input_dim=9, activation = 'relu'))
model.add(Dense(12, activation = 'relu'))
model.add(Dense(12, activation = 'sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer = 'adam')
model.fit(X,Y, epochs = 15, batch_size = 10, verbose = 2)
predictions_0 = model.predict(np.array(X[:3]))
#print(predictions_0)

# task2

class NeuralNetwork:
    def __init__(self, epochs=15, batch_size=10, verbose = 2):
        self.epochs = epochs
        self.batch_size = batch_size
        self.verbose = verbose
        np.set_printoptions(precision=2, floatmode='fixed', suppress=True)

    def prepare_data(self, file_path):
        dataset = np.genfromtxt(file_path, delimiter=',', dtype=float)
        for i in range(len(dataset[0]) - 1):
            dataset = dataset[~np.isnan(dataset[:, i])]
        dataset = np.around(dataset[:, i])
        self.Y = dataset[:, -1]
        self.X = dataset[:, :9]

    def train(self):
        self.model = Sequential()
        self.model.add(Dense(12, input_dim=9, activation='relu'))
        self.model.add(Dense(8, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))
        self.model.compile(loss='binary_crossentropy', optimizer='adam')
        self.model.fit(self.X, self.Y, epochs=self.epochs, batch_size=self.batch_size, verbose=self.verbose)

    def inference(self, data_to_predict):
        predictions = self.model.predict(np.array(data_to_predict))
        return predictions


nn = NeuralNetwork(epochs=15, batch_size=10)
nn.prepare_data('data.txt')
nn.train()
predictions_0 = nn.inference(nn.X[:3])
#print(predictions_0)