import numpy as np
#import state_visualization as sv
#import two_qubit_gates as tqg
from numba import njit, prange

@njit(cache=True, parallel=True)
def two_qubit(initial_state,op,p1,p2,N):
    
    final_state=np.zeros(2**N, dtype = np.complex128)
    r1 = 2**(N-p1)
    r2 = 2**(N-p2)
    for i in prange(2**N):
        q1 = (r1&i)/r1
        q2 = (r2&i)/r2
        u = int(2*q1+q2)
        w = r1 + r2
        v3 = w | i
        v2 = r2^v3
        v1 = r1^v3
        v0 = w^v3
        final_state[i] = op[u,0]*initial_state[v0] + op[u,1]*initial_state[v1] + op[u,2]*initial_state[v2]+ op[u,3]*initial_state[v3] 
    return final_state

# def func2():
#     cx = tqg.CX_gate()
#     N = 4
#     p1 = 3
#     p2 = 4
#     initial_state = np.zeros(2**N, dtype = np.complex128)
#     initial_state[11] = 1
#     final_state =  two_qubit(initial_state,cx,p1,p2,N)
#     sv.visualize_state(initial_state, N)
#     sv.visualize_state(final_state,N)
    
    
# # func2()  

































# def two_qubit(initial_state, op, p1, p2, N):
#     final_state = np.zeros(2**N, dtype = np.complex128)
#     r1 = 2**(N-p1)
#     r2 = 2**(N-p2)
#     for i in range(2**N):
#         q1 = (r1 & i)/r1
#         q2 = (r2 & i)/r2
#         u = int(2*q1+q2)
#         w = r1+r2
#         v3 = w | i
#         v2 = r2^v3
#         v1 = r1^v3
#         v0 = w^v3
#         final_state[i] = op[u, 0]*initial_state[v0]+op[u, 1]*initial_state[v1]+op[u, 2]*initial_state[v2]+op[u, 3]*initial_state[v3]
#     return final_state

# def tw():
#     N=4
#     p1 = 1
#     p2 = 2
#     cx= tqg.CX_gate()
#     initial_state = np.zeros(2**N, dtype = np.complex128)
#     initial_state[11] = 1
#     final_state = two_qubit(initial_state, cx, p1, p2, N)
#     sv.visualize_state(initial_state, N)
#     sv.visualize_state(final_state, N)
# tw()