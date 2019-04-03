import numpy as np  
  
def cost(theta, X, y):
  m, n = X.shape
  h = np.matmul(X, theta)
  sq = (h - y) * X
  return sq.sum() / m