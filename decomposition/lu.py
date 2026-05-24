import scipy.linalg as sla
import numpy as np
def LU_decom(A):
    temp = np.array(A, dtype=float)
    P, L, U = sla.lu(temp)
    return P, L, U
    