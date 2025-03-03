import numpy as np


def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

training_input = np.array([[0,0,1],
                           [1,1,1],
                           [1,0,1],
                           [0,1,1]])

training_output = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3,1)) - 1

print("Random starting synaptic weights:")
print(synaptic_weights)

for iteration in range(100000):
    input_layer = training_input
    output_layer = sigmoid(np.dot(input_layer, synaptic_weights))

    error = training_output - output_layer
    adjustment = error * sigmoid_derivative(output_layer)
    synaptic_weights += np.dot(input_layer.T, adjustment)

print("Synaptic weights after training:")
print(synaptic_weights)

print("Output after training:")
print(output_layer)