import numpy as np
def EVD_decom(A):
    temp = np.array(A, dtype=float)
    w, v = np.linalg.eig(temp)
    return w, v