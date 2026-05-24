import numpy as np
from sklearn.decomposition import PCA
def PCA_decom(A):
    temp = np.array(A, dtype=float)
    pca = PCA()
    transformed = pca.fit_transform(temp)
    return (
        pca.components_,
        pca.explained_variance_,
        transformed
    )