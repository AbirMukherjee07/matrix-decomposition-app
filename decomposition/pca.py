import numpy as np
def PCA_decom(A):
    temp = np.array(A)
    mean = np.mean(temp, axis=0)
    temp = temp - mean
    cov = np.cov(temp.T)
    w,v = np.linalg.eig(cov)
    idx = np.argsort(w)[::-1]
    v1 = v[:, idx[0]]
    v2 = v[:, idx[1]]
    u1 = v1/np.sqrt(v1.dot(v1))
    u2 = v2 - (v2.dot(u1))*u1
    u2 = u2/np.sqrt(u2.dot(u2))
    return (u1, u2)