import numpy as np

def stepFunction(sum):
    return int(sum >= 1)

def sigmoidFunction(sum):
    return 1 / (1 + np.exp(-sum))

def tahnFunction(sum):
    return (np.exp(sum) - np.exp(-sum)) / (np.exp(sum) + np.exp(-sum))

def reluFunction(sum):
    if (sum >= 0):
        return sum
    return 0

def linearFunction(sum):
    return sum

def softmaxFunction(x):
    ex = np.exp(x)
    return ex / ex.sum()