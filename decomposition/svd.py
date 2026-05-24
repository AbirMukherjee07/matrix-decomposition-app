import numpy as np 
def SVD_decom(A):
    temp = np.array(A, dtype=float)
    U, S, VT = np.linalg.svd(temp)
    return U, S, VT