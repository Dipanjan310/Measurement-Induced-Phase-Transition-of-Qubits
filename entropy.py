import numpy as np

def calculate_entropy(initial_state, N1, N):
    matrix = initial_state.reshape(2**N1, 2**(N-N1))
    p,q,r = np.linalg.svd(matrix)
    entropy = np.sum(q**2*np.log(q**2+1e-40))
    entropy = -(entropy)
    return entropy