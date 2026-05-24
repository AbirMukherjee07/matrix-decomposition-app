import numpy as np
def QR_decom(A):
    temp = np.array(A, dtype=float)
    Q, R = np.linalg.qr(temp)
    return Q,R
    