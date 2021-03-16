import numpy as np
from sympy import *

def eigen(X):
    matrixMean = np.mean(X, axis=0)
    cov = np.cov(X.T)
    eigVal, eigVec = np.linalg.eig(cov)
    print(f"EigenValue: {eigVal}\nEigenVector: {eigVec}")


array1 = np.array([[4,1],[2,3],[5,4],[1,0]])

eigen(array1)
