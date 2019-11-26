import numpy as np
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    if t >= 0:
        return 1
    return 0

def prediction(X, W, b):
    return stepFunction((np.matmul(X,W)+b)[0])

def update_weights(x, W, b, r, s=1.0):
    # Loop through weights and update them
    w = np.zeroes(len(W))
    for j,w in enumerate(W):
        W[j] = w + s * r * x[j]
    b = b + s * r
    return W,b

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate = 0.01):
    """
    Parameters
    ----------
    X : 2-D array
    y : 1-D array
    W : 1-D array
    b : float
    learn_rate : float
    """
    # Loop through the points and adjust as needed
    for i,x in enumerate(X):
        # Get prediction
        p = prediction(x,W,b)

        # Handle misclassifications
        if p < y[i]:
            # prediction = 0, truth = 1
            W,b = update_weights(x, W, b, learn_rate, 1.0)
        elif p > y[i]:
            # prediction = 1, truth = 0
            W,b = update_weights(x, W, b, learn_rate, -1.0)

    return W, b
    
# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines
