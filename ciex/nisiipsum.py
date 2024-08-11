from scipy.special import softmax
import numpy as np

# Input vector of scores
scores = np.array([2.0, 1.0, 0.1])

# Compute the softmax
probabilities = softmax(scores)

print(probabilities)
