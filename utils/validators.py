def validate_cholesky(A):
    rows, cols = A.shape
    if rows != cols:
        return False, "Matrix must be square."
    if not np.allclose(A, A.T):
        return False, "Matrix must be symmetric."
    if np.any(np.linalg.eigvalsh(A) <= 0):
        return False, "Matrix must be positive definite."
    return True, ""
def validate_eva(A):
    rows, cols = A.shape
    if rows != cols:
        return False,"Matrix must be square."
    return True,""